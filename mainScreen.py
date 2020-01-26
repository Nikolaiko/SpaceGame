import pygame

class MainScreen:
    myfont = None
    screenTitle = None
    startLabel = None
    exitLabel = None
    pygameLib = None
    window = None
    screenSize = None
    screenTitlePosition = None
    startLabelPosition = None
    exitLabelPosition = None

    def __init__(self, pygameInstance, windowScreen):
        self.pygameLib = pygameInstance
        self.window = windowScreen
        self.screenSize = self.window.get_size()

        middleX = self.screenSize[0]  / 2
        middleY = self.screenSize[1] / 2

        self.myfont = self.pygameLib.font.SysFont('Comic Sans MS', 30)
        self.screenTitle = self.myfont.render('Main Screen', False, (255, 0, 0))
        self.startLabel = self.myfont.render('Start Game', False, (255, 0, 0))
        self.exitLabel = self.myfont.render('Exit Game', False, (255, 0, 0))

        self.screenTitlePosition = (middleX - self.screenTitle.get_size()[0] / 2, 5)
        self.startLabelPosition = (middleX  - self.startLabel.get_size()[0] / 2, middleY)
        self.exitLabelPosition = (middleX - self.exitLabel.get_size()[0] / 2, middleY + 40)

    def draw(self, eventsList):
        returnValue = 0

        for currentEvent in eventsList:
            if currentEvent.type == self.pygameLib.KEYDOWN:
                if currentEvent.key == self.pygameLib.K_LEFT:
                    returnValue = 3
                elif currentEvent.key == self.pygameLib.K_RIGHT:
                    returnValue = 2

        self.window.blit(self.screenTitle, self.screenTitlePosition)
        self.window.blit(self.startLabel, self.startLabelPosition)
        self.window.blit(self.exitLabel, self.exitLabelPosition)

        return returnValue
