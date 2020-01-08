import pygame

MAIN_WINDOW_WIDTH = 600
MAIN_WINDOW_HEIGHT = 400
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)

pygame.init()

gameIsOn = True
clock = pygame.time.Clock()
screenSurface = pygame.display.set_mode((MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT))

while gameIsOn == True:

    systemEvents = pygame.event.get()
    for event in systemEvents:
        if event.type == pygame.QUIT:
            gameIsOn = False

    screenSurface.fill(BACKGROUND_COLOR)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
