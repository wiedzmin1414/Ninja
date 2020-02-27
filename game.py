import ninja
import pygame
from pygame.locals import *
from colors import red, blue, black
from VPoint import  VPoint
from bullets import Bullet, Link_shuriken
import ceiling
import numpy as np


class Game():
    def __init__(self, max_x, max_y,  lag=10):
        self.max_x = max_x
        self.max_y = max_y
        self.ninja = ninja.Ninja(0, 100)
        self.control = { 
            # "action name" = (key, action)
            "jump": (K_w, self.ninja.jump, ),
            "reset": (K_r, self.ninja.reset,),
            "speed up" : (K_u, self.speed_up),
            "speed down" : (K_i, self.speed_down),
            "shorten link" : (K_w, self.ninja.shorten_link),
            "extend link" : (K_s, self.ninja.extend_link),
        }
        self.run = True
        self.shuriken_image = pygame.image.load('images/shuriken/shuriken3.png')
        self.shuriken_size = 10
        self.shuriken_image2 = pygame.image.load('images/shuriken/shuriken4.png')
        self.shuriken_size2 = 10
        self.list_of_bullets = []
        self.lag = lag
        self.ceiling = ceiling.Ceiling(self.max_x, 300, 300, red, 10)
        self.font = pygame.font.SysFont("comicsansms", 24)
        self.big_font = pygame.font.SysFont("comicsansms", 100)
        self.delta_view = 0
        
    def speed_up(self):
        if self.lag > 19:
            self.lag -= 10
            print("Speed up, lag=", self.lag)
        
    def speed_down(self):
        if self.lag < 400:
            self.lag += 20
            print("Speed down, lag=", self.lag)

    def play(self, window):
        self.generate_next_frame(window)
        self.wait_to_start(window)
        while self.run:
            self.still_play()
            self.keyboard()
            self.mouse()
            self.move_all_object()
            #self.delete_unnedded_items()
            self.generate_next_frame(window)
            self.render_frame()
            self.delete_unnedded_items()
            self.handle_shuriken()
            self.handle_delta_view()
            self.generate_ceiling()

    def still_play(self):
        for event in pygame.event.get():  # press ESC
            if event.type == pygame.QUIT:
                self.run = False
        if self.ninja.position.get_y() > self.max_y:
            self.run = False

        if not self.run:
            self.game_over()

    def game_over(self):
        pygame.time.delay(1000)

    def generate_ceiling(self):
        if self.ninja.position.get_x() > self.ceiling.get_end() - 2*self.max_x:
            #print(self.ceiling.get_end())
            self.ceiling.generate()

    def handle_shuriken(self):
        if self.ninja.shuriken: # if shuriken exist
            if self.ninja.shuriken.above_ceiling(self.ceiling.height) and not self.ninja.is_hanging:
                #print("Shuriken poza zasiegiem!")
                x = self.ninja.shuriken.position.get_x()
                y = self.ninja.shuriken.position.get_y()
                if not self.ninja.shuriken.have_been_checked:
                    self.ninja.shuriken.have_been_checked = True
                    if x in self.ceiling:
                        #print("Wisi")
                        self.ninja.establish_hang(x, y)

    def mouse(self):
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_position = list(pygame.mouse.get_pos())
        mouse_position[0] += self.delta_view
        if mouse_buttons[0] and not self.ninja.shuriken and self.ninja.position.get_y() >= 0:
            #print("Leci shuriken")
            self.ninja.shuriken = Link_shuriken(self.ninja.link_hand(), mouse_position, speed=50)
        if not mouse_buttons[0] and self.ninja.shuriken:
            #print("Konczy wisiec")
            if self.ninja.is_hanging:
                self.ninja.stop_hanging()
            else:
                self.ninja.shuriken = None
        if mouse_buttons[2]:
            if self.ninja.is_shot_available():
                self.ninja.shot()
                self.list_of_bullets.append(Bullet(self.ninja.armed_hand(), mouse_position, speed=50))
            
    def keyboard(self):
        pressed_keys = pygame.key.get_pressed()
        for key, action  in self.control.values():
            if pressed_keys[key]:
                action()

    def score(self):
        return str(int((self.ninja.position.get_x() - 100) // 10))

    def handle_delta_view(self):
        if not self.ninja.is_hanging: #  delta_view change only when ninja is flying
            delta = self.ninja.position.get_x() - self.delta_view
            if delta > 0: #  delta_view will never go back
                if delta < self.max_x / 4:
                    self.delta_view += 0.7*self.ninja.speed.get_x()
                elif delta < self.max_x / 2:
                    self.delta_view += 1.2*self.ninja.speed.get_x()
                else:
                    self.delta_view += 2*self.ninja.speed.get_x()

    def generate_next_frame(self, window):
        window.fill(blue)
        self.ceiling.draw(window, self.delta_view, self.delta_view, self.max_x)
        #window.blit(self.background, [0,0])
        self.ninja.draw(window, self.shuriken_image, self.shuriken_size, self.delta_view)
        for bullet in self.list_of_bullets:
            bullet.draw(window, self.shuriken_image2, self.shuriken_size2, self.delta_view)
        score_text = self.font.render("Score: " + self.score(), True, red)
        window.blit(score_text, (10, 10))
    
    def render_frame(self):
        pygame.display.update()
        pygame.time.delay(self.lag)
    
    def wait_to_start(self, window):
        count = 3
        while count:
            self.generate_next_frame(window)
            count_text = self.font.render(str(count), True, red)
            window.blit(count_text, (self.max_x // 2, self.max_y // 2))
        ## NOW WAIT! ##
            pygame.display.update()
            pygame.time.delay(1000)
            count -= 1
        print("Start")

    def move_all_object(self):
        self.ninja.move()
        for bullet in self.list_of_bullets:
            bullet.move()

    def delete_unnedded_items(self):
        self.list_of_bullets = [bullet for bullet in self.list_of_bullets
                                if bullet.is_visible(self.delta_view, 0, self.max_x + self.delta_view, self.max_y)]
            

print("Ladowanko gry: {}".format(__name__))
