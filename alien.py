# make imports
import pygame
from pygame.sprite import Sprite
from random import randrange

class Alien(Sprite):

    def __init__(self, aiSettings, screen):
        super().__init__()
        self.screen = screen
        self.aiSettings = aiSettings

        # setup the sprites
        sprites = ["/Users/linds/Desktop/will/Python Crash Course/pyGame/A1.bmp", "/Users/linds/Desktop/will/Python Crash Course/pyGame/A2.bmp", "/Users/linds/Desktop/will/Python Crash Course/pyGame/A3.bmp"]
        Index = randrange(0, 3)
        self.image = pygame.image.load(sprites[Index])
        self.rect = self.image.get_rect()

        # start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        # draw the alien to the screen
        self.screen.blit(self.image, self.rect)

    def checkEdges(self):
        screenRect = self.screen.get_rect()
        if self.rect.right >= screenRect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # move the alien to the right
        self.x += (self.aiSettings.alien_speed * self.aiSettings.fleetDirection)
        self.rect.x = self.x



