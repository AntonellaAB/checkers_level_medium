#All constant variables
import pygame
WIDTH, HEIGHT = 700, 700
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#rgb 
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

#crown size
#CROWN = pygame.image.load("assets/crown.png")
#CROWN = pygame.transform.smoothscale(CROWN, (45, 25))
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (35, 25))

#Nos quedamos en 7:17:00