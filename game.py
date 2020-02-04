import ninja
import pygame
from pygame.locals import *
from colors import *


class Game():
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.ninja = ninja.Ninja(700, 500)
        # self.testo = pygame.image.load(r'testoxD.jpg')

    def play(self, window):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.keyboard()
            self.mouse()
            self.ninja.move()
            window.fill(black)
            self.ninja.draw(window)
            pygame.display.update()
            pygame.time.delay(20)

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
            
    def keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[K_r]:
            self.ninja.reset()
        if keys[K_SPACE]:
            self.ninja.jump()


print("Ladowanko gry: {}".format(__name__))
