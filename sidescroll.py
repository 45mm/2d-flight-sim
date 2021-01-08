def backscroll():
  screen.blit(bg, (bgx, 0))
  screen.blit(bg, (bgx2, 0))


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
  