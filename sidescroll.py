def exec(vel1, screen, bg):
  bgx = 0
  bgx2 = bg.get_width()
  screen.blit(bg, (bgx, 0))
  screen.blit(bg, (bgx2, 0))
  bgx -= vel1
  bgx2 -= vel1
  if bgx < bg.get_width() * -1:  
      bgx = bg.get_width()
  if bgx2 < bg.get_width() * -1:
      bgx2 = bg.get_width()
  # if cam is not None:
  #   image = cam.get_image()
    #screen.blit(image, (0, 0))
  
  