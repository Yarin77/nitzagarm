import pygame

from constants import *
from helpers import screen, read_comment_from_user
from Comment import Comment


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self):
        self.comments.append(read_comment_from_user())

    def display(self, start_comment):
        pass

    def share(self, phonum):
        pass


    def display_comments(self, start_comment):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = start_comment
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        font = pygame.font.SysFont(FONT_NAME, UI_FONT_SIZE)
        pos_x_comment = FIRST_COMMENT_X_POS
        pos_y_comment = FIRST_COMMENT_Y_POS
        for i in range(start_comment, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            comment_text = font.render(self.comments[position_index], True, BLACK)
            screen.blit(comment_text, [pos_x_comment, pos_y_comment])
            pos_y_comment += COMMENT_TEXT_SIZE
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1 + start_comment:
                break

