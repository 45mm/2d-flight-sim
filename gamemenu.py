import pygame
import pygame.freetype


#font colors (rgb)
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

bigfont = pygame.font.Font(None, 80)
smallfont = pygame.font.Font(None, 45)

def play_again(self, screen, ht, wt):
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

    pygame.display.flip()
    in_main_menu = True
    while in_main_menu:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x >= textx - 5 and x <= textx + textx_size + 5:
                    if y >= texty - 5 and y <= texty + texty_size + 5:
                        in_main_menu = False
                        #player.RESTART_NEEDED = True
                        break

'''def newgame(text, fontsize, text_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Consolas", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()'''