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

imageSprite = pygame.image.load("images/sprite.png").convert_alpha()
cloudSprite = pygame.image.load("images/clouds.png").convert_alpha()
birdSprite = pygame.image.load("images/bird.png").convert_alpha()
terrainImage = pygame.image.load("images/terrain_final4000dpi.png").convert_alpha()
rawbg = pygame.image.load("images/bg_final2000dpi.png").convert()
terrain = pygame.transform.scale(terrainImage, (SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.transform.scale(rawbg, (SCREEN_WIDTH, SCREEN_HEIGHT))

player = game_sprites.Sprite(imageSprite, **PLAYER_ARGS)
#Cloud = game_sprites.Cloud(cloudSprite, **CLOUD_ARGS)


#\/cloud spawn code
cloudlist=[]
cloudfrequencyc=0
def cloudspawn(camera, cameradist, Terrainclass):# ,safedist):
  safespawn = True
  x=random.random()*SCREEN_WIDTH#-((screen.get_width()/4)*random.random())
  # y=player.y+((random.random()-0.5)*VIEW_HEIGHT)
  y=SCREEN_HEIGHT/2 * random.random()
  # if <=0 or abs(player.y-y)<safedist:
  if camera.rect.left-cameradist<=x<=camera.rect.right+cameradist or camera.rect.top-cameradist<=y<=camera.rect.bottom+cameradist:
    safespawn=False
  # else:
  #   for cloud in cloudlist:
  #     if abs(cloud.rect.x-x)<=safedist  or abs(cloud.rect.y-y)<=safedist :
  #       safespawn=False
  #       break
  if safespawn==True:
    print("spawn allowed")
    #cloud_args = {'cloudSprite':cloudSprite, 'x':SCREEN_WIDTH-((SCREEN_WIDTH/4)*random.random()), 'y':SCREEN_HEIGHT*random.random(), 'w':80, 'h':40, 'cloudvelc':5}
    cloudvar=game_sprites.Cloud(cloudSprite=cloudSprite, x=x, y=y, **CLOUD_ARGS)
    collidedmask = pygame.sprite.collide_mask(cloudvar, Terrainclass)
    print(collidedmask)
    if collidedmask == None:
      cloudlist.append(cloudvar)
      
def cloudupdate():
  for cloud in cloudlist:
    cloud.update(surf,player)
    cloud.render(surf)

#Bird = game_sprites.Birds(birdSprite, **BIRD_ARGS)
birdlist=[]
birdfrequencyc=0
def birdspawn(camera, cameradist, Terrainclass):
  safespawn = True
  x=random.random()*SCREEN_WIDTH
  y=SCREEN_HEIGHT/2 * random.random()
  if camera.rect.left-cameradist<=x<=camera.rect.right+cameradist or camera.rect.top-cameradist<=y<=camera.rect.bottom+cameradist:
    safespawn=False
    
  if safespawn==True:
    print("spawn allowed")
    birdvar=game_sprites.Birds(birdSprite=birdSprite, x=x, y=y, **BIRD_ARGS)
    collidedmask = pygame.sprite.collide_mask(birdvar, Terrainclass)
    print(collidedmask)
    if collidedmask == None:
      birdlist.append(birdvar)
      
def birdupdate():
  for bird in birdlist:
    bird.update(surf)
    bird.render(surf)

Terrain = game_sprites.Terrain(terrain, surface=background)

image_rect = background.get_rect()
surf = pygame.Surface((image_rect.width, image_rect.height))
#pygame.draw.rect(surf, (0,0,0), (VIEW_WIDTH, VIEW_HEIGHT, 0, 0))

while True:
  camera = cam.Camera(VW = VIEW_WIDTH, VH = VIEW_HEIGHT, player = player)
  #surf = background.copy()
  surf.blit(background, image_rect)
  #screen.blit(surf, image_rect)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
          quit()
    if GAMEMODE == 'Running':
      pass
      #TODO: Move this
    elif GAMEMODE == 'Menu':
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        gamemenu.restart_program()
        player.RESTART_NEEDED = False
    elif GAMEMODE == 'Starting':
      if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
        GAMEMODE = 'Running'
        START_TIME = pygame.time.get_ticks()
    if event.type == pygame.VIDEORESIZE:
      screen = pygame.display.set_mode(event.size, flags)
      VIEW_HEIGHT, VIEW_WIDTH = event.h, event.w
    
  if START_TIME:
    gametime = (pygame.time.get_ticks() - START_TIME)/1000
  
  if GAMEMODE == 'Running':
    screen.blit(terrain, (0,0))
    phy.PlanePhy(self=player)
    keys = pygame.key.get_pressed()
    camera.CameraClip(surf)
    player.render(surf)
    #Cloud.render(surf)
    #Bird.render(surf)
    player.update(keys, KEYMAP, surf, RunPlayerUpdate)
    #Cloud.update(screen = surf, toRun = True, playerclass = player)
    if cloudfrequencyc%10==0:
      cloudspawn(camera, 150, Terrain)
    cloudupdate()
    if birdfrequencyc%10 == 0:
      birdspawn(camera, 50, Terrain)
    birdupdate()
    #Bird.update(screen = surf)
    # for point in Terrain.mask.outline(8):
      # pygame.draw.rect(surf, (255,0,255), (point, (2,2)))
    #renderimage = pygame.transform.chop(surf, camera.rect)
    screen.blit(surf, (0,0), camera)
    gamemenu.flightscore(screen, gametime)
    fps_rn = clock.get_fps()
    gamemenu.showfps(screen, fps_rn)

    if player.RESTART_NEEDED:
      GAMEMODE = 'Menu'
      
  elif GAMEMODE == 'Menu':
      if player.RESTART_NEEDED:
        gamemenu.play_game(screen)
        player.RESTART_NEEDED = False
  
  elif GAMEMODE == 'Starting':
    gamemenu.newgame(screen)
    
  #try:
  #  resizablesurface.blit(pygame.transform.scale(renderimage, resizablesurface.get_rect().size), (0, 0))
  #except:
  
  resizablesurface.blit(pygame.transform.scale(screen, resizablesurface.get_rect().size), (0, 0))   
  pygame.display.flip() 
  pygame.event.pump()
  clock.tick(60)
  birdfrequencyc += 1
  
