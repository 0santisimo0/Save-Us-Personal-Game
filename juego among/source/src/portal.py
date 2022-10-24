from utils.Constantes import PORTAL_LEFT, PORTAL_RIGHT, ENEMIES_PORTAL
from pygame.sprite import Sprite


class Portal(Sprite):
    def __init__(self):
        self.image_right = PORTAL_RIGHT[0]
        self.image_left = PORTAL_LEFT[0]
        self.image_enemie = ENEMIES_PORTAL[0]
        self.portal_left_rect = self.image_left.get_rect()
        self.portal_right_rect = self.image_right.get_rect()
        self.portal_enemie_rect = self.image_enemie.get_rect()
        self.portal_index = 0

    def update(self):
        if self.portal_index >= 48:
            self.portal_index = 0

        self.image_right = PORTAL_RIGHT[self.portal_index // 8]
        self.image_left = PORTAL_LEFT[self.portal_index // 8]
        self.image_enemie = ENEMIES_PORTAL[self.portal_index // 8]
        self.portal_left_rect.midbottom = (190, 290)
        self.portal_right_rect.midbottom = (1030, 650)
        self.portal_enemie_rect.midbottom = (1020, 290)
        self.portal_index += 1

    def draw(self, screen):
        screen.blit(self.image_left, self.portal_left_rect)
        screen.blit(self.image_right, self.portal_right_rect)
        screen.blit(self.image_enemie, self.portal_enemie_rect)
