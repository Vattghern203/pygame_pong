import pygame
from scripts.settings import *
from scripts.scene import Scene
from scripts.menu import Menu
from scripts.gameOver import GameOver
from scripts.game import Game
from scripts.player import Player

class StartGame:

    def __init__(self):
        #padrão iniciar font, som e video
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.display = pygame.display.set_mode([WIDTH, HEIGHT])

        self.player1 = Player(0, 100, 30, 150, 1, "assets/player1.png")
        self.player2 = Player(1000, 100, 30, 150, 1, "assets/player2.png")

        print(self.player1.rect)
        print(self.player2.rect)


        self.scene = "menu"
        self.current_scene = Menu()
        self.current_scene.update()

    def run(self):
        while True:
            if self.scene == "menu" and self.current_scene.active==False:

                self.scene = "game"
                self.current_scene = Game()

                self.current_scene.all_sprites.add(self.player1.sprite)
                self.current_scene.all_sprites.add(self.player2.sprite)

                self.current_scene.update()

            elif self.scene == "game" and self.current_scene.active == False:

                self.scene = "gameover"
                self.current_scene = GameOver()

            elif self.scene == "gameover" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.current_scene.events(event)

            self.display.fill((0, 0, 0))

            self.current_scene.draw()
            self.current_scene.update()
            pygame.display.flip()