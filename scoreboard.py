import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():

    def __init__(self, aiSettings, screen, stats):
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.aiSettings = aiSettings
        self.stats = stats

        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.prepScore()
        self.prepHighScore()
        self.prepShips()

    def prepScore(self):

        roundedScore = int(round(self.stats.score, -1))
        scoreStr = str(roundedScore)
        self.scoreImage = self.font.render(scoreStr, True, self.textColor, self.aiSettings.bgColor)

        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20

    def prepHighScore(self):

        highScore = int(round(self.stats.highScore, -1))
        highScoreStr = str(highScore)
        self.highScoreImage = self.font.render(highScoreStr, True, self.textColor, self.aiSettings.bgColor) 

        self.highScoreRect = self.highScoreImage.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = self.screenRect.top + 20

    def prepShips(self):

        self.ships = Group()
        for shipNumber in range(self.stats.shipsLeft):
            ship = Ship(self.aiSettings, self.screen)
            ship.rect.x = 10 + shipNumber * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def showScore(self):
        
        self.screen.blit(self.scoreImage, self.scoreRect)
        self.screen.blit(self.highScoreImage, self.highScoreRect)
        self.ships.draw(self.screen)