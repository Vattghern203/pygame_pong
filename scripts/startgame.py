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

        self.player1 = Player("assets/player1.png", 1, 110, 0)
        self.player2 = Player("assets/player2.png", 1, 1280, 0, False)

        print(self.player1.sprite.rect)

        self.scene = "menu"
        self.current_scene = Menu()
        self.current_scene.update()

    def run(self):
        while True:
            if self.scene == "menu" and self.current_scene.active==False:

                self.scene = "game"
                self.current_scene = Game()

                self.current_scene.all_sprites.add(self.player1.sprite, self.player2.sprite)

            elif self.scene == "game" and self.current_scene.active == False:

                self.scene = "gameover"
                self.current_scene = GameOver()

            elif self.scene == "gameover" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

            self.player1.handle_velocity()
            self.player1.handle_bounds()
            self.player2.handle_bounds()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_s:

                        self.player1.velocity = 6
                        self.player1.sprite.rect.y += 10
                    
                    elif event.key == pygame.K_w:

                        self.player1.velocity = -6
                        self.player1.sprite.rect.y -= 10


                if event.type == pygame.QUIT:
                    pygame.quit()
                self.current_scene.events(event)

            self.display.fill((0, 0, 0))

            self.current_scene.draw()
            self.current_scene.update()

            pygame.display.flip()