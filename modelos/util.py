from pygame import image

def load_image_sprite(nombre):
  imagen = image.load(nombre)
  return imagen #.convert_alpha()
