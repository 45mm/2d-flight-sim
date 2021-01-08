import pygame, math, pygame.camera, os

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRAVITY=0.24

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE | pygame.DOUBLEBUF)
pygame.display.set_caption("Figuring out Rotation")
clock = pygame.time.Clock()
bg = pygame.image.load(os.path.join('images','bg.png')).convert()
bgx = 0
bgx2 = bg.get_width()
imageSprite = pygame.image.load("sprite.png")

keymap = {
'tiltup': pygame.K_UP, 
'tiltdown': pygame.K_DOWN, 
'decel': None, # implement
'accel': None
}

g = pygame.sprite.Group()
player = Sprite(200, 200, 80, 40, 3, pygame.math.Vector2(3,0))
g.add(player)

while True:
  backscroll()
  mainloop()
  bgx -= player.vel[0]
  bgx2 -= player.vel[0]
  if bgx < bg.get_width() * -1:  
      bgx = bg.get_width()
  if bgx2 < bg.get_width() * -1:
      bgx2 = bg.get_width()
  # if cam is not None:
  #   image = cam.get_image()
    #screen.blit(image, (0, 0))
  if player.RESTART_NEEDED:
    player.restart()
    player.RESTART_NEEDED = False