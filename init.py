import pygame, math
import sidescroll, game_sprites, phy, gamemenu, cam
from constants import *

pygame.init()

resizablesurface = pygame.display.set_mode([VIEW_WIDTH, VIEW_HEIGHT], pygame.RESIZABLE)
screen = resizablesurface.copy()
#screen = pygame.display.set_mode([VIEW_WIDTH, VIEW_HEIGHT], pygame.RESIZABLE)
pygame.display.set_caption("Game Testing")
clock = pygame.time.Clock()


imageSprite = pygame.image.load("images/sprite.png").convert_alpha()
cloudSprite = pygame.image.load("images/clouds.png").convert_alpha()
#birdSprite = pygame.image.load("").convert_alpha()

terrain = pygame.transform.scale(
  pygame.image.load("images/terrain_final4000dpi.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.transform.scale(
  pygame.image.load("images/terrain_final4000dpi.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

player = game_sprites.Sprite(imageSprite, **PLAYER_ARGS)
Cloud = game_sprites.Cloud(cloudSprite, **CLOUD_ARGS)
#Bird = game_sprites.Bird(**bird_args)
Terrain = game_sprites.Terrain(terrain, surface=background)

while True:
  camera = cam.Camera(VW = VIEW_WIDTH, VH = VIEW_HEIGHT, player = player)
  surf = background.copy()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
          quit()

  if GAMEMODE == 'Running':
    #TODO: Move this
    if event.type == pygame.K_d and player.vel.x <= 0:
      player.vel.x = 0 

  elif GAMEMODE == 'Menu':
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      gamemenu.restart_program()
      player.RESTART_NEEDED = False

  elif GAMEMODE == 'Starting':
    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
      GAMEMODE = 'Running'
      START_TIME = pygame.time.get_ticks()

  if event.type == pygame.VIDEORESIZE:
    screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
    VIEW_HEIGHT, VIEW_WIDTH = event.h, event.w
    
  if START_TIME:
    gametime = (pygame.time.get_ticks() - START_TIME)/1000
  
  if GAMEMODE == 'Running':
    screen.fill(SKYBLUE) #TODO: Move this?
    phy.PlanePhy(self=player)
    keys = pygame.key.get_pressed()
    camera.CameraClip(surf)
    player.render(surf)
    Cloud.render(surf)
    #Bird.render(surf)
    player.update(keys, KEYMAP, surf, RunPlayerUpdate)
    Cloud.update(screen = surf, toRun = True, playerclass = player)
    #Bird.update(screen = surf)
    for point in Terrain.mask.outline(8):
      pygame.draw.rect(surf, (255,0,255), (point, (2,2)))

    screen.blit(surf, (0,0), camera)
    gamemenu.flightscore(screen, gametime)

    if player.RESTART_NEEDED:
      GAMEMODE = 'Menu'
      
  elif GAMEMODE == 'Menu':
      if player.RESTART_NEEDED:
        gamemenu.play_game(screen)
        player.RESTART_NEEDED = False
  
  elif GAMEMODE == 'Starting':
    gamemenu.newgame(screen)
    
  resizablesurface.blit(pygame.transform.scale(screen, resizablesurface.get_rect().size), (0, 0))
  pygame.display.flip()
  clock.tick(60)
