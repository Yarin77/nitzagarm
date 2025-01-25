import pygame

from constants import *
from helpers import screen


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

    def add_comment(self, comment):
        self.comments.append(comment)

    def display(self):
        pass


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = 0
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def from_text_to_array(self, text):
        """
        the function get text and break it into sentences that fits the screen, in
        case the text too long to for one line
        :param text: string
            text to show on screen
        :return: list of sentences
        """
        text_array = []
        text_to_edit = text
        if len(text) > 20:
            while not (len(text_to_edit) <= 0):
                if len(text_to_edit) < LINE_MAX_LENGTH:
                    text_array.append(text_to_edit)
                    text_to_edit = ""
                else:
                    temp = text_to_edit[0: LINE_MAX_LENGTH]
                    text_to_edit = text_to_edit[LINE_MAX_LENGTH:]
                    while not (temp[-1] == ' ') and not (temp[-1] == ','):
                        text_to_edit = temp[-1] + text_to_edit
                        temp_len = int(len(temp))
                        temp = temp[0: temp_len - 1]
                    text_array.append(temp)
        else:
            text_array.append(text)
        return text_array

    def center_text(self, num_of_rows, text_to_display, row_number):
        """
        center a sentence on screen
        :param num_of_rows: int
            number of sentences on screen
        :param text_to_display: string
            sentence to center
        :param row_number: int
            sentence row number in total text
        :return: tuple
            position of centered text
        """
        horizontal_margin = \
            (POST_HEIGHT - num_of_rows * TEXT_POST_FONT_SIZE) // 2
        # Get the text object size (height and width)
        text_rect = text_to_display.get_rect()
        # Center the text to the center of X axis
        text_rect.x = ((POST_WIDTH - text_rect.width) // 2) + 20
        # Center the text to the center of the post on Y axis
        text_rect.y = (POST_Y_POS + horizontal_margin +
                       row_number * TEXT_POST_FONT_SIZE)
        return text_rect