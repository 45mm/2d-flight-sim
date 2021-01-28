import pygame
import pygame.freetype
import os, sys, psutil, logging #os, sys and logging are inbuilt
from constants import *

pygame.init()
pygame.font.init()

def print_text(text, fontsize, textcolor, bgcolor, isbold):
    font = pygame.freetype.SysFont("Consolas", fontsize, bold=isbold)
    surface, _ = font.render(text=text, fgcolor=textcolor, bgcolor=bgcolor)
    return surface.convert_alpha()

def restart_program():
    try:
        psy = psutil.Process(os.getpid())  #gives id of memory process
        for handler in psy.open_files() + psy.connections():    #sees files open using memory id
            os.close(handler.fd)     #closes the files given by loop
    except Exception as exc:  #wildcard* exception
        logging.error(exc)    #should give a summary of what made program crash ig
    python = sys.executable   #path for executable binary python (bytecode for specific processor)
    os.execl(python, python, *sys.argv)  #execl causes running process 'python' to be replaced by program passed as arguments

def play_game(screen):
    #text1 = 'SCORE: ',str(int(score)),' CLICK TO TRY AGAIN'
    text1 = 'CLICK ANYWHERE TO PLAY AGAIN'
    screen.fill(BLACK)
    playagainbox = print_text(text1, 36, WHITE, None, False)
    againrect = playagainbox.get_rect(center = (screen.get_width()/2, screen.get_height()/2))
    screen.blit(playagainbox, againrect)

def quit_program():
    pygame.time.wait(1000)
    pygame.quit()
    sys.exit()

def newgame(screen):
    newgame_box = print_text('FLIGHT SIMULATOR', 46, WHITE , None, True)
    helpmsg = print_text('ESC: exit| A: decelerate | D: accelerate | UP, DOWN: Rotate', 13, BLUE, None, False)
    presskeymsg = print_text('PRESS ANY KEY TO START', 9, RED, None, True)
    wt, ht = screen.get_width(), screen.get_height()
    keymsg_rect = presskeymsg.get_rect(center = (wt/2, ht*2/3))
    newgame_rect = newgame_box.get_rect(center=(wt/2, ht*1/3))
    help_rect = helpmsg.get_rect(center = (wt/2, ht*3/4))
    screen.blit(newgame_box, newgame_rect)
    screen.blit(presskeymsg, keymsg_rect)
    screen.blit(helpmsg, help_rect)
    
def flightscore(screen, time):
    text1 = 'SCORE: ' + str(int(time))
    score = print_text(text1, 16, WHITE, None, True)
    wt = screen.get_width()
    ht = screen.get_height()
    scorebox = score.get_rect(center = (wt*34/40, ht*39/40))
    screen.blit(score, scorebox)
    flightscore.finalscore = str(int(time))
    
def showfps(screen, fps):
    text1 = 'FPS: ' + str(int(fps))
    fps_text = print_text(text1, 16, WHITE, None, True)
    wt = screen.get_width()
    ht = screen.get_height()
    fps_rect = fps_text.get_rect(center = (wt*34/40, ht*1/40))
    screen.blit(fps_text, fps_rect)
    
    