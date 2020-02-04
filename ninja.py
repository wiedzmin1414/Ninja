from bullets_and_VPoint import VPoint
import math
import pygame
import numpy as np


class Ninja:
    def __init__(self, x, y):
        self.position = VPoint(x, y)
        self.last_position = VPoint(x+1, y-1)
        self.speed = VPoint(0, 0)
        self.acc = VPoint(0,0)
        ### hanging mode
        self.is_hanging = False
        self.hanging_point = None
        self.R = None
        self.alfa = 0
        self.alfa_speed = None
        self.alfa_acc = 0.001

    def calculate_linear_speed(self):
        return self.position - self.last_position

    def draw(self, window):
        x = self.position.get_x()
        y = self.position.get_y()
        print(x, y)
        pygame.draw.rect(window, (255, 0, 0), (x, y, 10, 10))
        if self.is_hanging:
            pygame.draw.line(window, (255, 0, 0), self.position.values(), self.hanging_point.values())

    def move(self, gravity=VPoint(0, -0.3)):
        if self.is_hanging:
            print(self.alfa)
            self.alfa_speed += self.alfa_acc
            self.alfa += self.alfa_speed
            self.last_position = self.position
            self.position = self.calculate_point_from_angle(self.alfa)
            if self.position.get_x() < self.hanging_point.get_x() and self.alfa_acc < 0:
                self.alfa_acc *= -1
            if self.position.get_x() > self.hanging_point.get_x() and self.alfa_acc > 0:
                self.alfa_acc *= -1

        else:
            self.position += self.speed
            self.speed -= gravity
            
    def calculate_point_from_angle(self, alfa):
        dx = self.R * math.sin(alfa)
        dy = self.R * math.cos(alfa)
        dp = VPoint(dx, dy)
        return self.hanging_point - dp

    def establish_hang(self, x, y):
        self.hanging_point = VPoint(x, y)
        self.alfa_speed = VPoint(0, 0)
        self.is_hanging = True
        self.calculate_hang()

    def calculate_hang(self):
        delta = self.position - self.hanging_point
        self.R = delta.length()
        #delta_x = self.position.sub_x(self.hanging_point)
        #sinus_alfa = delta_x / self.R
        #self.alfa = math.asin(sinus_alfa)
       # if self.position.get_x() < self.hanging_point.get_x():
       #     self.alfa = 2
        self.alfa_speed = 0
        self.alfa_acc = 0.001
        min_error = 100000
        for alfa in np.arange(0, 2*math.pi, math.pi/256):
            position = self.calculate_point_from_angle(alfa)
            error_vector = position - self.position
            current_error = error_vector.length()
            if current_error < min_error:
                best_alfa = alfa
                min_error = current_error
                #print(min_error)
        self.alfa = best_alfa

    def stop_hanging(self):
        self.speed = 1.3*(self.position - self.last_position)
        self.is_hanging = False
        
    def reset(self):
        self.position = VPoint(700,500)
        self.speed = VPoint(0,0)
        self.is_hanging = False
        
    def jump(self, distance = VPoint(0,-2)):
        self.speed += distance


