class GameStats():

    def __init__(self, aiSettings):
        self.aiSettings = aiSettings
        self.resetStats()
        self.gameActive = False
        self.score = 0
        self.highScore = 0

    def resetStats(self):
        self.shipsLeft = self.aiSettings.shipLimit
        self.score = 0