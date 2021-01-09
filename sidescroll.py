import pygame

def exec_wrapper(bg):

  bgx = 0 
  bgx2 = bg.get_width()

  def exec(player, screen, bg):

    nonlocal bgx
    nonlocal bgx2

    screen.blit(bg, (bgx, 0))
    screen.blit(bg, (bgx2, 0))
    if (player.vel.x > 0 and player.x > 250) or (player.x < 150 and player.vel.x < 0):
        bgx -= player.vel[0]
        bgx2 -= player.vel[0]
        player.x -= player.vel[0]
    if bgx < bg.get_width() * -1:  
        bgx = bg.get_width()
    if bgx2 < bg.get_width() * -1:
        bgx2 = bg.get_width()
    # if cam is not None:
    #   image = cam.get_image()
      #screen.blit(image, (0, 0))

  return exec
