class Bullet:
    def __init__(self, x, y, speed_x, speed_y, colors=(0, 255, 0)):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.colors = colors

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y


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
        


if __name__ == "__main__":
    z = VPoint(2, 3)
    w = VPoint(10, 20)
    print(w, z, w+z, w-z)
    print(w.sub_x(z), w.sub_y(z), w.length(), w.get_y())
