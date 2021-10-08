from pygame import *
from pygame.sprite import Sprite

class HeroeDrawer(Sprite):
  instance = None

  def __new__(cls, *arg, **kargs):
    if cls.instance is None:
      cls.instance = object.__new__(cls, *arg, **kargs)
    return cls.instance

  def __init__(self):
    Sprite.__init__(self)
    self.orientation = 0
    self.movement_speed = 10
    self.cont = 0
    self.points = 0

  def set_initial_location(self, pos):
    self.rect.x = pos[0]
    self.rect.y = pos[1]

  def is_collided_with(self, sprite):
    if self.rect.colliderect(sprite.rect):
      self.points -= 10
    else:
      pass

  def reset_heroe(self):
    self.points = 0

  def set_sprites(self, sprites):
    self.spr_images = sprites
    self.image = self.spr_images[self.orientation][0]
    self.rect = self.image.get_rect()

  def update(self):
    pressed_key = key.get_pressed()
    if pressed_key[K_LEFT]:
      self.rect.left -= self.movement_speed
      self.orientation = 1
    if pressed_key[K_RIGHT]:
      self.rect.left += self.movement_speed
      self.orientation = 0
    if pressed_key[K_DOWN]:
      self.rect.top += self.movement_speed
      self.orientation = 2
    if pressed_key[K_UP]:
      self.rect.top -= self.movement_speed
      self.orientation = 3
    
    if pressed_key[K_LEFT] or pressed_key[K_RIGHT] or pressed_key[K_UP] or pressed_key[K_DOWN]:
      self.image = self.spr_images[self.orientation][self.cont]
      self.cont += 1
      self.cont %= 3
      self.points += 1

      self.rect.top %= 600 - 60
      self.rect.left %= 800

  def draw(self, screen):
    text_font = font.Font(None, 20)
    text = text_font.render("puntos: " + str(self.points), 1, (20,20,50))
    screen.blit(self.image, self.rect)
    screen.blit(text, (self.rect.x - 20, self.rect.y -15))
