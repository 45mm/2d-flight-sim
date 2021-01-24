import pygame

def exec_wrapper(bg):
  bgy = 0
  bgy2 = bg.get_height()

  def exec(player, screen, bg, toScroll):

    nonlocal bgy
    nonlocal bgy2

    if toScroll:
      screen.blit(bg, (0, bgy))
      screen.blit(bg, (0, bgy2))

    if (player.vel.y > 0 and player.y > screen.get_height()/2) or (player.y < (screen.get_height()*3/2) and player.vel.y < 0):
      if toScroll:
        bgy -= player.vel[1]
        bgy2 -= player.vel[1]
      player.y -= player.vel[1]

    if bgy<bg.get_height()*(-1):
      bgy = bg.get_height()
      
    if bgy2 < bg.get_height()*(-1):
      bgy2 = bg.get_height()

    if (player.vel.y<0 and player.y<(screen.get_width()*3/2)):
      if bgy > bg.get_height():
        bgy = bg.get_height()*(-1)
        
      if bgy2>bg.get_height():
        bgy2 = bg.get_height()*(-1)

  return exec