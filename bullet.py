import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, aiSettings, screen, ship):

        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, aiSettings.bulletWidth, aiSettings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = aiSettings.bulletColor
        self.speed = aiSettings.bulletSpeed

    def update(self):

        self.y -= self.speed
        self.rect.y = self.y

    def drawBullet(self):

        pygame.draw.rect(self.screen, self.color, self.rect)
