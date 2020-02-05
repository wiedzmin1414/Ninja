import ninja
import pygame
from pygame.locals import *
from colors import *
from bullets_and_VPoint import Bullet, VPoint


class Game():
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.ninja = ninja.Ninja2(700, 500) #Ninja2 is available too!
        self.control = { 
            "jump": (K_SPACE, self.ninja.jump),
            "reset": (K_r, self.ninja.reset),
            "normal_tribe" : (K_u, self.speed_up),
            "slow_tribe" : (K_d, self.speed_down),
        }
        self.list_of_bullets = []
        self.lag = 30
        
    def speed_up(self):
        if self.lag > 20:
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

    def mouse(self):
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_position = pygame.mouse.get_pos()
        #print(mouse_buttons)
        if mouse_buttons[0] and not self.ninja.is_hanging:
            print("Wisi")
            self.ninja.establish_hang(*mouse_position)
        if not mouse_buttons[0] and self.ninja.is_hanging:
            print("Konczy wisiec")
            self.ninja.stop_hanging()
        if mouse_buttons[2]:
            self.list_of_bullets.append(Bullet(self.ninja.position, mouse_position))
            
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
        window.fill(black)
        self.ninja.draw(window)
        for bullet in self.list_of_bullets:
            bullet.draw(window)
        pygame.display.update()
        pygame.time.delay(self.lag)
        
    def move_all_object(self):
        self.ninja.move()
        for bullet in self.list_of_bullets:
            bullet.move()
            
    def delete_unnedded_items(self):
        self.list_of_bullets = [bullet for bullet in self.list_of_bullets if bullet.is_visible(0, 0, self.max_x, self.max_y)]
            

print("Ladowanko gry: {}".format(__name__))
