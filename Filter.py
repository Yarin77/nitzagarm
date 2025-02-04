from helpers import screen, from_text_to_array
import pygame
from constants import *
class Filter:

    def __init__(self, color, transparency_level):
        self.color = color
        self.transparency_level = transparency_level

    def apply_filter(self):
        surface = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        surface.set_alpha(self.transparency_level)
        surface.fill(self.color)
        screen.blit(surface, (POST_X_POS, POST_Y_POS))

    def set_filter(self, transparency_level):
        self.transparency_level = transparency_level



