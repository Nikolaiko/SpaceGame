import pygame
from mainScreen import MainScreen
from gameScreen import GameScreen
from endGameScreen import EndScreen

MAIN_WINDOW_WIDTH = 600
MAIN_WINDOW_HEIGHT = 400
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)

pygame.init()

drawResult = 0
gameIsOn = True
clock = pygame.time.Clock()
screenSurface = pygame.display.set_mode((MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT))
currentScreen = MainScreen(pygame, screenSurface)

while gameIsOn == True:

    systemEvents = pygame.event.get()
    for event in systemEvents:
        if event.type == pygame.QUIT:
            gameIsOn = False

    screenSurface.fill(BACKGROUND_COLOR)

    drawResult = currentScreen.draw(systemEvents)
    if drawResult == 1:
        currentScreen = MainScreen(pygame, screenSurface)
    elif drawResult == 2:
        currentScreen = GameScreen(pygame, screenSurface)
    elif drawResult == 3:
        currentScreen = EndScreen(pygame, screenSurface)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
