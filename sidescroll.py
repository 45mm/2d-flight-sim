import pygame

def exec_wrapper(bg):

  bgx = 0 
  bgx2 = bg.get_width()

  def exec(vel1, screen, bg):

    nonlocal bgx
    nonlocal bgx2

    screen.blit(bg, (bgx, 0))
    screen.blit(bg, (bgx2, 0))
    bgx -= 1.4
    bgx2 -= 1.4
    if bgx < bg.get_width() * -1:  
        bgx = bg.get_width()
    if bgx2 < bg.get_width() * -1:
        bgx2 = bg.get_width()
    # if cam is not None:
    #   image = cam.get_image()
      #screen.blit(image, (0, 0))

  return exec
