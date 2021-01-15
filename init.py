import pygame, math
import sidescroll, game_sprites, phy, gamemenu

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
#GRAVITY=0.01

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE)
pygame.display.set_caption("Game Testing")
clock = pygame.time.Clock()
#bg = pygame.image.load(os.path.join('images','bg.png')).convert()

keymap = {
'tiltup': pygame.K_UP, 
'tiltdown': pygame.K_DOWN,
'decel': pygame.K_a,
'accel': pygame.K_d
}

bg = pygame.image.load("images/bg.png")
#cloud = pygameimage.load("")
#bird = pygame.image.load("")
sidescroll_exec = sidescroll.exec_wrapper(bg)

imageSprite = pygame.image.load("images/sprite.png")

player_args = {'imageSprite':imageSprite, 'x':40, 'y':300, 'w':80, 'h':40, 
                            'rot_angle':3, 'vel':pygame.math.Vector2(2,0)}

g = pygame.sprite.Group()
# player = game_sprites.Sprite(imageSprite = imageSprite, 
#                             x=200, y=200, w=80, h=40, 
#                             rot_angle=3, vel=pygame.math.Vector2(3,0))
player = game_sprites.Sprite(**player_args)                            
g.add(player)
    

bgx = 0
bgx2 = bg.get_width()

RunPlanePhy = RunPlayerUpdate = RunSidescroll = True

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
    
    
  if GameMode == 'Running':
  
    screen.fill((0,0,0)) #TODO: Move this?
    sidescroll_exec(player, screen, bg, RunSidescroll)
    phy.PlanePhy(self=player, liftc=0.01, dragc=0.05, gravity=0.01, HEIGHT=SCREEN_HEIGHT, toRun=RunPlanePhy)
    # mainloop.mainloop(player, screen, keymap, SCREEN_WIDTH, SCREEN_HEIGHT)
    keys = pygame.key.get_pressed()
    player.update(keys, keymap, SCREEN_WIDTH, SCREEN_HEIGHT, RunPlayerUpdate)
    player.render(screen)

    if player.RESTART_NEEDED:
      GameMode = 'Menu'
      
  elif GameMode == 'Menu':
      
      if player.RESTART_NEEDED:
        #RunPlanePhy = RunSideScroll = False
        gamemenu.play_game(screen, SCREEN_HEIGHT, SCREEN_WIDTH)
        player.RESTART_NEEDED = False
  
  elif GameMode == 'Starting':
    
    gamemenu.newgame(screen, SCREEN_HEIGHT, SCREEN_WIDTH)
    
      
  pygame.display.flip()
  clock.tick(60)

