import os, contextlib

# Suppress the "Hello from the pygame community" message
with contextlib.redirect_stdout(None):
    import pygame

import sys, pywinstyles


def main():
    pygame.init()

    # -- Constants -- #
    WIDTH, HEIGHT = 1280, 720
    CENTER_X, CENTER_Y = WIDTH / 2, HEIGHT / 2

    # -- Display Setup -- #
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame")

    # Set Windows title bar to black
    try:
        pywinstyles.change_header_color(screen, "black")
    except:
        # Fallback for non-Windows systems
        pass

    FPS = 60
    clock = pygame.time.Clock()

    running = True
    while running:
        # -- Event Handling -- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # -- Rendering -- #
        screen.fill("black")

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
