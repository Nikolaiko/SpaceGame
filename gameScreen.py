import pygame
import Сonstants

from spaceship import Spaceship
from bullet import Bullet
from enemyShip import EnemyShip

class GameScreen:
    myfont = None
    screenTitle = None
    pygameLib = None
    window = None
    screenSize = None
    gameHero = None
    allBullets = []
    enemyShips = []

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

        for i in range(0, 3):
            enemy = EnemyShip()
            enemy.image = pygame.image.load(enemy.imagePath).convert_alpha()
            enemy.x = (enemy.imageWidth * i) + 5
            enemy.y = 50
            self.enemyShips.append(enemy)

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

        for currentEvent in eventsList:
            if currentEvent.type == pygame.KEYDOWN:
                if currentEvent.key == pygame.K_SPACE:
                    newBullet = Bullet()
                    newBullet.x = self.gameHero.x + (self.gameHero.imageWidth / 2) - (newBullet.width / 2)
                    newBullet.y = self.gameHero.y - newBullet.heigth
                    newBullet.image = pygame.image.load(newBullet.imagePath)
                    self.allBullets.append(newBullet)

        for currentBullet in self.allBullets:
            currentBullet.y = currentBullet.y - currentBullet.speed

        conditions = filter(lambda bullet : bullet.y > -bullet.heigth, self.allBullets)
        self.allBullets = list(conditions)

        self.window.blit(self.screenTitle, (0, 0))
        self.window.blit(self.gameHero.image, (self.gameHero.x, self.gameHero.y))
        for currentBullet in self.allBullets:
            self.window.blit(currentBullet.image, (currentBullet.x, currentBullet.y))


        lastEnemy = self.enemyShips[-1]
        firstEnemy = self.enemyShips[0]
        needToReverse = False
        if (lastEnemy.x + lastEnemy.imageWidth + lastEnemy.speed >= self.screenSize[0] or
            firstEnemy.x + lastEnemy.speed <= 0):
            needToReverse = True


        for currentEnemy in self.enemyShips:
            if (needToReverse):
                currentEnemy.reverse()

            currentEnemy.move()
            self.window.blit(currentEnemy.image, (currentEnemy.x, currentEnemy.y))

        return returnValue
