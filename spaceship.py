class Spaceship:
    imageWidth = 60
    imageHeight = 60
    imagePath = "spaceship.png"
    image = None
    speed = 1.3
    x = 0
    y = 0

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveRight(self):
        self.x = self.x + self.speed
