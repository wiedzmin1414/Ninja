# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:35:25 2020

@author: polakiew
"""
from VPoint import VPoint
import pygame

class Bullet:
    def __init__(self, start_position, mouse_position, speed= 12, color= (0, 255, 0)):
        position_x = start_position.get_x()
        position_y = start_position.get_y()
        self.position = VPoint(position_x, position_y)
        mouse_position = VPoint(mouse_position[0], mouse_position[1])
        direction = mouse_position -  self.position
        self.speed = speed / direction.length() * direction 
        self.color = color

    def move(self, gravity= VPoint(0,0)):
        self.position += self.speed
        self.speed -= gravity
        
    def draw(self, window, color = None):
        if not color:
            color = self.color
        pygame.draw.rect(window, color, (*self.position.values(), 3, 3))
        
    def is_visible(self, min_x, min_y, max_x, max_y):
        return (self.position.get_x() > min_x and self.position.get_x() < max_x
            and self.position.get_y() > min_y and self.position.get_y() < max_y)
        
        
class Link_shuriken(Bullet):
    def draw(self, window):
        pygame.draw.rect(window, (128,128,128), (*self.position.values(), 5, 5))
        
    def above_ceiling(self, ceiling_height):
        return 0 <= self.position.get_y() <= ceiling_height
    