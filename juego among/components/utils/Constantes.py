import os
import pygame

# global
TITLE = 'Save US'
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), '..', 'elementos')
BG = pygame.image.load(os.path.join(IMG_DIR, 'stars/fondospace.png'))
ICON = pygame.image.load(os.path.join(IMG_DIR, 'other/icon.jpg'))
RESTART = pygame.image.load(os.path.join(IMG_DIR, 'other/reset.png'))

ICON_MENU = pygame.image.load(os.path.join(IMG_DIR, 'other/icono.png'))
ICON_MENU = pygame.transform.scale(ICON_MENU, (450, 200))

FONT_STYLE = os.path.join(IMG_DIR, 'other/abc.ttf')

# assets
STAR = pygame.image.load(os.path.join(IMG_DIR, 'stars/star1.png'))
STAR = pygame.transform.scale(STAR, (7, 7))
STAR_SMALL = pygame.image.load(os.path.join(IMG_DIR, 'stars/star1.png'))
STAR_SMALL = pygame.transform.scale(STAR, (5, 5))
STAR_DRAW = [STAR, STAR_SMALL]

VICTORY = pygame.image.load(os.path.join(IMG_DIR, 'other/victory.png'))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'other/defeat.png'))
GAME_OVER =pygame.transform.scale(GAME_OVER, (500, 100))

SURFACE = pygame.image.load(os.path.join(IMG_DIR, 'stars/platform4.png'))
SURFACE.get_rect()

SHIP = [pygame.image.load(os.path.join(IMG_DIR, 'other/ship transp.png')),
        pygame.image.load(os.path.join(IMG_DIR, 'other/ship transp.png'))]


USER_WAITING = [pygame.image.load(os.path.join(IMG_DIR, 'user/trip.png')),
                pygame.image.load(os.path.join(IMG_DIR, 'user/tripwait.png'))]

USER_WAITING1 = [pygame.image.load(os.path.join(IMG_DIR, 'user/trip1.png')),
                 pygame.image.load(os.path.join(IMG_DIR, 'user/tripwait1.png'))]

TRIP_DEAD = pygame.image.load(os.path.join(IMG_DIR, 'user/tripdead.png'))
TRIP_DEAD = pygame.transform.scale(TRIP_DEAD, (100, 80))

ENEMIE = [pygame.image.load(os.path.join(IMG_DIR, 'enemies/impostorlengua1a.png')),
          pygame.image.load(os.path.join(IMG_DIR, 'enemies/impostorlengua1b.png')),
          pygame.image.load(os.path.join(IMG_DIR, 'enemies/impostorlengua1c.png')),
          pygame.image.load(os.path.join(IMG_DIR, 'enemies/impostorlengua1b.png'))]

ENEMIE1 = [pygame.image.load(os.path.join(IMG_DIR, 'enemies/impostorlengua.png')),
           pygame.image.load(os.path.join(IMG_DIR, 'enemies/impostorlengua1.png'))]

ENEMIE2 = [pygame.image.load(os.path.join(IMG_DIR, 'enemies/enemiefly.png')),
           pygame.image.load(os.path.join(IMG_DIR, 'enemies/enemieflya.png')),
           pygame.image.load(os.path.join(IMG_DIR, 'enemies/enemieflyb.png')),
           pygame.image.load(os.path.join(IMG_DIR, 'enemies/enemieflya.png'))]

ENEMIE3 = [pygame.image.load(os.path.join(IMG_DIR, 'enemies/fantasmaa.png')),
           pygame.image.load(os.path.join(IMG_DIR, 'enemies/fantasmab.png')),
           pygame.image.load(os.path.join(IMG_DIR, 'enemies/fantasmac.png')),
           pygame.image.load(os.path.join(IMG_DIR, 'enemies/fantasmab.png'))]

ENEMIE4 = [pygame.image.load(os.path.join(IMG_DIR, 'enemies/enemieship.png')),
           pygame.image.load(os.path.join(IMG_DIR, 'enemies/enemieship1.png'))]

RUNNING_RIGHT = [pygame.image.load(os.path.join(IMG_DIR, 'user/runright.png')),
                 pygame.image.load(os.path.join(IMG_DIR, 'user/runright1.png'))]

RUNNING_LEFT = [pygame.image.load(os.path.join(IMG_DIR, 'user/runleft.png')),
                pygame.image.load(os.path.join(IMG_DIR, 'user/runleft1.png'))]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, 'user/fly.png'))

IMPOSTOR_TONGUE = pygame.image.load(os.path.join(IMG_DIR, 'enemies/impostorlengua.png'))

PORTAL_LEFT = [pygame.image.load(os.path.join(IMG_DIR, 'stars/portaleft.png')),
               pygame.image.load(os.path.join(IMG_DIR, 'stars/portaleftA.png')),
               pygame.image.load(os.path.join(IMG_DIR, 'stars/portaleftB.png')),
               pygame.image.load(os.path.join(IMG_DIR, 'stars/portaleftC.png')),
               pygame.image.load(os.path.join(IMG_DIR, 'stars/portaleftB.png')),
               pygame.image.load(os.path.join(IMG_DIR, 'stars/portaleftA.png'))]

PORTAL_RIGHT = [pygame.image.load(os.path.join(IMG_DIR, 'stars/portalright.png')),
                pygame.image.load(os.path.join(IMG_DIR, 'stars/portalrightA.png')),
                pygame.image.load(os.path.join(IMG_DIR, 'stars/portalrightB.png')),
                pygame.image.load(os.path.join(IMG_DIR, 'stars/portalrightC.png')),
                pygame.image.load(os.path.join(IMG_DIR, 'stars/portalrightB.png')),
                pygame.image.load(os.path.join(IMG_DIR, 'stars/portalrightA.png'))]

ENEMIES_PORTAL = [pygame.image.load(os.path.join(IMG_DIR, 'other/port rick.png')),
                  pygame.image.load(os.path.join(IMG_DIR, 'other/port rick (1).png')),
                  pygame.image.load(os.path.join(IMG_DIR, 'other/port rick (2).png')),
                  pygame.image.load(os.path.join(IMG_DIR, 'other/port rick (3).png')),
                  pygame.image.load(os.path.join(IMG_DIR, 'other/port rick (2).png')),
                  pygame.image.load(os.path.join(IMG_DIR, 'other/port rick (1).png'))]

CREW_JAIL = pygame.image.load(os.path.join(IMG_DIR, 'other/trips.png'))
CREW_JAIL = pygame.transform.scale(CREW_JAIL, (150, 200))

PLAT_CREW = pygame.image.load(os.path.join(IMG_DIR, 'other/platcrew.png'))

SHIP_TRIP = pygame.image.load(os.path.join(IMG_DIR, 'other/shipcrew.png'))
