from obstacles.obstacle import Obstacle
from utils.Constantes import ENEMIE


class Impostor1(Obstacle):
    position_y = 200

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.step_index = 0
        self.rect.y = self.position_y

    def draw(self, screen):
        if self.step_index >= 20:
            self.step_index = 0
        self.image = ENEMIE[self.step_index // 5]
        screen.blit(self.image, self.rect)
        self.step_index += 1
