from VPoint import VPoint
#from bullets import Bullet, Link_shuriken
import math
import pygame
import numpy as np


class Ninja:
    def __init__(self, x, y, alfa_acc = 0.001, shot_pause = 60, link_hand_delta = VPoint(4,11)):
        ### normal move (without hanging)
        self.position = VPoint(x, y)
        self.last_position = None
        self.speed = VPoint(0, 0)
        self.acc = VPoint(0,0)
        self.jump_available = True 
        ### hanging mode
        self.is_hanging = False
        self.hanging_point = None
        self.R = 0
        self.alfa = None
        self.alfa_speed = None
        self.alfa_acc = alfa_acc
        self.image = pygame.image.load('images/ninja/ninja3.png')
        self.image_throw = pygame.image.load('images/ninja/ninja3_throw.png')
        self.image_hanging = pygame.image.load('images/ninja/ninja3_hanging.png')
        self.image_hanging_throw = pygame.image.load('images/ninja/ninja3_hanging_throw.png')
        self.shuriken = None
        self.shot_counter = 0
        self.shot_pause = shot_pause
        self.link_hand_delta = link_hand_delta

    def link_hand(self):
        return self.position + self.link_hand_delta

    def armed_hand(self):
        return self.position + VPoint(46, 32)

    def shot(self):
        self.shot_counter = self.shot_pause

    def shot_count(self):
        if self.shot_counter:
            self.shot_counter -= 1

    def is_shot_available(self):
        return not self.shot_counter

    def calculate_linear_speed(self):
        return self.position - self.last_position

    def draw(self, window, shuriken_image, shuriken_size):
        #print(x, y)
        #pygame.draw.rect(window, (255, 0, 0), (x, y, 10, 10))
        if self.shuriken:
            if self.shot_counter > self.shot_pause - 5:
                window.blit(self.image_hanging_throw, self.position.values())
            else:
                window.blit(self.image_hanging, self.position.values())
            pygame.draw.line(window, (255, 0, 0), self.link_hand().values(), self.shuriken.position.values())
            self.shuriken.draw(window, shuriken_image, shuriken_size)
        else:
            if self.shot_counter > self.shot_pause - 5:
                window.blit(self.image_throw, self.position.values())
            else:
                window.blit(self.image, self.position.values())

    def move(self, gravity=VPoint(0, -0.3)):
        if self.is_hanging:
            #print(self.alfa)
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
        #print(self.position.values())
        if self.shuriken and not self.is_hanging:
            self.shuriken.move()
        self.shot_count()

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
        #print("STOP hanging")
        self.speed = self.position - self.last_position
        self.acc = VPoint(0,0)
        self.is_hanging = False
        self.jump_available = True
        self.shuriken = None
        
    def reset(self):
        self.position = VPoint(100,500)
        self.speed = VPoint(0,0)
        self.acc = VPoint(0,0)
        self.is_hanging = False
        self.jump_available = True
        
    def jump(self, distance = VPoint(0,-10)):
        if self.jump_available:
            self.speed.y = 0
            self.acc.y = 0
            self.speed += distance
            self.jump_available = False
        
    def shorten_link(self, value=3):
            self.R -= value
            self.R = max(0, self.R)
            if not self.R:
                self.alfa_acc = 0
                self.alfa_speed = 0
                self.alfa = math.pi
    
    def extend_link(self, value = 5):
        self.R += value
