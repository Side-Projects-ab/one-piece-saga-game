#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit

"""
https://www.pygame.org/docs/ref/image.html#pygame.image.load
"""


def draw_character_movement(screen: pygame.Surface, character: pygame.Surface):
    x, y = pygame.mouse.get_pos()
    x -= character.get_width() / 2
    y -= character.get_height() / 2
    screen.blit(character, (x, y))


def create_character(file_path: str,
                     character_ratio: float,
                     background: pygame.Surface) -> pygame.Surface:
    """
    Creates a character and do the necessary transformations.
    :param background:
    :param file_path:
    :param character_ratio:
    :return:
    """
    # Add a level of transparency to the character
    character = pygame.image.load(file_path).convert_alpha()

    # Transform the character to the appropriate size
    character = pygame.transform.scale(character,
                                       (int(character_ratio * background.get_width()),
                                        int(character_ratio * background.get_height())))

    return character

def main():
    # Initialize image properties
    background_image = "background_level_1.jpg"
    main_character_image = "luffy_character.png"
    side_character_image = "zoro_character.jpg"
    ground_image = "ground.png"

    # Initialize all imported pygame modules
    pygame.init()

    # Size tuple
    size_screen = (800, 500)

    # Initialize the screen
    # https://stackoverflow.com/questions/19695653/flags-and-depth-in-coding-pygame
    screen = pygame.display.set_mode(size = size_screen, flags = 0, depth = 32)
    pygame.display.set_caption("One Piece-Level 1")

    # Load the pygame background image and creates a copy.
    background = pygame.image.load(background_image).convert()

    # Add the character ratio
    ratio = 0.1

    main_character = create_character(
        file_path = main_character_image,
        character_ratio = ratio,
        background = background
    )

    second_character = create_character(
        file_path = side_character_image,
        character_ratio = ratio,
        background = background
    )

    ground_obj = create_character(
        file_path = ground_image,
        character_ratio = 1.0,
        background = background
    )

    ground = {"width": 0, "height": screen.get_height()-20}

    # Draws the background on the screen
    screen.blit(background, (0, 0))

    screen.blit(
        main_character,
        (0, (screen.get_height() - main_character.get_height()))
    )

    screen.blit(
        second_character,
        (screen.get_width() - second_character.get_width(),
         (screen.get_height() - second_character.get_height()))
    )

    # Infinite loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            # Draws the background on the screen
            screen.blit(background, (0, 0))

            # Draw the ground on the screen
            screen.blit(ground_obj, (ground["width"], ground["height"]))

            # Move main character
            # draw_character_movement(screen = screen, character = main_character)

            # Move side character
            # draw_character_movement(screen = screen, character = second_character)

            pygame.display.update()


if __name__ == "__main__":
    main()
