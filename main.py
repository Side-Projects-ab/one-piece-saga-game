#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit

"""
https://www.pygame.org/docs/ref/image.html#pygame.image.load
"""


def create_character(file_path: str,
                     width_ratio: float,
                     height_ratio: float,
                     background: pygame.Surface) -> pygame.Surface:
    """
    Creates a character and do the necessary transformations.
    :param file_path:
    :param width_ratio:
    :param height_ratio:
    :param background:
    :return:
    """
    # Add a level of transparency to the character
    character = pygame.image.load(file_path).convert_alpha()

    # Transform the character to the appropriate size
    character = pygame.transform.scale(character,
                                       (int(width_ratio * background.get_width()),
                                        int(height_ratio * background.get_height())))

    return character


class Player(pygame.sprite.Sprite):
    def __init__(self, surface_object, keys, speed, boundaries = (0, 0)):
        super(Player, self).__init__()
        self.surf = surface_object
        self.rect = self.surf.get_rect()
        self.up = keys["Up"]
        self.down = keys["Down"]
        self.right = keys["Right"]
        self.left = keys["Left"]
        self.boundaries = boundaries
        self.speed = speed

    def update(self, pressed_keys):
        if pressed_keys[self.up]:
            self.rect.move_ip(0, -1 * self.speed)
        if pressed_keys[self.down]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[self.left]:
            self.rect.move_ip(-1 * self.speed, 0)
        if pressed_keys[self.right]:
            self.rect.move_ip(self.speed, 0)
        # If it is in the middle look in the other direction.
        if self.rect.x == self.boundaries[0] / 2:
            self.surf = pygame.transform.flip(self.surf, True, False)


def draw_character(screen: pygame.Surface, character: Player):
    screen.blit(character.surf, character.rect)


def main():
    # Initialize image properties
    background_image = "background_level_1.jpg"
    main_character_image = "Luffy2_character.png"
    side_character_image = "zoro_character.png"
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
    ratio_char = 0.1

    # Add the ground ratio
    ratio_ground_w = 0.8
    ratio_ground_h = 0.1

    main_character = create_character(
        file_path = main_character_image,
        width_ratio = ratio_char,
        height_ratio = ratio_char,
        background = background
    )

    second_character = create_character(
        file_path = side_character_image,
        width_ratio = ratio_char,
        height_ratio = ratio_char,
        background = background
    )

    ground_obj = create_character(
        file_path = ground_image,
        width_ratio = ratio_ground_w,
        height_ratio = ratio_ground_h,
        background = background
    )

    main_player = Player(
        surface_object = main_character,
        keys = {"Up": K_UP, "Down": K_DOWN, "Left": K_LEFT, "Right": K_RIGHT},
        speed = 20,
        boundaries = (screen.get_width(), screen.get_height())
    )

    side_player = Player(
        surface_object = second_character,
        keys = {"Up": K_w, "Down": K_s, "Left": K_a, "Right": K_d},
        speed = 20,
        boundaries = (screen.get_width(), screen.get_height())
    )

    ground = {"width": screen.get_width() / 8,
              "height": screen.get_height() - ground_obj.get_height()}

    main_player.rect.x, main_player.rect.y = ground["width"], \
                                             (
                                                     screen.get_height() - ground_obj.get_height() -
                                                     main_character.get_height()
                                             )
    side_player.rect.x, side_player.rect.y = (ground["width"] + ground_obj.get_width() -
                                              second_character.get_width()), \
                                             (
                                                     screen.get_height() - ground_obj.get_height() -
                                                     second_character.get_height()
                                             )

    running = True

    # Infinite loop
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            pressed_keys = pygame.key.get_pressed()

            # Update the main player
            main_player.update(pressed_keys)

            # Update the second player
            side_player.update(pressed_keys)

            # Draws the background on the screen
            screen.blit(background, (0, 0))

            # Draw the ground on the screen
            screen.blit(ground_obj, (ground["width"], ground["height"]))

            # Move main character
            draw_character(screen = screen, character = main_player)

            # Move side character
            draw_character(screen = screen, character = side_player)

            pygame.display.update()


if __name__ == "__main__":
    main()
