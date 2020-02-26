import ninja
import pygame
from pygame.locals import *
from colors import *
from VPoint import  VPoint
from bullets import Bullet, Link_shuriken
import ceiling


class Game():
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.ninja = ninja.Ninja(700, 500) #Ninja2 is available too!
        self.control = { 
            # "action name" = (key, action, [True, False]available in hanging mode)
            "jump": (K_w, self.ninja.jump, ),
            "reset": (K_r, self.ninja.reset,),
            "speed up" : (K_u, self.speed_up),
            "speed down" : (K_i, self.speed_down),
            "shorten link" : (K_w, self.ninja.shorten_link),
            "extend link" : (K_s, self.ninja.extend_link),
        }
        self.shuriken_image = pygame.image.load('images/shuriken/shuriken3.png')
        self.shuriken_size = 10
        self.shuriken_image2 = pygame.image.load('images/shuriken/shuriken4.png')
        self.shuriken_size2 = 10
        self.list_of_bullets = []
        self.lag = 100
        #self.background = pygame.image.load('tlo.jpg')
        self.ceiling = ceiling.Ceiling(self.max_x, 300, 300, red, 10) 
        
    def speed_up(self):
        if self.lag > 19:
            self.lag -= 10
            print("Speed up, lag=", self.lag)
        
    def speed_down(self):
        if self.lag < 400:
            self.lag += 20
            print("Speed down, lag=", self.lag)

    def play(self, window):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.keyboard()
            self.mouse()
            self.move_all_object()
            self.delete_unnedded_items()
            self.generate_next_frame(window)
            self.handle_shuriken()

    def handle_shuriken(self):
        if self.ninja.shuriken: # is shuriken exist
            if self.ninja.shuriken.above_ceiling(self.ceiling.height) and not self.ninja.is_hanging:
                #print("Shuriken poza zasiegiem!")
                x = self.ninja.shuriken.position.get_x()
                if x in self.ceiling:
                    print("Wisi")
                    self.ninja.establish_hang(x, 0)

    def mouse(self):
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_position = pygame.mouse.get_pos()
        #print(mouse_buttons)
        '''
        if mouse_buttons[0] and not self.ninja.is_hanging:
            print("Wisi")
            self.ninja.establish_hang(*mouse_position)
        if not mouse_buttons[0] and self.ninja.is_hanging:
            print("Konczy wisiec")
            self.ninja.stop_hanging()
        '''
        if mouse_buttons[0] and not self.ninja.shuriken:
            print("Leci shuriken")
            self.ninja.shuriken = Link_shuriken(self.ninja.position, mouse_position)
        if not mouse_buttons[0] and self.ninja.shuriken:
            print("Konczy wisiec")
            if self.ninja.is_hanging:
                self.ninja.stop_hanging()
            else:
                self.ninja.shuriken = None
        if mouse_buttons[2]:
            if self.ninja.is_shot_available():
                self.ninja.shot()
                self.list_of_bullets.append(Bullet(self.ninja.armed_hand(), mouse_position))
            
    def keyboard(self):
        pressed_keys = pygame.key.get_pressed()
        #if keys[self.control["reset"]]:
        #    self.ninja.reset()
        #if keys["jump"]:
        #    self.ninja.jump()
        for key, action  in self.control.values():
            if pressed_keys[key]:
                action()
    
    def generate_next_frame(self, window):
        window.fill(blue)
        self.ceiling.draw(window)
        #window.blit(self.background, [0,0])
        self.ninja.draw(window, self.shuriken_image, self.shuriken_size)
        for bullet in self.list_of_bullets:
            bullet.draw(window, self.shuriken_image2, self.shuriken_size2)
        ## NOW WAIT! ##
        pygame.display.update()
        pygame.time.delay(self.lag)
        
    def move_all_object(self):
        self.ninja.move()
        for bullet in self.list_of_bullets:
            bullet.move()
            
    def delete_unnedded_items(self):
        self.list_of_bullets = [bullet for bullet in self.list_of_bullets if bullet.is_visible(0, 0, self.max_x, self.max_y)]
            

print("Ladowanko gry: {}".format(__name__))
