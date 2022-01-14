# make imports
import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
import game_functions as gf
from scoreboard import Scoreboard

def run_game():
    # initialize the game and create a screen object
    pygame.init()
    aiSettings = Settings()
    screen = pygame.display.set_mode((aiSettings.screen_width, aiSettings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(aiSettings)
    sb = Scoreboard(aiSettings, screen, stats)

    ship = Ship(aiSettings, screen)
    alien = Alien(aiSettings, screen)
    bullets = Group()
    aliens = Group()
    playButton = Button(aiSettings, screen, "Play")

    # create the fleet of aliens
    gf.createFleet(aiSettings, screen, aliens, ship)

    # start the main loop for the game
    while True:

        gf.check_events(ship, screen, bullets, aiSettings, playButton, stats, aliens)

        if stats.gameActive:
            if stats.shipsLeft > 0:
                
                ship.update()
                bullets.update()
                gf.updateAliens(aiSettings, aliens, ship, stats, screen, bullets)
                gf.destroy(bullets, aliens, aiSettings, ship, screen, stats, sb)
            else:
                stats.gameActive = False

        gf.update_screen(aiSettings, screen, ship, bullets, aliens, stats, playButton, sb)
        
        

if __name__ == "__main__":
    run_game()