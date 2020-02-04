import ninja
import pygame
from pygame.locals import *
from colors import *
from bullets_and_VPoint import Bullet, VPoint


class Game():
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.ninja = ninja.Ninja(700, 500)
        # self.testo = pygame.image.load(r'testoxD.jpg')
        self.control = { 
            "jump": (K_SPACE, self.ninja.jump),
            "reset": (K_r, self.ninja.reset)
        }
        self.list_of_bullets = []

    def play(self, window):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.keyboard()
            self.mouse()
            self.move_all_object()
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
        pygame.time.delay(20)
        
    def move_all_object(self):
        self.ninja.move()
        for bullet in self.list_of_bullets:
            bullet.move()
            

print("Ladowanko gry: {}".format(__name__))
