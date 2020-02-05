import pygame
import game

pygame.init()
# window
x_length = 1600
y_length = 900
window = pygame.display.set_mode((x_length, y_length))
pygame.display.set_caption("Ninja Lukas")
        
w = game.Game(x_length, y_length)
w.play(window)
pygame.quit()
print("Thanks for game!")
