# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:56:45 2020

@author: polakiew
"""

import numpy
import pygame
from bullets_and_VPoint import VPoint

class Person():
    def __init__(self, window, size, starting_point):
        #size - dlugosc od glowy do brzucha
        self.window = window
        self.size = size
        self.head = starting_point
        self.headR = size / 7
        self.stomach = starting_point - VPoint(0,size)
        self.left_hand = starting_point - VPoint(size, size)
        self.left_elbow = starting_point - 0.5*VPoint(size,size)
        self.right_hand = starting_point - VPoint(-size, size)
        self.right_elbow = starting_point - 0.5*VPoint(-size, size)
        self.left_foot = self.stomach - VPoint(size, size)
        self.left_knee = self.stomach - 0.5*VPoint(size,size)
        self.right_foot = self.stomach - VPoint(-size, size)
        self.right_knee = self.stomach - 0.5*VPoint(-size, size)
        
    def draw(self):
        pass
    