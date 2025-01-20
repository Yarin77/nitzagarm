import pygame
from constants import *
from helpers import screen


class text_post:
    def __init__(self,username, location, description, text, text_color, background_color):
        super().__init__(username, location, description)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color

    def display(self):
        font1 = pygame.font.SysFont(FONT_NAME, TEXT_POST_FONT_SIZE)
        text = font1.render(self.text, True, BLACK)
        screen.blit(text, [POST_X_POS, POST_Y_POS])

        font2 = pygame.font.SysFont(FONT_NAME, UI_FONT_SIZE)
        text = font2.render(self.text, True, BLACK)
        screen.blit(text, [USER_NAME_X_POS, USER_NAME_Y_POS])

        text = font2.render(self.text, True, BLACK)
        screen.blit(text, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

        text = font2.render(self.text, True, BLACK)
        screen.blit(text, [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS])

        text = font2.render(self.text, True, BLACK)
        screen.blit(text, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])





