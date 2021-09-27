import pygame

from utils.Constantes import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE


def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 22)
    white_color = (255, 255, 255)
    text = font.render('Time: ' + str(points), True, white_color)
    text_rect = text.get_rect()
    text_rect.center = (1100, 50)
    return text, text_rect


def get_centered_message(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FONT_STYLE, 40)
    blue_color = ('#D4ECDD')
    text = font.render(message, True, blue_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
