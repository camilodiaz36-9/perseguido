from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
import uuid

from modelos.enemigo import ZombieDrawer
from modelos.heroe import HeroeDrawer
from modelos.productos import AbajoHumano, AbajoZombie, ArribaHumano, ArribaZombie, DerechaHumano, DerechaZombie, IzquierdaHumano, IzquierdaZombie

class Builder(ABC):
    
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def create_left(self) -> None:
        pass

    @abstractmethod
    def create_right(self) -> None:
        pass

    @abstractmethod
    def create_up(self) -> None:
        pass

    @abstractmethod
    def create_down(self) -> None:
        pass

class Hero():
    def __init__(self) -> None:
        self.parts = []
        self.id = str(uuid.uuid4())
        self.drawer = HeroeDrawer()

    def add(self, part: Any) -> None:
        self.parts.append(part)
    
    def create_drawer(self) -> HeroeDrawer:
        self.drawer.set_sprites(self.parts)

    def get_drawer(self):
        return self.drawer
    
class Zombie():
    def __init__(self) -> None:
        self.parts = []
        self.id = str(uuid.uuid4())
        self.drawer = ZombieDrawer()

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def create_drawer(self) -> ZombieDrawer:
        self.drawer.set_sprites(self.parts)
    
    def get_drawer(self):
        return self.drawer

class ConcreteBuilderHero(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Hero()

    @property
    def product(self) -> Hero:
        product = self._product
        self.reset()
        return product

    def create_left(self) -> None:
        left_part_hero = IzquierdaHumano()
        self._product.add(left_part_hero.get_sprites())

    def create_right(self) -> None:
        right_part_hero = DerechaHumano()
        self._product.add(right_part_hero.get_sprites())

    def create_up(self) -> None:
        up_part_hero = ArribaHumano()
        self._product.add(up_part_hero.get_sprites())

    def create_down(self) -> None:
        down_part_hero = AbajoHumano()
        self._product.add(down_part_hero.get_sprites())

class ConcreteBuilderZombie(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Zombie()

    @property
    def product(self) -> Zombie:
        
        product = self._product
        self.reset()
        return product

    def create_left(self) -> None:
        left_part_zombie = IzquierdaZombie()
        self._product.add(left_part_zombie.get_sprites())

    def create_right(self) -> None:
        right_part_zombie = DerechaZombie()
        self._product.add(right_part_zombie.get_sprites())

    def create_up(self) -> None:
        up_part_zombie = ArribaZombie()
        self._product.add(up_part_zombie.get_sprites())

    def create_down(self) -> None:
        down_part_zombie = AbajoZombie()
        self._product.add(down_part_zombie.get_sprites())

class Director:
    
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_heroe(self) -> None:
        self.builder.create_left()
        self.builder.create_right()
        self.builder.create_up()
        self.builder.create_down()

    def build_zombie(self) -> None:
        self.builder.create_left()
        self.builder.create_right()
        self.builder.create_up()
        self.builder.create_down()