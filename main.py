import pygame
from buttons import like_button, click_post_button, comment_button, view_more_comments_button
from helpers import screen, mouse_in_button
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, img1_post_path, img2_post_path, NUM_OF_COMMENTS_TO_DISPLAY, img3_post_path
from Post import Post
from ImagePost import ImagePost
from text_post import TextPost
from Comment import Comment


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    posts_data_list = [[img1_post_path, "noam_belkin", "The father land", "Isagi is legit NPC #MOVE!!!!", "image"],
                  [img2_post_path, "omerKorin1808", "beer sheva", "love the camel", "image"],
                  ["We must sign new Wingback! Dalot can't do the job for us!", "mashash", "Manchester", "i am gay", (255, 255, 0), (255, 0, 0), "text"],
                  [img3_post_path, "eitan_levi", "beer sheva", "after a quick goon session", "image"]]

    posts_list = []
    for post_data in posts_data_list:
        if post_data[-1] == "image":
            post = ImagePost(post_data[0], post_data[1], post_data[2], post_data[3])
        else:
            post = TextPost(post_data[0], post_data[1], post_data[2], post_data[3], post_data[4], post_data[5])
        posts_list.append(post)
    running = True
    cur_post = posts_list[0]
    cur_post_num = 0
    start_comment = 0
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mouse_in_button(like_button, pos):
                    cur_post.add_like()
                elif mouse_in_button(click_post_button, pos):
                    if cur_post_num < len(posts_list) - 1:
                        cur_post_num += 1
                    else:
                        cur_post_num = 0

                elif mouse_in_button(comment_button, pos):
                    cur_post.add_comment()

                elif mouse_in_button(view_more_comments_button, pos):
                    if start_comment >= len(cur_post.comments) - NUM_OF_COMMENTS_TO_DISPLAY:
                        start_comment = 0
                    else:
                        start_comment += NUM_OF_COMMENTS_TO_DISPLAY


        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        cur_post = posts_list[cur_post_num]
        cur_post.display(start_comment)

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
