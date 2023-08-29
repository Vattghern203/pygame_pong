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

    def handle_NPC(self, window_height=720):

        if (self.sprite.rect.y <= 0):

            self.sprite.rect.y = 0
            
            self.velocity = 6
            self.sprite.rect.y -= 10


        elif (self.sprite.rect.y >= (window_height - self.heigth)):

            self.sprite.rect.y = window_height - self.heigth

            self.velocity = -6
            self.sprite.rect.y += 10

        self.sprite.rect.y += self.velocity