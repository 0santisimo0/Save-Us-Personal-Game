import pygame
import random

from utils import text_utils
from utils.Constantes import (
    TITLE,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    BG,
    FPS,
    STAR_DRAW,
    SURFACE,
    RESTART, ICON_MENU, CREW_JAIL, SHIP_TRIP, VICTORY, PLAT_CREW)
from obstacles.obstaclesManager import ObstaclesManager
from portal import Portal
from tripulante import Tripulante


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        pygame.mixer.music.load('sounds/nocturne.mp3')
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.restart_bottom = RESTART.get_rect()
        self.x_pos_star = random.randint(10, 1190)
        self.y_pos_star = random.randint(10, 690)
        self.crew_jail = CREW_JAIL.get_rect()
        self.portal = Portal()
        self.player = Tripulante()
        self.obstacles_manager = ObstaclesManager()
        self.start_timer = pygame.time.get_ticks()
        self.running = True
        self.win = False
        self.x_pos_ship = 0
        self.death_count = 0
        self.win_count = 0
        self.points = 0
        self.game_speed = 4
        self.stars_vel = 0
        self.best_time = 0

    def run(self):
        start_sound = pygame.mixer.Sound('sounds/boton.mp3')
        start_sound.play()
        self.points = 0
        self.player.reset_position()
        self.obstacles_manager.reset_obstacles()
        self.playing = True
        self.game_speed = 4
        while self.playing:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                exit()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.portal.update()
        self.player.update(self, user_input)
        self.obstacles_manager.update(self)

        if self.stars_vel >= 40:
            self.stars_vel = 0

    def draw(self):
        self.clock.tick(FPS)
        self.draw_background()
        self.score()
        self.portal.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacles_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def score(self):
        self.points = round((0.01 + self.points), 2)
        if self.points % 0.5 == 0:
            self.game_speed += 1
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)

    def best_time_obtained(self):
        if self.win_count > 1:
            if self.points < self.best_time:
                self.best_time = self.points
        else:
            self.best_time = self.points

    def draw_background(self):
        self.draw_stars()

        surface_level_1 = pygame.transform.scale(SURFACE, (900, 150))
        self.screen.blit(surface_level_1, (140, 260))
        surface_ground = pygame.transform.scale(SURFACE, (1100, 400))
        self.screen.blit(surface_ground, (-20, 620))
        surface_jail = PLAT_CREW.get_rect()
        surface_jail.midtop = (1130, 240)
        self.screen.blit(PLAT_CREW, surface_jail)
        self.crew_jail.midbottom = (1130, 300)
        self.screen.blit(CREW_JAIL, self.crew_jail)

    def draw_stars(self):
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))

        stars = STAR_DRAW[self.stars_vel // 20]
        self.stars_vel += 1

        if self.stars_vel in range(0, 2):
            self.screen.blit(stars, (random.randint(10, 1190), random.randint(10, 690)))
        elif self.stars_vel in range(20, 21):
            self.screen.blit(stars, (random.randint(10, 1190), random.randint(10, 690)))

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if self.death_count == 0 and event.type == pygame.KEYDOWN:
                self.run()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                if self.restart_bottom.collidepoint(click):
                    self.run()

    def execute(self):
        pygame.mixer.music.play(2)
        while self.running:
            if not self.playing and not self.win:
                self.show_menu()
            elif self.win:
                self.victory_animation()

    def show_menu(self):
        self.running = True
        self.clock.tick(FPS)

        if self.stars_vel >= 40:
            self.stars_vel = 0
        self.draw_stars()
        self.print_menu_elements()

        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message("Press Any Key to Start")
        else:
            text, text_rect = text_utils.get_centered_message("Press to Restart")
            self.restart_bottom.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.2)
            self.screen.blit(RESTART, self.restart_bottom)
            death_score, death_score_rect = text_utils.get_centered_message("Death count: " + str(self.death_count),
                                                                            height=half_screen_height + 50)
            points_score, points_score_rect = text_utils.get_centered_message("Time: " + str(self.points),
                                                                              height=half_screen_height + 100)
            vic_count, vic_count_rect = text_utils.get_centered_message('Victory count: ' + str(self.win_count),
                                                                        height=half_screen_height + 150)
            self.screen.blit(vic_count, vic_count_rect)
            self.screen.blit(death_score, death_score_rect)
            self.screen.blit(points_score, points_score_rect)
            max_score, max_score_rect = text_utils.get_centered_message('Best Time: ' + str(self.best_time),
                                                                        height=half_screen_height + 200)
            self.screen.blit(max_score, max_score_rect)

        menu_icon_rect = ICON_MENU.get_rect()
        menu_icon_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3.2)
        self.screen.blit(ICON_MENU, menu_icon_rect)
        self.screen.blit(text, text_rect)

    def handle_key_in_victory_animation(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                if self.restart_bottom.collidepoint(click):
                    self.win = False
                    self.x_pos_ship = 0
                    self.run()

    def victory_animation(self):
        self.running = True
        pygame.display.update()
        self.handle_key_in_victory_animation()

        self.clock.tick(FPS)
        if self.stars_vel >= 40:
            self.stars_vel = 0
        self.draw_stars()
        ship_crew_image = SHIP_TRIP
        ship_crew_rect = ship_crew_image.get_rect()
        ship_crew_rect.midleft = (0, SCREEN_HEIGHT / 2)
        self.x_pos_ship += self.game_speed

        self.screen.blit(ship_crew_image, (self.x_pos_ship + ship_crew_rect.x, SCREEN_HEIGHT / 2))

        if self.x_pos_ship >= 1250:
            half_screen_height = SCREEN_HEIGHT // 2
            self.restart_bottom.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.2)
            death_score, death_score_rect = text_utils.get_centered_message("Death count: " + str(self.death_count),
                                                                            height=half_screen_height + 50)
            points_score, points_score_rect = text_utils.get_centered_message("Time: " + str(self.points),
                                                                              height=half_screen_height + 100)

            vic_count, vic_count_rect = text_utils.get_centered_message('Victory count: ' + str(self.win_count),
                                                                        height=half_screen_height + 150)
            self.screen.blit(vic_count, vic_count_rect)

            self.best_time_obtained()
            max_score, max_score_rect = text_utils.get_centered_message('Best Time: ' + str(self.best_time),
                                                                        height=half_screen_height + 200)
            self.screen.blit(max_score, max_score_rect)

            victory_rect = VICTORY.get_rect()
            victory_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3.2)
            self.screen.blit(VICTORY, victory_rect)
            victory_sound = pygame.mixer.Sound('sounds/vic.mp3')
            victory_sound.play()
            pygame.time.delay(1000)
            self.screen.blit(death_score, death_score_rect)
            self.screen.blit(points_score, points_score_rect)
            self.screen.blit(RESTART, self.restart_bottom)
