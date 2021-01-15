import pygame
import pygame.freetype
import os, sys, psutil, logging #os, sys and logging are inbuilt

pygame.init()
pygame.font.init()
#font colors (rgb)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0,0,0)

bigfont = pygame.font.SysFont("Consolas", 80)
smallfont = pygame.font.SysFont("Consolas", 45)

def restart_program():
    try:
        psy = psutil.Process(os.getpid())  #gives id of memory process
        for handler in psy.open_files() + psy.connections():    #sees files open using memory id
            os.close(handler.fd)     #closes the files given by loop
    except Exception as exc:  #wildcard* exception
        logging.error(exc)    #should give a summary of what made program crash ig
    python = sys.executable   #path for executable binary python (bytecode for specific processor)
    os.execl(python, python, *sys.argv)  #execl causes running process 'python' to be replaced by program passed as arguments

def play_game(screen, ht, wt):
    text = bigfont.render('Play again?', 12, (0, 0, 0))
    textx = wt / 2 - text.get_width() / 2
    texty = ht / 2 - text.get_height() / 2
    textx_size = text.get_width()
    texty_size = text.get_height()
    pygame.draw.rect(screen, (255, 255, 255), ((textx - 5, texty - 5),
                                               (textx_size + 10, texty_size +
                                                10)))
    screen.blit(text, (wt / 2 - text.get_width() / 2,
                       ht / 2 - text.get_height() / 2))
    

def quit_program():
    pygame.time.wait(1000)
    pygame.quit()
    sys.exit()

def print_text(text, fontsize, textcolor, bgcolor, isbold):
    font = pygame.freetype.SysFont("Consolas", fontsize, bold=isbold)
    surface, _ = font.render(text=text, fgcolor=textcolor, bgcolor=bgcolor)
    return surface.convert_alpha()

def newgame(screen, ht, wt):
    newgame_box = print_text('FLIGHT SIMULATOR', 46, WHITE , BLACK, True)
    presskeymsg = print_text('PRESS ANY KEY TO START', 9, RED, BLACK, True)
    keymsg_rect = presskeymsg.get_rect(center = (wt/2, ht*2/3))
    newgame_rect = newgame_box.get_rect(center=(wt/2, ht/2))
    screen.blit(newgame_box, newgame_rect)
    screen.blit(presskeymsg, keymsg_rect)
    