import pygame
import Сonstants

class EndScreen:
    myfont = None
    screenTitle = None
    pygameLib = None
    window = None
    screenSize = None

    def __init__(self, pygameInstance, windowScreen):
        self.pygameLib = pygameInstance
        self.window = windowScreen
        self.screenSize = self.window.get_size()

        self.myfont = self.pygameLib.font.SysFont('Comic Sans MS', 30)
        self.screenTitle = self.myfont.render('End Screen', False, (255, 0, 0))

    def draw(self, eventsList):
        returnValue = 0

        for currentEvent in eventsList:
            if currentEvent.type == self.pygameLib.KEYDOWN:
                returnValue = Сonstants.EXIT_GAME

        self.window.blit(self.screenTitle, (0, 0))

        return returnValue
