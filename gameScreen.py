import pygame
import Сonstants
from spaceship import Spaceship

class GameScreen:
    myfont = None
    screenTitle = None
    pygameLib = None
    window = None
    screenSize = None
    gameHero = None

    def __init__(self, pygameInstance, windowScreen):
        self.pygameLib = pygameInstance
        self.window = windowScreen
        self.screenSize = self.window.get_size()

        self.myfont = self.pygameLib.font.SysFont('Comic Sans MS', 30)
        self.screenTitle = self.myfont.render('Game Screen', False, (255, 0, 0))

        self.gameHero = Spaceship()
        self.gameHero.image = pygame.image.load(self.gameHero.imagePath).convert_alpha()
        self.gameHero.x = (self.screenSize[0] / 2) - (self.gameHero.imageWidth / 2)
        self.gameHero.y = self.screenSize[1] - self.gameHero.imageHeight

    def draw(self, eventsList):
        returnValue = Сonstants.NO_ACTION

        allKeys = pygame.key.get_pressed()
        if allKeys[pygame.K_LEFT]:
            self.gameHero.moveLeft()
        if allKeys[pygame.K_RIGHT]:
            self.gameHero.moveRight()

        if self.gameHero.x >= self.screenSize[0] - self.gameHero.imageWidth:
            self.gameHero.x = self.screenSize[0] - self.gameHero.imageWidth
        elif self. gameHero.x < 0:
            self.gameHero.x = 0


        self.window.blit(self.screenTitle, (0, 0))
        self.window.blit(self.gameHero.image, (self.gameHero.x, self.gameHero.y))

        return returnValue
