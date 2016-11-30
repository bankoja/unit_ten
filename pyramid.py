# James Bankole 11/22/16 unit 10
# This program creates a multi-colored brick pyramid.
import pygame, sys


from pygame.locals import *


import brick


pygame.init()


mainSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Brick Pyramid BOYYYYY")


ORANGE = (205, 133, 0)
GROD = (205, 155, 29)
GOLROD = (238, 180, 34)
GOLDD = (238, 201, 0)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)
numberOfBricks = 9


SPACES = 5


# Multiply spaces by number of bricks + 1
widthOfBrick = (mainSurface.get_width() - SPACES*10)/9


heightOfScreen = mainSurface.get_height()


xPos = SPACES
yPos = heightOfScreen - 25


listColors = [ORANGE, GROD, GOLROD, GOLDD, GOLD]


rowNumber = 0


# This loop creates the bricks for each row, changes row and color
for color in listColors:
   # This indents the first brick in each row.
   xPos = rowNumber * (widthOfBrick + SPACES)
   for x in range(numberOfBricks):
       pieONE = brick.Brick(mainSurface, 25, widthOfBrick, color)
       pieONE.draw(xPos, yPos)
       xPos += widthOfBrick + SPACES
   yPos -= 25 + SPACES
   numberOfBricks -= 2
   rowNumber += 1




pygame.display.update()
while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
