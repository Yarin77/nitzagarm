import pygame
from constants import *
from Post import Post
from helpers import screen, from_text_to_array
from Filter import Filter


class ImagePost(Post):
    def __init__(self, image, username, location, description, filter=None):
        super().__init__(username, location, description)
        self.image = image
        self.filter = filter

    def display(self, start_comment):
        img = pygame.image.load(self.image)
        img = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))
        screen.blit(img, (POST_X_POS, POST_Y_POS))

        if self.filter:
            self.filter.apply_filter()
        font = pygame.font.SysFont(FONT_NAME, UI_FONT_SIZE)
        text_user = font.render(self.username, True, (0, 0, 0))
        screen.blit(text_user, (USER_NAME_X_POS, USER_NAME_Y_POS))

        text_loc = font.render(self.location, True, (0, 0, 0))
        screen.blit(text_loc, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        text_desc = font.render(self.description, True, BLACK)
        screen.blit(text_desc, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

        text_like = font.render(str(self.likes_counter), True, (0, 0, 0))
        screen.blit(text_like, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

        self.display_comments(start_comment)
