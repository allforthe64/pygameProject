# create the Settings class
class Settings():

    def __init__(self):
        #initialize the game's settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bgColor = (6, 5, 38)

        #ship settings
        self.ship_speed_factor = 1
        self.shipLimit = 3

        #bullet settings
        self.bulletSpeed = 1
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = (255, 255, 255)
        self.bulletsAllowed = 5

        #alien settings
        self.alien_speed = 1
        self.fleetDropSpeed = 10
        #fleet direction of 1 represents right and direction of -1 represents left
        self.fleetDirection = 1
        self.alienPoints = 50

        self.speedUpScale = 1.1
        self.pointsBonus = 1.5

    def initializeDynamicSettings(self):

        self.alien_speed = 1
        self.fleetDirection = 1
        self.alienPoints = 50

    def increaseSpeed(self):
        self.alien_speed *= self.speedUpScale
        self.alienPoints *= self.pointsBonus
        