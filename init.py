import pygame, math
import sidescroll, game_sprites, phy, gamemenu, verticalscroll

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
#GRAVITY=0.01

pygame.init()
surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE)
screen = surface.copy()
pygame.display.set_caption("Game Testing")
clock = pygame.time.Clock()

keymap = {
'tiltup': pygame.K_UP, 
'tiltdown': pygame.K_DOWN,
'decel': pygame.K_a,
'accel': pygame.K_d
}

bg = pygame.image.load("images/bg.png")

sidescroll_exec = sidescroll.exec_wrapper(bg)
verticalscroll_exec = verticalscroll.exec_wrapper(bg)

imageSprite = pygame.image.load("images/sprite.png")
cloudSprite = pygame.image.load("images/clouds.png")
#birdSprite = pygame.image.load("")

player_args = {'imageSprite':imageSprite, 'x':40, 'y':300, 'w':80, 'h':40, 
                            'rot_angle':3, 'vel':pygame.math.Vector2(2,0)}

cloud_args = {'imageSprite':cloudSprite, 'x':35, 'y':255, 'w':80, 'h':40,
                           'rot_angle':3,  'vel':pygame.math.Vector2(-2, 0)}
allSprites = pygame.sprite.Group()

player = game_sprites.Sprite(**player_args)
Cloud = game_sprites.Sprite(**cloud_args)
allSprites.add(player)
allSprites.add(Cloud)

bgx = 0
bgx2 = bg.get_width()

RunPlanePhy = RunPlayerUpdate = RunSidescroll = True
RunVerticalscroll = True

GameMode = 'Starting'


while True:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
          quit()
    if GameMode == 'Running':
      if event.type == pygame.K_d and player.vel.x <= 0:
        player.vel.x = 0 
    elif GameMode == 'Menu':
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        gamemenu.restart_program()
        player.RESTART_NEEDED = False
    elif GameMode == 'Starting':
      if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
        GameMode = 'Running'
    if event.type == pygame.VIDEORESIZE:
      surface = pygame.display.set_mode(event.size, pygame.RESIZABLE)
      SCREEN_HEIGHT, SCREEN_WIDTH = event.h, event.w
    
    
  if GameMode == 'Running':
  
    screen.fill((0,0,0)) #TODO: Move this?
    #sidescroll_exec(player, screen, bg, RunSidescroll)
    #verticalscroll_exec(player, screen, bg, RunVerticalscroll)
    phy.PlanePhy(self=player, liftc=0.01, dragc=0.02, gravity=0.01, HEIGHT=SCREEN_HEIGHT, toRun=RunPlanePhy)
    # mainloop.mainloop(player, screen, keymap, SCREEN_WIDTH, SCREEN_HEIGHT)
    keys = pygame.key.get_pressed()
    player.update(keys, keymap, screen, RunPlayerUpdate)
    player.render(screen)
    player1.render(screen)
    '''
    camera.center = (player.x, player.y)
    player.render(surf)
    surf = bg.copy()
    player.render(surf)
    player1.render(screen)
    screen.blit(surf, (0,0), camera)'''

    if player.RESTART_NEEDED:
      GameMode = 'Menu'
      
  elif GameMode == 'Menu':
      
      if player.RESTART_NEEDED:
        #RunPlanePhy = RunSideScroll = False
        gamemenu.play_game(screen)
        player.RESTART_NEEDED = False
  
  elif GameMode == 'Starting':
    
    gamemenu.newgame(screen)
    
  surface.blit(pygame.transform.scale(screen, surface.get_rect().size), (0, 0))
  pygame.display.flip()
  clock.tick(60)

