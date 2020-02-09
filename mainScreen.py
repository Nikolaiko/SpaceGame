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

    middleX = None
    middleY = None

    selectedIndex = 0
    selectedColor = (0, 255, 0)
    unselectedColor = (255, 0, 0)

    def __init__(self, pygameInstance, windowScreen):
        self.pygameLib = pygameInstance
        self.window = windowScreen
        self.screenSize = self.window.get_size()

        self.middleX = self.screenSize[0]  / 2
        self.middleY = self.screenSize[1] / 2

        self.myfont = self.pygameLib.font.SysFont('Comic Sans MS', 30)
        self.screenTitle = self.myfont.render('Main Screen', False, (255, 0, 0))
        self.screenTitlePosition = (self.middleX - self.screenTitle.get_size()[0] / 2, 5)

    def draw(self, eventsList):
        returnValue = 0

        for currentEvent in eventsList:
            if currentEvent.type == self.pygameLib.KEYDOWN:
                if currentEvent.key == self.pygameLib.K_DOWN:
                    self.selectedIndex = min(1, self.selectedIndex + 1)
                elif currentEvent.key == self.pygameLib.K_UP:
                    self.selectedIndex = max(0, self.selectedIndex - 1)

        if (self.selectedIndex == 0):
            self.startLabel = self.myfont.render('Start Game', False, self.selectedColor)
            self.exitLabel = self.myfont.render('Exit Game', False, self.unselectedColor)
        elif (self.selectedIndex == 1):
            self.startLabel = self.myfont.render('Start Game', False, self.unselectedColor)
            self.exitLabel = self.myfont.render('Exit Game', False, self.selectedColor)

        self.startLabelPosition = (self.middleX  - self.startLabel.get_size()[0] / 2, self.middleY)
        self.exitLabelPosition = (self.middleX - self.exitLabel.get_size()[0] / 2, self.middleY + 40)

        self.window.blit(self.screenTitle, self.screenTitlePosition)
        self.window.blit(self.startLabel, self.startLabelPosition)
        self.window.blit(self.exitLabel, self.exitLabelPosition)

        return returnValue
