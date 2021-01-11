import pygame
import pygame.freetype

#font colors (rgb)
BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

def textbox(text, fontsize, text_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Consolas", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()