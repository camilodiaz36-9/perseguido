from abc import ABC, abstractmethod
from .util import load_image_sprite

class Abajo(ABC):
  @abstractmethod
  def get_sprites(self):
    pass

class Arriba(ABC):
  @abstractmethod
  def get_sprites(self):
    pass

class Izquierda(ABC):
  @abstractmethod
  def get_sprites(self):
    pass

class Derecha(ABC):
  @abstractmethod
  def get_sprites(self):
    pass

class AbajoHumano(Abajo):
  def get_sprites(self):
    return [load_image_sprite('imagenes/F1.png'),
            load_image_sprite('imagenes/F2.png'),
            load_image_sprite('imagenes/F3.png')]

class ArribaHumano(Arriba):
  def get_sprites(self):
    return [load_image_sprite('imagenes/B1.png'),
            load_image_sprite('imagenes/B2.png'),
            load_image_sprite('imagenes/B3.png')]

class IzquierdaHumano(Izquierda):
  def get_sprites(self):
    return [load_image_sprite('imagenes/I1.png'),
            load_image_sprite('imagenes/I2.png'),
            load_image_sprite('imagenes/I3.png')]

class DerechaHumano(Derecha):
  def get_sprites(self):
    return [load_image_sprite('imagenes/D1.png'),
            load_image_sprite('imagenes/D2.png'),
            load_image_sprite('imagenes/D3.png')]

class AbajoZombie(Abajo):
  def get_sprites(self):
    return [load_image_sprite('imagenes/ZF1.png'),
            load_image_sprite('imagenes/ZF2.png'),
            load_image_sprite('imagenes/ZF3.png')]

class ArribaZombie(Arriba):
  def get_sprites(self):
    return [load_image_sprite('imagenes/ZB1.png'),
            load_image_sprite('imagenes/ZB2.png'),
            load_image_sprite('imagenes/ZB3.png')]

class IzquierdaZombie(Izquierda):
  def get_sprites(self):
    return [load_image_sprite('imagenes/ZI1.png'),
            load_image_sprite('imagenes/ZI2.png'),
            load_image_sprite('imagenes/ZI3.png')]

class DerechaZombie(Derecha):
  def get_sprites(self):
    return [load_image_sprite('imagenes/ZD1.png'),
            load_image_sprite('imagenes/ZD2.png'),
            load_image_sprite('imagenes/ZD3.png')]