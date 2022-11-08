import pygame
from pygame.sprite import Sprite
from utils.Constantes import USER_WAITING, RUNNING_RIGHT, RUNNING_LEFT, JUMPING, GAME_OVER, SCREEN_WIDTH, \
    SCREEN_HEIGHT, TRIP_DEAD


class Tripulante(Sprite):
    X_POS = 20
    Y_POS = 560
    Y_POS_DUCK = 565
    JUMP_VEL = 15

    def __init__(self):
        self.image = USER_WAITING[0]
        self.trip_rect = self.image.get_rect()
        self.trip_rect.x = self.X_POS
        self.trip_rect.y = self.Y_POS
        self.step_index = 0
        self.trip_wait = True
        self.trip_run_right = False
        self.trip_run_left = False
        self.trip_jump = False
        self.touch_portal = False
        self.jump_vel = self.JUMP_VEL

        self.game_over = False
        self.image_game_over = GAME_OVER
        self.image_game_over_rect = self.image_game_over.get_rect()
        self.image_game_over_rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 7

    def update(self, game, user_input):
        if self.trip_jump:
            self.jump()
        if self.trip_run_right:
            self.run_right()
        if self.trip_run_left:
            self.run_left()
        if self.trip_wait:
            self.wait()

        if user_input[pygame.K_RIGHT] and not self.trip_jump:
            self.trip_run_right = True
            self.trip_run_left = False
            self.trip_jump = False
            self.trip_wait = False
            self.touch_portal = False

        elif user_input[pygame.K_LEFT] and not self.trip_jump:
            self.trip_run_left = True
            self.trip_run_right = False
            self.trip_jump = False
            self.trip_wait = False
            self.touch_portal = False

        elif user_input[pygame.K_UP] and not self.trip_jump:
            jump_sound = pygame.mixer.Sound('../sounds/jump.wav')
            jump_sound.play()
            self.trip_jump = True
            self.trip_run_left = False
            self.trip_run_right = False
            self.trip_wait = False
            self.touch_portal = False

        elif not self.trip_jump:
            self.trip_wait = True
            self.trip_run_left = False
            self.trip_run_right = False
            self.trip_jump = False
            self.touch_portal = False

        if self.step_index >= 10:
            self.step_index = 0

    def wait(self):
        self.image = USER_WAITING[0] if self.step_index < 5 else USER_WAITING[1]
        self.trip_rect = self.image.get_rect()
        self.trip_rect.x = self.X_POS
        self.trip_rect.y = self.Y_POS
        self.step_index += 1

    def run_right(self):
        self.image = RUNNING_RIGHT[0] if self.step_index < 5 else RUNNING_RIGHT[1]
        self.trip_rect = self.image.get_rect()
        self.trip_rect.x = self.X_POS
        self.trip_rect.y = self.Y_POS_DUCK
        self.step_index += 1
        self.X_POS += 6

    def run_left(self):
        self.image = RUNNING_LEFT[0] if self.step_index < 5 else RUNNING_LEFT[1]
        self.trip_rect = self.image.get_rect()
        self.trip_rect.x = self.X_POS
        self.trip_rect.y = self.Y_POS_DUCK
        self.step_index += 1
        self.X_POS -= 6

    def jump(self):
        self.image = JUMPING
        if self.trip_jump:
            self.trip_rect.y -= self.jump_vel
            self.trip_rect.x += 3
            self.jump_vel -= 1
            self.X_POS = self.trip_rect.x

        if self.jump_vel < -self.JUMP_VEL:
            self.trip_rect.y = self.Y_POS
            self.trip_jump = False
            self.jump_vel = self.JUMP_VEL

    def teleport(self):
        teleport = pygame.mixer.Sound('../sounds/teleport.mp3')
        teleport.play()
        self.Y_POS = 200
        self.Y_POS_DUCK = 205
        self.X_POS = 200
        self.trip_rect.y = self.Y_POS
        self.trip_rect.x = self.X_POS

    def teleport_down(self):
        teleport = pygame.mixer.Sound('../sounds/teleport.mp3')
        teleport.play()
        self.Y_POS = 560
        self.Y_POS_DUCK = 565
        self.X_POS = 950
        self.trip_rect.y = self.Y_POS
        self.trip_rect.x = self.X_POS

    def reset_position(self):
        self.Y_POS = 560
        self.Y_POS_DUCK = 565
        self.X_POS = 20
        self.trip_rect.x = self.X_POS
        self.trip_rect.y = self.Y_POS

    def draw(self, screen):
        if self.game_over:
            self.image = TRIP_DEAD
        screen.blit(self.image, (self.trip_rect.x, self.trip_rect.y))
        self.print_game_over(screen)

    def print_game_over(self, screen):
        if self.game_over:
            game_over = pygame.mixer.Sound('../sounds/lose.mp3')
            game_over.play()
            self.image_game_over = GAME_OVER
            screen.blit(self.image_game_over, self.image_game_over_rect)
            pygame.display.flip()
            pygame.time.delay(2000)
            self.game_over = False
