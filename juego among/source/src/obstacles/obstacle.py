import pygame
from pygame.sprite import Sprite
from utils.Constantes import SCREEN_WIDTH


class Obstacle(Sprite):

    def __init__(self, image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles_list):
        self.rect.x -= game_speed/2
        if self.rect.x < -self.rect.width:
            obstacles_list.pop(0)

    def teleport_down_ground(self):
        teleport = pygame.mixer.Sound('sounds/teleport.mp3')
        teleport.play()
        self.rect.x = 950
        self.rect.y = 565

    def teleport_down_air(self):
        teleport = pygame.mixer.Sound('sounds/teleport.mp3')
        teleport.play()
        self.rect.x = 950
        self.rect.y = 450

    def draw(self, screen):
        screen.blit(self.image[self.obstacle_type], self.rect)