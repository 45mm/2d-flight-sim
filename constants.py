import pygame, game_sprites
pygame.init()

SCREEN_WIDTH = 5000
SCREEN_HEIGHT = 500
START_TIME = None

#GRAVITY=0.01
VIEW_WIDTH = 500
VIEW_HEIGHT = 500

KEYMAP = {
'tiltup': pygame.K_UP,
'tiltdown': pygame.K_DOWN,
'decel': pygame.K_a,
'accel': pygame.K_d
}

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0,0,0)
SKYBLUE = (135,206,235)

LIFTC = 0.01
DRAGC =0.02
GRAVITY= 0.01


PLAYER_ARGS = { 'x':150, 'y':250, 'w':80, 'h':40, 
                            'rot_angle':3, 'vel':pygame.math.Vector2(2,0)}
CLOUD_ARGS = { 'x':0, 'y':20, 'w':80, 'h':40, 'cloudvelc':5}
#bird_args = {'birdSprite':birdSprite, 'x':100, 'y':100, 'w':80, 'h':40, 'birdvelx':4, 'birdvely':2}

RunPlanePhy = RunPlayerUpdate = RunSidescroll = True
RunVerticalscroll = True

GAMEMODE = 'Starting'


