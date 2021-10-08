from pygame import *
from pygame.sprite import Sprite
from random import randint

class ZombieDrawer(Sprite):
  instance = None

  def __init__(self):
    Sprite.__init__(self)
    self.orientation = 0
    self.movement_speed = randint(1,3)
    self.cont = 0

  def set_initial_location(self, pos):
    self.rect.x = pos[0]
    self.rect.y = pos[1]

  def set_sprites(self, sprites):
    self.spr_images = sprites
    self.image = self.spr_images[self.orientation][0]
    self.rect = self.image.get_rect()

  def update(self, xAlpha, yAlpha):
    xDelta = xAlpha - self.rect.x
    yDelta = yAlpha - self.rect.y

    moveLeft = xDelta<=(self.movement_speed)
    moveRight = xDelta>(self.movement_speed)
    moveDown = yDelta>(self.movement_speed)
    moveUp = yDelta<=(self.movement_speed)
    
    if moveLeft:
      self.rect.left -= self.movement_speed
      self.orientation = 1
    if moveRight:
      self.rect.left += self.movement_speed
      self.orientation = 0
    if moveDown:
      self.rect.top += self.movement_speed
      self.orientation = 2
    if moveUp:
      self.rect.top -= self.movement_speed
      self.orientation = 3
    
    if moveLeft or moveRight or moveUp or moveDown:
      self.image = self.spr_images[self.orientation][self.cont]
      self.cont += 1
      self.cont %= 3

      self.rect.top %= 600-60
      self.rect.left %= 800
    
  def draw(self, screen):
    screen.blit(self.image, self.rect)
