import pygame, math
import sidescroll, game_sprites, phy, gamemenu

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRAVITY=0.01

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

player_args = {'imageSprite':imageSprite, 'x':200, 'y':200, 'w':80, 'h':40, 
                            'rot_angle':1.5, 'vel':pygame.math.Vector2(3,0)}

g = pygame.sprite.Group()
# player = game_sprites.Sprite(imageSprite = imageSprite, 
#                             x=200, y=200, w=80, h=40, 
#                             rot_angle=3, vel=pygame.math.Vector2(3,0))
player = game_sprites.Sprite(**player_args)                            
g.add(player)
    

bgx = 0
bgx2 = bg.get_width()

RunPlanePhy = RunPlayerUpdate = RunSidescroll = True

while True:
  screen.fill((0,0,0)) #TODO: Move this?
  sidescroll_exec(player, screen, bg, RunSidescroll)
  phy.PlanePhy(player, 0.01, 0.01, GRAVITY, SCREEN_HEIGHT, RunPlanePhy)
  # mainloop.mainloop(player, screen, keymap, SCREEN_WIDTH, SCREEN_HEIGHT)
  keys = pygame.key.get_pressed()
  player.update(keys, keymap, SCREEN_WIDTH, SCREEN_HEIGHT, RunPlayerUpdate)
  player.render(screen)

  # print(bgx, bgx2)

  for event in pygame.event.get():      
    if event.type == pygame.QUIT:
        quit()
    
  if player.RESTART_NEEDED:
    RunPlanePhy = RunSideScroll = False
    gamemenu.play_game(screen, SCREEN_HEIGHT, SCREEN_WIDTH)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                gamemenu.restart_program()
    player.RESTART_NEEDED = False

  pygame.display.flip()
  clock.tick(60)

