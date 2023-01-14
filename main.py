# Fabien Thich
# December 21, 2022

import pygame
import random

class Rectangle():
  def __init__(self):
    self.x = random.randint(0, 700)
    self.y = random.randint(0, 500)
    self.width = random.randint(20, 70)
    self.height = random.randint(20, 70)
    self.change_x = random.randint(-3, 3)
    self.change_y = random.randint(-3, 3)
    self.colour_r = random.randint(0,225)
    self.colour_g = random.randint(0,225)
    self.colour_b = random.randint(0,225)
    self.colour = (self.colour_r, self.colour_g, self.colour_b)

  def draw(self):
    pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height])

  def move(self):
    self.x += self.change_x
    self.y += self.change_y

class Ellipse(Rectangle):
  def draw(self):
    pygame.draw.ellipse(screen, self.colour, [self.x, self.y, self.width, self.height])
    
my_list = []

for i in range(50):
  my_rectangle = Rectangle()
  my_list.append(my_rectangle)

for i in range(50):
  my_ellipse = Ellipse()
  my_list.append(my_ellipse)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
  
    # my_object.draw()
    for item in my_list:
      item.draw()
      
    # my_object.move()
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
