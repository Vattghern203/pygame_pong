import pygame

from scripts.entity import Entity
from scripts.obj import Obj

class Player(Entity):

    def __init__(self, x: float, y: float, width: float, height: float, velocity: float, img:str) -> None:
        super().__init__(x, y, width, height)

        self.velocity = velocity
        self.sprite = Obj(img=img)

    def move(self, distance:float):

        self.x += distance

    def change_velocity(self, value:float):

        self.velocity += value