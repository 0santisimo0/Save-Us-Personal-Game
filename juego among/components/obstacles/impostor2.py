from components.obstacles.obstacles import Obstacles
from utils.Constantes import ENEMIE1


class Impostor2(Obstacles):
    position_y = 210

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.step_index = 0
        self.rect.y = self.position_y

    def draw(self, screen):
        if self.step_index >= 20:
            self.step_index = 0
        self.image = ENEMIE1[self.step_index // 10]
        screen.blit(self.image, self.rect)
        self.step_index += 1
