import pygame

class Entity:

    def __init__(self, x:float, y:float, width:float, height:float) -> None:
        
        self.rect = pygame.Rect(x, y, width, height)