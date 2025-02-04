import pygame
import pywhatkit
from constants import *
from helpers import screen, from_text_to_array, center_text
from Post import Post

class TextPost(Post):
    def __init__(self, text, username, location, description, text_color, background_color):
        super().__init__(username, location, description)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color

    def share(self, phone_num):
        msg = self.text + " \n " + self.description
        pywhatkit.sendwhatmsg_instantly(phone_num, msg)

    def display(self, start_comment):
        rect = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, rect)

        font1 = pygame.font.SysFont(FONT_NAME, TEXT_POST_FONT_SIZE)
        array_text = from_text_to_array(self.text)
        count = 0
        for item in array_text:
            count += 1
            text_post = font1.render(item, True, self.text_color)
            pos = center_text(len(array_text), text_post, count)
            screen.blit(text_post, pos)

        font2 = pygame.font.SysFont(FONT_NAME, UI_FONT_SIZE)
        text_user = font2.render(self.username, True, BLACK)
        screen.blit(text_user, [USER_NAME_X_POS, USER_NAME_Y_POS])

        text_loc = font2.render(self.location, True, BLACK)
        screen.blit(text_loc, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

        text_like = font2.render(str(self.likes_counter), True, BLACK)
        screen.blit(text_like, [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS])

        # array_desc = from_text_to_array(self.description)
        # count = 0
        # pos_y = DESCRIPTION_TEXT_Y_POS
        # for item in array_desc:
        #     count += 1
        #     desc_post = font2.render(item, True, BLACK)
        #     screen.blit(desc_post, (DESCRIPTION_TEXT_X_POS, pos_y))
        #     pos_y += UI_FONT_SIZE

        text_desc = font2.render(self.description, True, BLACK)
        screen.blit(text_desc, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

        self.display_comments(start_comment)




