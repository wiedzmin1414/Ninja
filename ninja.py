from bullets_and_VPoint import *
import math
import pygame


class Ninja:
    def __init__(self, x, y):
        self.position = VPoint(x, y)
        self.last_position = VPoint(x+1, y-1)
        self.speed = VPoint(0, 0)
        ### hanging mode
        self.is_hanging = False
        self.hanging_point = None
        self.R = None
        self.alfa = None
        self.speed_alfa = None
        self.acc_alfa = None

    def draw(self, window):
        x = self.position.get_x()
        y = self.position.get_y()
        print(x, y)
        pygame.draw.rect(window, (255, 0, 0), (x, y, 10, 10))
        if self.is_hanging:
            pygame.draw.line(window, (255, 0, 0), self.position.values(), self.hanging_point.values())

    def move(self, gravity=VPoint(0,5)):
        if self.is_hanging:
            self.alfa += self.acc_alfa
            self.last_position = self.position
            self.position = self.calculate_point_from_angle()
        else:
            self.position += self.speed
            self.speed -= gravity
            
    def calculate_point_from_angle(self):
        dx = self.R * math.sin(self.alfa)
        dy = self.R * math.cos(self.alfa)
        dp = VPoint(dx, dy)
        return self.hanging_point - dp

    def establish_hang(self, x, y):
        self.hanging_point = VPoint(x, y)
        self.speed_alfa = VPoint(0, 0)
        self.acc_alfa
        self.is_hanging = True
        self.calculate_hang()

    def calculate_hang(self):
        delta = self.position - self.hanging_point
        self.R = delta.length()
        delta_x = self.position.sub_x(self.hanging_point)
        sinus_alfa = delta_x / self.R
        self.alfa = math.asin(sinus_alfa)
        self.acc_alfa = self.alfa / 10

    def stop_hanging(self):
        self.acc = VPoint(0,0)
        self.speed = self.position - self.last_position


