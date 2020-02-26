# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:28:34 2020

@author: polakiew
"""

import numpy as np
import pygame


class Block():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def draw(self, window, colour, heigh):
        pygame.draw.rect(window, colour, (self.start, 0, self.end - self.start, heigh), 1)

    def return_end(self):
        return self.end
    
    def __str__(self):
        return str([self.start, self.end])
    
    def __contains__(self, number):
        return self.start <= number <= self.end

class Ceiling():
    def __init__(self, max_x, blank_size, block_size, colour, height):
        self.max_x = max_x #  width of window
        self.blank_size = blank_size
        self.block_size = block_size
        self.colour = colour
        self.block_list = [Block(0, np.random.randint(self.blank_size) + 100)]
        self.generate()
        self.height = height
        
    def generate(self):
        position = self.block_list[-1].return_end()
        end = position + 4*self.max_x #  where I want to end generate
        print(position, end)
        while position < end:
            print(position)
            actual_blank_size = np.random.randint(self.blank_size) + 100
            actual_block_size = np.random.randint(self.block_size) + 100
            start_block = position + actual_blank_size
            position = start_block + actual_block_size
            block = Block(start_block, position)
            self.block_list.append(block)
            
    def draw(self, window):
        for block in self.block_list:
            block.draw(window, self.colour, self.height)
            
    def __str__(self):
        return str(self.block_list)

    def __contains__(self, number):
        for block in self.block_list:
            if number in block:
                return True
        return False


if __name__ == "__main__":
    w = Ceiling(400, 100, 100, (2,255,4))
    print(w)
