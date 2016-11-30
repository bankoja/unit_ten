# James Bankole 11/22/16 unit 10
# This program creates a multi-colored brick pyramid.
import pygame


class Brick:
   """This class creates a brick that can be used in programs such as breakout and stacker."""
   def __init__(self, surface, brickHeight, brickWidth, color):
       self.surface = surface
       self.brickHeight = brickHeight
       self.brickWidth = brickWidth
       self.color = color


   def draw(self, x, y):
       """This function draws the brick in the position that the user inputs. The 0 fills in the bricks."""
       pygame.draw.rect(self.surface, self.color, (x, y, self.brickWidth, self.brickHeight), 0)