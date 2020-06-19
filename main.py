#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit

"""
https://www.pygame.org/docs/ref/image.html#pygame.image.load
"""

if __name__ == "__main__":
    # Initialize image properties
    background_image = "background_level_1.jpg"
    main_character_image = "luffy_character.png"

    # Initialize all imported pygame modules
    pygame.init()

    # Size tuple
    size_screen = (800, 500)

    # Initialize the screen
    # https://stackoverflow.com/questions/19695653/flags-and-depth-in-coding-pygame
    screen = pygame.display.set_mode(size=size_screen, flags=0, depth=32)
    pygame.display.set_caption("One Piece-Level 1")

    # Load the pygame background image and creates a copy.
    background = pygame.image.load(background_image).convert()
    # Add a level of transparency to the main character
    main_character = pygame.image.load(main_character_image).convert_alpha()

    # Infinite loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            # Draws the background on the screen
            screen.blit(background, (0, 0))

            x, y = pygame.mouse.get_pos()
            x -= main_character.get_width() / 2
            y -= main_character.get_height() / 2
            screen.blit(main_character, (x, y))

            pygame.display.update()
