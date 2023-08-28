from scripts.entity import Entity

class Player(Entity):

    def __init__(self, img:str, velocity:float, posX:float, posY:float, controlled: bool=True) -> None:
        super().__init__(img, posX, posY)

        self.velocity = velocity
        self.posX = posX
        self.posY = posY
        self.controlled = controlled

    def handle_velocity(self):

        self.sprite.rect.y += self.velocity