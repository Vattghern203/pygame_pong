from scripts.entity import Entity

from pygame.mixer import Sound

class Ball(Entity):

    def __init__(self, img: str, posX: float, posY: float, dir_x:int=6, dir_y:int=6) -> None:
        super().__init__(img, posX, posY)

        self.dir_x = dir_x
        self.dir_y = dir_y

    def handle_redirect(self):

        if self.sprite.rect.y <= 0:

            self.dir_y *= -1

        elif self.sprite.rect.y >= 720 - 15:

            self.dir_y *= -1

        if self.sprite.rect.x <= 0:

            self.dir_x *= -1

        elif self.sprite.rect.x >= 1280 - 15:

            self.sprite.rect.x = 600
            self.dir_x *= -1

        self.sprite.rect.x += self.dir_x
        self.sprite.rect.y += self.dir_y

    def handle_colision(self, first_obj, second_obj):

        if self.sprite.rect.colliderect(first_obj) or self.sprite.rect.colliderect(second_obj):

            hit = Sound('assets/oof.wav')
            hit.play()

            self.dir_x