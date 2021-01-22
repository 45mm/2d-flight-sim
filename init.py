import pygame, math, random
import sidescroll, game_sprites, phy, gamemenu, cam

SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 2000
start_time = None

#GRAVITY=0.01
VIEW_WIDTH = 500
VIEW_HEIGHT = 500

pygame.init()

surface = pygame.display.set_mode([VIEW_WIDTH, VIEW_HEIGHT], pygame.RESIZABLE)
screen = surface.copy()
#screen = pygame.display.set_mode([VIEW_WIDTH, VIEW_HEIGHT], pygame.RESIZABLE)
pygame.display.set_caption("Game Testing")
clock = pygame.time.Clock()

keymap = {
'tiltup': pygame.K_UP, 
'tiltdown': pygame.K_DOWN,
'decel': pygame.K_a,
'accel': pygame.K_d
}

bg = pygame.transform.scale(
  pygame.image.load("images/terrain4000dpi.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
# bg = pygame.image.load("images/bg.png").convert_alpha()
#bg = pygame.transform.scale(
#  pygame.image.load("images/bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

sidescroll_exec = sidescroll.exec_wrapper(bg)

imageSprite = pygame.image.load("images/sprite.png").convert_alpha()
cloudSprite = pygame.image.load("images/clouds.png").convert_alpha()
#birdSprite = pygame.image.load("").convert_alpha()

player_args = {'imageSprite':imageSprite, 'x':140, 'y':300, 'w':80, 'h':40, 
                            'rot_angle':3, 'vel':pygame.math.Vector2(2,0)}
#cloud_args = {'cloudSprite':cloudSprite, 'x':SCREEN_WIDTH*random.random(),
#                           'y':150*random.random(), 'w':80, 'h':40, 'cloudvelc':5}
terrain_args = {'ground':bg , 'surface':surface}

allSprites = pygame.sprite.Group()

player = game_sprites.Sprite(**player_args)
Terrain = game_sprites.Terrain(**terrain_args)
allSprites.add(player)

#\/cloud spawn code
cloudlist=[]
cloudfrequencyc=0
def cloudspawn(safedist):
  safespawn = True
  x=screen.get_width()-(screen.get_width())/4*random.random()
  y=screen.get_height()*random.random()
  for cloud in cloudlist:
    if abs(cloud.rect.x-x)<=safedist or abs(player.x-x<safedist) or abs(cloud.rect.y-y<=safedist) or abs(player.y-y<safedist):
      safespawn=False
      break
  if safespawn==True:
    #cloud_args = {'cloudSprite':cloudSprite, 'x':SCREEN_WIDTH-((SCREEN_WIDTH/4)*random.random()), 'y':SCREEN_HEIGHT*random.random(), 'w':80, 'h':40, 'cloudvelc':5}
    cloud_args = {'cloudSprite':cloudSprite, 'x':x, 'y':y, 'w':80, 'h':40, 'cloudvelc':3}
    cloudvar=game_sprites.Cloud(**cloud_args)
    cloudlist.append(cloudvar)
    allSprites.add(cloudvar)
def cloudupdate():
  for cloud in cloudlist:
    cloud.update(surf,player)
    cloud.render(surf)
  #cloudvar.update(surf, player)
  #return cloudvar
bgx = 0
bgx2 = bg.get_width()

RunPlanePhy = RunPlayerUpdate = RunSidescroll = True
RunVerticalscroll = True
finalscore = 0

GameMode = 'Starting'


while True:
  
  camera = cam.Camera(VW = VIEW_WIDTH, VH = VIEW_HEIGHT, player = player)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
          quit()
  
  surf = bg.copy()

  if GameMode == 'Running':
    # TODO: move this to the Sprite class
    if event.type == pygame.K_d and player.vel.x <= 0:
      player.vel.x = 0 

  elif GameMode == 'Menu':
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      gamemenu.restart_program()
      player.RESTART_NEEDED = False

  elif GameMode == 'Starting':
    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
      GameMode = 'Running'
      start_time = pygame.time.get_ticks()

  if event.type == pygame.VIDEORESIZE:
    screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
    VIEW_HEIGHT, VIEW_WIDTH = event.h, event.w
    
  if start_time:
    gametime = (pygame.time.get_ticks() - start_time)/1000
  
  if GameMode == 'Running':
    
    screen.fill((0,191,255)) #TODO: Move this?
    # sidescroll_exec(player, screen, bg, RunSidescroll)
    #verticalscroll_exec(player, screen, bg, RunVerticalscroll)
    phy.PlanePhy(self=player, liftc=0.01, dragc=0.02, gravity=0.01, HEIGHT=SCREEN_HEIGHT, toRun=RunPlanePhy)
    keys = pygame.key.get_pressed()
    camera.CameraClip(surf)
    player.render(surf)
    #cloud = cloudspawn()
    if cloudfrequencyc%15==0:
      cloudspawn(50)
    cloudupdate()
    
    player.update(keys, keymap, surf, RunPlayerUpdate)
    #cloud.update(screen = surf, toRun = True, playerclass = player)

    #print(player.RESTART_NEEDED)

    screen.blit(surf, (0,0), camera)
    gamemenu.flightscore(screen, gametime)
    score = (gamemenu.flightscore.finalscore)
    
    if player.RESTART_NEEDED:
      finalscore = score
      GameMode = 'Menu'
      
  elif GameMode == 'Menu':
      
      if player.RESTART_NEEDED:
        #RunPlanePhy = RunSideScroll = False
        #gamemenu.play_game(screen, finalscore)
        gamemenu.play_game(screen)
        player.RESTART_NEEDED = False
  
  elif GameMode == 'Starting':
    
    gamemenu.newgame(screen)
    
  cloudfrequencyc+=1
  surface.blit(pygame.transform.scale(screen, surface.get_rect().size), (0, 0))
  pygame.display.flip()
  clock.tick(60)
