import pygame, math #, os
import sidescroll, game_sprites, phy #, mainloop

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRAVITY=0.02

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE)
pygame.display.set_caption("Figuring out Rotation")
clock = pygame.time.Clock()
#bg = pygame.image.load(os.path.join('images','bg.png')).convert()

keymap = {
'tiltup': pygame.K_UP, 
'tiltdown': pygame.K_DOWN, 
'decel': None, # implement
'accel': None
}

bg = pygame.image.load("images/bg.png")
sidescroll_exec = sidescroll.exec_wrapper(bg)

imageSprite = pygame.image.load("images/sprite.png")

player_args = {'imageSprite':imageSprite, 'x':200, 'y':200, 'w':80, 'h':40, 
                            'rot_angle':3, 'vel':pygame.math.Vector2(3,0)}
g = pygame.sprite.Group()
# player = game_sprites.Sprite(imageSprite = imageSprite, 
#                             x=200, y=200, w=80, h=40, 
#                             rot_angle=3, vel=pygame.math.Vector2(3,0))
player = game_sprites.Sprite(**player_args)                            
g.add(player)

def restart():
  player = game_sprites.Sprite(**player_args) 
  z = 1000
  pygame.time.wait(z)

bgx = 0
bgx2 = bg.get_width()

while True:
  screen.fill((0,0,0)) #TODO: Move this?
  sidescroll_exec(player, screen, bg)
  phy.PlanePhy(player, 0.00000000001, 0.00000000001, GRAVITY, SCREEN_HEIGHT)
  # mainloop.mainloop(player, screen, keymap, SCREEN_WIDTH, SCREEN_HEIGHT)
  keys = pygame.key.get_pressed()
  player.update(keys, keymap, SCREEN_WIDTH, SCREEN_HEIGHT)
  player.render(screen)

  # print(bgx, bgx2)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        quit()
  
  if player.RESTART_NEEDED:
    restart()
    player.RESTART_NEEDED = False

  pygame.display.update()
  clock.tick(60)
