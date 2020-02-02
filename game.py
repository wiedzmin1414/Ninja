import ninja
import pygame
from pygame.locals import *
from colors import *
import time


class Game():
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.ninja = ninja.Ninja(50, 50)
        # self.testo = pygame.image.load(r'testoxD.jpg')

    def play(self, window):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.mouse()
            self.ninja.move()
            self.ninja.draw(window)
            pygame.draw.rect(window, (255, 0, 0), (0, 0, 10, 10))
            pygame.draw.rect(window, (0, 255, 0), (*self.ninja.position.values(), 10, 10))
            time.sleep(1)

    def mouse(self):
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_position = pygame.mouse.get_pos()
        print(mouse_buttons)
        if mouse_buttons[0]:
            if not self.ninja.is_hanging:
                self.ninja.establish_hang(*mouse_position)
        if not mouse_buttons[0]:
            self.ninja.is_hanging = False
            self.ninja.stop_hanging()

print("Ladowanko gry: {}".format(__name__))