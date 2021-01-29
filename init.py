import pygame, math, random
import sidescroll, game_sprites, phy, gamemenu, cam
from constants import *

pygame.init()

resizablesurface = pygame.display.set_mode([VIEW_WIDTH, VIEW_HEIGHT], flags)
screen = resizablesurface.copy()
#screen = pygame.display.set_mode([VIEW_WIDTH, VIEW_HEIGHT], pygame.RESIZABLE)
pygame.display.set_caption("Game Testing")
clock = pygame.time.Clock()

# for cloudnum in range(4):
#   path = ("images/cloud{}.png".format(cloudnum))
#   cloud%d.format(cloudnum) = pygame.image.load(path).convert_alpha()

imageSprite = pygame.image.load("images/drawn_plane_white_89x20.png").convert_alpha()

terrainImage = pygame.image.load("images/terrain_final4000dpi.png").convert_alpha()
rawbg = pygame.image.load("images/bg_trans_2000dpi.png").convert()

cloudSprite = pygame.image.load("images/clouds_trans.png")#.convert_alpha()
birdSprite = pygame.image.load("images/bird.png")#.convert_alpha()

terrain = pygame.transform.scale(terrainImage, (SCREEN_WIDTH, SCREEN_HEIGHT)) 
background = pygame.transform.scale(rawbg, (SCREEN_WIDTH, SCREEN_HEIGHT))

player = game_sprites.Sprite(imageSprite, **PLAYER_ARGS)
#Cloud = game_sprites.Cloud(cloudSprite, **CLOUD_ARGS)

Terrain = game_sprites.Terrain(terrain, surface=background)

image_rect = background.get_rect()
surf = pygame.Surface((image_rect.width, image_rect.height))
#pygame.draw.rect(surf, (0,0,0), (VIEW_WIDTH, VIEW_HEIGHT, 0, 0))

RunAgain = False

def mainloop():
  
  global START_TIME, VIEW_WIDTH, VIEW_HEIGHT, RUN_PLAYER_UPDATE, RUN_PLAYER_PHY, RUN_SIDESCROLL, GAMEMODE
  global resizablesurface, screen, clock, imageSprite, terrainImage, rawbg, cloudSprite, birdSprite, terrain, background, player, Terrain
  global image_rect, surf, spawn_freq
  
  camera = cam.Camera(VW = VIEW_WIDTH, VH = VIEW_HEIGHT, player = player)
  #surf = background.copy()
  surf.blit(background, image_rect)
  #screen.blit(surf, image_rect)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()       
          
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        quit()
    
    if GAMEMODE == 'Starting':
      if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
        GAMEMODE = 'Running'
        START_TIME = pygame.time.get_ticks()
        
    if GAMEMODE == 'Menu':
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        gamemenu.restart_program()
        RunAgain = True
        player.RESTART_NEEDED = False
        
    if event.type == pygame.VIDEORESIZE:
      screen = pygame.display.set_mode(event.size, flags)
      VIEW_HEIGHT, VIEW_WIDTH = event.h, event.w
      
  if START_TIME:
    gametime = (pygame.time.get_ticks() - START_TIME)/1000   
        
  if GAMEMODE == 'Running':
      #screen.blit(terrain, (0,0))
    surf.blit(terrain, camera.rect, camera.rect)
    phy.PlanePhy(self=player)
    keys = pygame.key.get_pressed()
    camera.CameraClip(surf)
    player.render(surf)
    player.update(keys, KEYMAP, surf, RUN_PLAYER_UPDATE,3)
    if spawn_freq%15==0:
      game_sprites.Cloud.cloudspawn(camera, 150, Terrain, birdSprite)
      game_sprites.Bird.birdspawn(camera, 50, Terrain, cloudSprite)
    game_sprites.Bird.birdupdate(surf = surf)
    game_sprites.Cloud.cloudupdate(surf = surf, player = player)
    screen.blit(surf, (0,0), camera)
    #screen.blit(surf, camera.get_rect())
    gamemenu.flightscore(screen, gametime)
    fps_rn = clock.get_fps()
    gamemenu.showfps(screen, fps_rn)
    if player.RESTART_NEEDED:
      GAMEMODE = 'Menu'
      
  elif GAMEMODE == 'Starting':
    gamemenu.newgame(screen) 
  
  resizablesurface.blit(pygame.transform.scale(screen, resizablesurface.get_rect().size), (0, 0))   
  pygame.display.update() 
  pygame.event.pump()
  clock.tick(60)
  spawn_freq += 1
  
while True:
  mainloop()
  
