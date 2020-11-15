class EnemyShip:
    direction = 1
    imageWidth = 60
    imageHeight = 60
    imagePath = "enemy_ship.png"
    image = None
    speed = 2.0
    x = 0
    y = 0

    def move(self):
        self.x = self.x + (self.speed * self.direction)

    def reverse(self):
        self.direction *= -1
