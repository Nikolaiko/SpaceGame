import pygame
import Сonstants

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
    if drawResult == Сonstants.MAIN_SCREEN:
        currentScreen = MainScreen(pygame, screenSurface)
    elif drawResult == Сonstants.GAME_SCREEN_ID:
        currentScreen = GameScreen(pygame, screenSurface)
    elif drawResult == 3:
        currentScreen = EndScreen(pygame, screenSurface)
    elif drawResult == Сonstants.EXIT_GAME:
        gameIsOn = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
