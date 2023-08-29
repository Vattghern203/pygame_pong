import pygame

from scripts.settings import HEIGHT

from scripts.obj import Obj

class Entity:

    def __init__(self, img:str, posX:float, posY:float) -> None:
        
        self.sprite = Obj(img=img, right=posX, top=posY)
        self.heigth = 150

    def handle_bounds(self, window_height:float=HEIGHT):

        if (self.sprite.rect.y <= 0):

            self.sprite.rect.y = 0

        elif (self.sprite.rect.y >= (window_height - self.heigth)):

            self.sprite.rect.y = window_height - self.heigth