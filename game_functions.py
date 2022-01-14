# make imports
import sys
from telnetlib import SB
import time

import pygame
from bullet import Bullet
from alien import Alien

def check_events(ship, screen, bullets, aiSettings, playButton, stats, aliens):

        if stats.gameActive == False:
            pygame.mouse.set_visible(True) 

     # watch for keyboard and mouse inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # move the ship to the right
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True

                # move the ship to the left
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True

                #fire bullt
                elif event.key == pygame.K_SPACE and len(bullets) < aiSettings.bulletsAllowed:
                    fireBullets(aiSettings, screen, ship, bullets)

                #quit the game
                elif event.key == pygame.K_q:
                    sys.exit()

            elif event.type == pygame.KEYUP:
                
                #stop moving the ship
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                checkPlayButton(stats, playButton, mouseX, mouseY, aiSettings, screen, ship, aliens, bullets)

def checkPlayButton(stats, playButton, mouseX, mouseY, aiSettings, screen, ship, aliens, bullets):
    buttonCollide = playButton.rect.collidepoint(mouseX, mouseY)
    if buttonCollide and not stats.gameActive:
        pygame.mouse.set_visible(False)

        stats.resetStats()
        stats.gameActive = True

        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #create a new fleet and the ship
        createFleet(aiSettings, screen, aliens, ship)
        ship.centerShip()


def fireBullets(aiSettings, screen, ship, bullets):
    
    newBullet = Bullet(aiSettings, screen, ship)
    bullets.add(newBullet)

def update_screen(aiSettings, screen, ship, bullets, aliens, stats, playButton, sb):

     # redraw the screen during each pass through the loop
    screen.fill(aiSettings.bgColor)
    ship.blitme()
    aliens.draw(screen)
    sb.prepScore()
    sb.showScore()
    sb.prepHighScore()
    sb.prepShips()

    if not stats.gameActive:
        playButton.drawButton() 

    for bullet in bullets.sprites():
        bullet.drawBullet()

    # make the most recently drawn screen visible
    pygame.display.flip()

def shipHit(aiSettings, stats, screen, ship, aliens, bullets):

    if stats.shipsLeft > 0:
        stats.shipsLeft -= 1

        aliens.empty()
        bullets.empty()

        createFleet(aiSettings, screen, aliens, ship)
        ship.centerShip()

        time.sleep(0.5)
    else:
        stats.gameActive = False
        pygame.mouse.set_visible(True)

def destroy(bullets, aliens, aiSettings, ship, screen, stats, sb):
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            else:
                checkBulletAlienCollision(aiSettings, screen, ship, aliens, bullets, stats, sb)
        
        if len(aliens) == 0:
            aiSettings.increaseSpeed()
            bullets.empty()
            createFleet(aiSettings, screen, aliens, ship)

def checkBulletAlienCollision(aiSettings, screen, ship, aliens, bullets, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += aiSettings.alienPoints * len(aliens)
        checkHighScore(stats, sb)

def checkHighScore(stats, sb):

    if stats.score > stats.highScore:
        stats.highScore = stats.score

def getNumberAliens(aiSettings, alienWidth):
    availableSpaceX = aiSettings.screen_width - 2 * alienWidth
    numberAliensX = int(availableSpaceX / (2 * alienWidth))

    return numberAliensX

def getNumberRows(aiSettings, shipHeight, alienHeight):
    availableSpaceY = (aiSettings.screen_height - (3 * alienHeight) - shipHeight)
    numberRows = int(availableSpaceY / (2.5 * alienHeight))

    return numberRows

def createAlien(aiSettings, screen, aliens, alienNumber, rowNumber):

    # create and alien and place it in the row
    alien = Alien(aiSettings, screen)
    alienWidth = alien.rect.width
    alien.x = alienWidth + 2 * alienWidth * alienNumber
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
    aliens.add(alien)

def createFleet(aiSettings, screen, aliens, ship):
    # create a full fleet of aliens
    alien = Alien(aiSettings, screen)
    numberAliensX = getNumberAliens(aiSettings, alien.rect.width)
    numberRows = getNumberRows(aiSettings, ship.rect.height, alien.rect.height)


    # create the fleet
    for rowNumber in range(numberRows):
        for alienNumber in range(numberAliensX):
            createAlien(aiSettings, screen, aliens, alienNumber, rowNumber)

def checkFleetEdges(aiSettings, aliens):
    #check if the fleet is touching the edge
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(aiSettings, aliens)
            break

def changeFleetDirection(aiSettings, aliens):
    #drop the entire fleet and change the fleet's direction
    for alien in aliens.sprites():
        alien.rect.y += aiSettings.fleetDropSpeed
    aiSettings.fleetDirection *= -1


def updateAliens(aiSettings, aliens, ship, stats, screen, bullets):
    # update the position of all aliens
    checkFleetEdges(aiSettings, aliens)
    aliens.update()

    checkAliensBottom(aiSettings, stats, screen, ship, aliens, bullets)

    if pygame.sprite.spritecollideany(ship, aliens):
        shipHit(aiSettings, stats, screen, ship, aliens, bullets)

def checkAliensBottom(aiSettings, stats, screen, ship, aliens, bullets):
    screenRect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screenRect.bottom:
            shipHit(aiSettings, stats, screen, ship, aliens, bullets)
            break
            



