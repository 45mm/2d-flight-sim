import pygame

def exec_wrapper(bg):

  bgx = 0 
  bgx2 = bg.get_width()

  def exec(player, screen, bg, toScroll):
      
    

    nonlocal bgx
    nonlocal bgx2
    
    if toScroll:
        screen.blit(bg, (bgx, 0))
        screen.blit(bg, (bgx2, 0))
        
    if (player.vel.x > 0 and player.x > screen.get_width()/2) or (player.x < (screen.get_height()*3/2) and player.vel.x < 0):
        if toScroll:
            bgx -= player.vel[0]
            bgx2 -= player.vel[0]
        player.x -= player.vel[0]
        
    if bgx < bg.get_width() * -1:  
        bgx = bg.get_width()
    if bgx2 < bg.get_width() * -1:  
        bgx2 = bg.get_width()
        
    if (player.vel.x < 0 and player.x < (screen.get_height()*3/2)):
        if bgx > bg.get_width() :  
            bgx = bg.get_width() * -1
        if bgx2 > bg.get_width() :
            bgx2 = bg.get_width() * -1
    

  return exec
