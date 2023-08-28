import pygame

from scripts.settings import HEIGHT

from scripts.obj import Obj

class Entity:

    def __init__(self, img:str, posX:float, posY:float) -> None:
        
        self.sprite = Obj(img=img, right=posX, top=posY)
        self.heigth = 150

    def handle_bounds(self):

        if (self.sprite.rect.y <= 0):

            self.sprite.rect.y = 0

        elif (self.sprite.rect.y > (HEIGHT - self.heigth)):

            self.sprite.rect.y = HEIGHT - self.heigth

        