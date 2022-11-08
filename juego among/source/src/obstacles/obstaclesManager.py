import pygame
import random

from utils.Constantes import ENEMIE, ENEMIE1, ENEMIE2, ENEMIE3, ENEMIE4
from obstacles.impostor1 import Impostor1
from obstacles.impostor2 import Impostor2
from obstacles.impostor3 import Impostor3
from obstacles.impostor4 import Impostor4
from obstacles.impostor5nave import Impostor5


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update(self, game):

        if game.player.trip_rect.colliderect(game.crew_jail):
            pygame.time.delay(500)
            game.win = True
            game.win_count += 1
            game.playing = False
        if game.player.trip_rect.collidepoint(game.portal.portal_right_rect.centerx, 570):
            game.player.teleport()
        if game.player.trip_rect.collidepoint(game.portal.portal_left_rect.centerx, 205):
            game.player.teleport_down()

        if len(self.obstacles_list) == 0 or len(self.obstacles_list) <= 4:
            impostor1 = Impostor1(ENEMIE)
            impostor2 = Impostor2(ENEMIE1)
            impostor3 = Impostor3(ENEMIE2)
            impostor4 = Impostor4(ENEMIE3)
            impostor5 = Impostor5(ENEMIE4)
            obstacle_list = [impostor5, impostor4, impostor3, impostor2, impostor1]
            obstacle_random_list = random.sample(obstacle_list, 5)
            obstacle_random_list[0].rect.x = 1000
            obstacle_random_list[1].rect.x = 1300
            obstacle_random_list[2].rect.x = 1600
            obstacle_random_list[3].rect.x = 1900
            obstacle_random_list[4].rect.x = 2100
            obstacle_with_position = [obstacle_random_list[0],
                                      obstacle_random_list[1],
                                      obstacle_random_list[2],
                                      obstacle_random_list[3],
                                      obstacle_random_list[4]]
            self.obstacles_list.extend(obstacle_with_position)

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if obstacle.rect.collidepoint(game.portal.portal_left_rect.centerx, 120):
                obstacle.teleport_down_air()
            if obstacle.rect.collidepoint(game.portal.portal_left_rect.centerx, 220):
                obstacle.teleport_down_ground()
            if game.player.trip_rect.collidepoint(obstacle.rect.center):
                die = pygame.mixer.Sound('../sounds/muerte.mp3')
                die.play()
                pygame.time.delay(100)
                game.death_count += 1
                game.player.game_over = True
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            if obstacle.rect.x < 950:
                obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []
