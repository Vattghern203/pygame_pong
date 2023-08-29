import pygame
from scripts.settings import *
from scripts.scene import Scene
from scripts.menu import Menu
from scripts.gameOver import GameOver
from scripts.game import Game
from scripts.player import Player
from scripts.ball import Ball

class StartGame:

    def __init__(self):
        #padrão iniciar font, som e video
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.clock = pygame.time.Clock()
        
        self.target_fps = 60

        self.display = pygame.display.set_mode([WIDTH, HEIGHT])

        self.player1 = Player("assets/player1.png", 6, 110, 0)
        self.player2 = Player("assets/player2.png", 6, 1280, 0, False)
        self.ball = Ball("assets/ball.png", WIDTH / 2, HEIGHT / 2, 6, 6)

        self.scene = "menu"
        self.current_scene = Menu()
        self.current_scene.update()

    def run(self):
        while True:
            if self.scene == "menu" and self.current_scene.active==False:

                self.scene = "game"
                self.current_scene = Game()

                pygame.mixer.music.load("assets/piao.mp3")
                pygame.mixer.music.play(-1)

                self.current_scene.all_sprites.add(self.player1.sprite, self.player2.sprite, self.ball.sprite)

            elif self.scene == "game" and self.current_scene.active == False:

                self.scene = "gameover"
                self.current_scene = GameOver()

                self.current_scene.bg = "assets/china.png"

            elif self.scene == "gameover" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()


            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.mixer.music.stop()
                    pygame.quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_s:

                        self.player1.velocity = 6
                    
                    elif event.key == pygame.K_w:

                        self.player1.velocity = -6

                self.current_scene.events(event)

            self.player1.handle_bounds()
            self.player1.handle_velocity()
            self.player2.handle_bounds()
            self.player2.handle_NPC()
            self.player2.sprite.rect.y += self.player2.velocity

            self.ball.handle_colision(self.player1.sprite.rect, self.player2.sprite.rect)
            self.ball.handle_redirect()
            

            self.display.fill((0, 0, 0))

            self.current_scene.draw()
            self.current_scene.update()

            pygame.display.flip()

            self.clock.tick(self.target_fps)