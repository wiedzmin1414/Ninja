import pygame
from VPoint import VPoint
import ninja


class Enemy(ninja.Ninja):
    def __init__(self, x, y, fly_to_point=None, x_acc=-1, y_acc=-1, speed=5):
        self.position = VPoint(x, y)
        if fly_to_point:
            self.acc = self.position - fly_to_point
        else:
            self.acc = VPoint(x_acc, y_acc)
        self.acc = speed/self.acc.length()*self.acc
        self.image = pygame.image.load('images/ninja/ninja3_enemy.png')
        self.size = 27
        self.image_size = VPoint(*self.image.get_rect().size)
        self.exist = True

    def move(self):
        self.position -= self.acc

    def draw(self, window, delta_view):
        window.blit(self.image, self.position.values_to_draw(delta_view))

    def is_visible(self, min_x, min_y, max_x, max_y):
        return min_x < self.position.get_x() < max_x and min_y < self.position.get_y() < max_y
