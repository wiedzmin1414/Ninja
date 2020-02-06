import pygame

class VPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return VPoint(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return VPoint(self.x - other.x, self.y - other.y)
    
    def __rmul__(self, number):
        return VPoint(number*self.x, number*self.y)

    def __str__(self):
        return str([self.x, self.y])

    def length(self):
        return (self.x**2 + self.y**2)**0.5

    def add_x(self, other):
        return self.x + other.x

    def sub_x(self, other):
        return self.x - other.x

    def add_y(self, other):
        return self.y + other.y

    def sub_y(self, other):
        return self.y - other.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def values(self):
        return self.x, self.y

    def add_point_on_screen(self, other):
        self.x -= other.x
        self.y += other.y
        
    def sub_point_on_screen(self, other):
        self.x += other.x
        self.y -= other.y

        
class Bullet:
    def __init__(self, start_position, mouse_position, speed= 4, color= (0, 255, 0)):
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
   

if __name__ == "__main__":
    z = VPoint(2, 3)
    w = VPoint(10, 20)
    print(w, z, w+z, w-z)
    print(w.sub_x(z), w.sub_y(z), w.length(), w.get_y())
    print("####### Bullet tests ##########")
    position = VPoint(2,3)
    mouse_position = (3,4)
    bullet = Bullet(position, mouse_position)
    edges = 0, 0, 800, 1200
    print(bullet.position, bullet.speed, bullet.is_visible(*edges))
    bullet.move()
    print(bullet.position)
    