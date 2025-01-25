import pygame
from constants import *
from Post import Post
from helpers import screen, from_text_to_array



class ImagePost(Post):

    def __init__(self,image, username, location, description):
        super().__init__(username, location, description)
        self.image = image


    def display(self, start_comment):
        img = pygame.image.load(self.image)
        img =pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))
        screen.blit(img, (POST_X_POS, POST_Y_POS))

        font = pygame.font.SysFont(FONT_NAME, UI_FONT_SIZE)
        text_user = font.render(self.username, True, (0, 0, 0))
        screen.blit(text_user, (USER_NAME_X_POS, USER_NAME_Y_POS))

        text_loc = font.render(self.location, True, (0, 0, 0))
        screen.blit(text_loc, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        # array_desc = from_text_to_array(self.description)
        # count = 0
        # pos_y = DESCRIPTION_TEXT_Y_POS
        # for item in array_desc:
        #     count += 1
        #     desc_post = font.render(item, True, BLACK)
        #     screen.blit(desc_post, (DESCRIPTION_TEXT_X_POS, pos_y))
        #     pos_y += UI_FONT_SIZE

        text_desc = font.render(self.description, True, BLACK)
        screen.blit(text_desc, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

        text_like = font.render(str(self.likes_counter), True, (0, 0, 0))
        screen.blit(text_like, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

        self.display_comments(start_comment)

