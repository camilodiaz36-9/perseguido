import pygame
from pygame.locals import *
import sys
from modelos.builder import ConcreteBuilderHero, ConcreteBuilderZombie, Director
from modelos.util import load_image_sprite
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ICON_SIZE = 32

def game():
  pygame.init()
  
  director = Director()
  
  builderHeroe = ConcreteBuilderHero()
  director.builder = builderHeroe
  director.build_heroe()
  heroe = builderHeroe.product
  heroe.create_drawer()
  heroeDrawer = heroe.get_drawer()

  builderZombie1 = ConcreteBuilderZombie()
  director.builder = builderZombie1
  director.build_zombie()
  zombie1 = builderZombie1.product
  zombie1.create_drawer()
  zombie1Drawer = zombie1.get_drawer()

  builderZombie2 = ConcreteBuilderZombie()
  director.builder = builderZombie2
  director.build_zombie()
  zombie2 = builderZombie2.product
  zombie2.create_drawer()
  zombie2Drawer = zombie2.get_drawer()

  builderZombie3 = ConcreteBuilderZombie()
  director.builder = builderZombie3
  director.build_zombie()
  zombie3 = builderZombie3.product
  zombie3.create_drawer()
  zombie3Drawer = zombie3.get_drawer()

  img_start = load_image_sprite('imagenes/inicio.jpg')
  img_background = load_image_sprite('imagenes/fondo.jpg')
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  pygame.mouse.set_visible(False)

  is_playing = False
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_SPACE]:
      heroeDrawer.set_initial_location((200,200))
      zombie1Drawer.set_initial_location((randint(0, 800),randint(0, 600)))
      zombie2Drawer.set_initial_location((randint(0, 800),randint(0, 600)))
      zombie3Drawer.set_initial_location((randint(0, 800),randint(0, 600)))
      is_playing = True
    if is_playing:
      screen.blit(img_background, (0, 0))
      heroeDrawer.update()
      zombie1Drawer.update(heroeDrawer.rect.x, heroeDrawer.rect.y)
      zombie2Drawer.update(heroeDrawer.rect.x, heroeDrawer.rect.y)
      zombie3Drawer.update(heroeDrawer.rect.x, heroeDrawer.rect.y)
      heroeDrawer.draw(screen)
      zombie1Drawer.draw(screen)
      zombie2Drawer.draw(screen)
      zombie3Drawer.draw(screen)
      
      heroeDrawer.is_collided_with(zombie1Drawer)
      heroeDrawer.is_collided_with(zombie2Drawer)
      heroeDrawer.is_collided_with(zombie3Drawer)

      if heroeDrawer.points <= -1:
        is_playing = False
        heroeDrawer.reset_heroe()
    else:
      screen.blit(img_start, (0, 0))
    pygame.display.update()
    pygame.time.delay(10)

if __name__ == '__main__':
  game()