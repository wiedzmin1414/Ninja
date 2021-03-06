# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:35:25 2020

@author: polakiew
"""
from VPoint import VPoint
import pygame


class Bullet:
    def __init__(self, start_position, mouse_position, speed=12, have_been_checked=False):
        position_x = start_position.get_x()
        position_y = start_position.get_y()
        self.position = VPoint(position_x, position_y)
        mouse_position = VPoint(mouse_position[0], mouse_position[1])
        direction = mouse_position - self.position
        self.speed = speed / direction.length() * direction
        self.angle = 0
        self.angle_speed = 15
        self.have_been_checked = have_been_checked
        self.size = 5
        self.exist = True

    def move(self, gravity= VPoint(0,0)):
        self.position += self.speed
        self.speed -= gravity
        self.angle += self.angle_speed
        
    def draw(self, window, image, size, delta_view):
        rotated_image = pygame.transform.rotate(image, self.angle)
        window.blit(rotated_image, (self.position - VPoint(size, size)).values_to_draw(delta_view))
        
    def is_visible(self, min_x, min_y, max_x, max_y):
        return min_x < self.position.get_x() < max_x and min_y < self.position.get_y() < max_y

    def middle(self, shuriken_size=10):
        return self.position + 0.5*VPoint(shuriken_size, shuriken_size)
        
        
class Link_shuriken(Bullet):
    def above_ceiling(self, ceiling_height):
        return self.position.get_y() <= ceiling_height
