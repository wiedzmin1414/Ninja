import pygame

pygame.init()
# window
x_length = 1600
y_length = 900
window = pygame.display.set_mode((x_length, y_length))
pygame.display.set_caption("Ninja Lukas")
pygame.draw.rect(window, (255, 0, 0), (10, 10, 100, 100))
while True:
    pass
