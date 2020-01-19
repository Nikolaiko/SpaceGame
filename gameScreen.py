import pygame

class GameScreen:
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
        self.screenTitle = self.myfont.render('Game Screen', False, (255, 0, 0))

    def draw(self, eventsList):
        returnValue = 0

        for currentEvent in eventsList:
            if currentEvent.type == self.pygameLib.KEYDOWN:
                if currentEvent.key == self.pygameLib.K_LEFT:
                    returnValue = 1
                elif currentEvent.key == self.pygameLib.K_RIGHT:
                    returnValue = 3

        self.window.blit(self.screenTitle, (0, 0))

        return returnValue
