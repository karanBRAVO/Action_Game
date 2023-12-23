# import statements
import pygame
import random
from pygame import transform
from pygame.locals import *
import time

# initializing pygame
pygame.init()

# setting fps clock
clock = pygame.time.Clock()

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

# Setting window
windowWidth = 350
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Space Shuttle")
print("*** Space Shuttle ***")
print("press Space_key to fire...")

# variable used
font1 = pygame.font.SysFont('monospace', 40, True, False)
font2 = pygame.font.SysFont('fantasy', 40, True, False)
message1 = font1.render('Starting in 3', True, white)
message2 = font1.render('Starting in 2', True, white)
message3 = font1.render('Starting in 1', True, white)
message4 = font1.render('Game Over', True, yellow)
message5 = font2.render('Space Shuttle', True, yellow)
messageRect = message1.get_rect()
message2Rect = message4.get_rect()
message3Rect = message5.get_rect()
messageRect.center = (windowWidth // 2, windowHeight // 2)
message2Rect.center = ((windowWidth // 2) + 10, windowHeight // 2)
message3Rect.center = (170, 170)
fps = 60
bulletWidth = 5
bulletHeight = 6
Assets = {
    'bg': transform.scale(pygame.image.load("img/spaceAssets/bg.webp"), (windowWidth, windowHeight)),
    'enemy1': pygame.image.load("img/spaceAssets/enemy1.png"),
    'enemy1Bullet1': transform.scale(pygame.image.load("img/spaceAssets/enemy1Bullet.png"),
                                     (bulletWidth, bulletHeight)),
    'enemy1Bullet2': transform.scale(pygame.image.load("img/spaceAssets/enemy1Bullet.png"),
                                     (bulletWidth, bulletHeight)),
    'enemy2': pygame.image.load("img/spaceAssets/enemy2.png"),
    'enemy2Bullet1': transform.scale(pygame.image.load("img/spaceAssets/enemy2Bullet.png"),
                                     (bulletWidth, bulletHeight)),
    'enemy2Bullet2': transform.scale(pygame.image.load("img/spaceAssets/enemy2Bullet.png"),
                                     (bulletWidth, bulletHeight)),
    'enemy3': pygame.image.load("img/spaceAssets/enemy3.png"),
    'enemy3Bullet1': transform.scale(pygame.image.load("img/spaceAssets/enemy3Bullet.png"),
                                     (bulletWidth, bulletHeight)),
    'enemy3Bullet2': transform.scale(pygame.image.load("img/spaceAssets/enemy3Bullet.png"),
                                     (bulletWidth, bulletHeight)),
    'player': pygame.image.load("img/spaceAssets/player.png"),
    'playerBullet': transform.scale(pygame.image.load("img/spaceAssets/playerBullet.png"),
                                    (bulletWidth, 15)),
}

enemy1Rect = pygame.Rect(10, -20, 41, 33)
enemy1Bullet1Rect = pygame.Rect(29, enemy1Rect.y + 13, bulletWidth, bulletHeight)
enemy1Bullet2Rect = pygame.Rect(29, enemy1Rect.y - 13, bulletWidth, bulletHeight)

enemy2Rect = pygame.Rect(100, -60, 37, 29)
enemy2Bullet1Rect = pygame.Rect(117, enemy2Rect.y + 13, bulletWidth, bulletHeight)
enemy2Bullet2Rect = pygame.Rect(117, enemy2Rect.y - 13, bulletWidth, bulletHeight)

enemy3Rect = pygame.Rect(200, -10, 40, 32)
enemy3Bullet1Rect = pygame.Rect(217, enemy3Rect.y + 13, bulletWidth, bulletHeight)
enemy3Bullet2Rect = pygame.Rect(217, enemy3Rect.y - 13, bulletWidth, bulletHeight)

playerRect = pygame.Rect(145, 427, 57, 60)
playerBulletRect = pygame.Rect(171, 455, bulletWidth, 15)

# detecting hit
playerHitRect = pygame.Rect(145, 427, 57, 2)
enemy1HitRect = pygame.Rect(12, -25, 38, 3)
enemy2HitRect = pygame.Rect(100, -65, 38, 3)
enemy3HitRect = pygame.Rect(202, -15, 38, 3)

# setting health rect
playerHealthRect = pygame.Rect(149, 488, 50, 5)
enemy1HealthRect = pygame.Rect(12, -25, 38, 3)
enemy2HealthRect = pygame.Rect(100, -65, 38, 3)
enemy3HealthRect = pygame.Rect(202, -15, 38, 3)

# decreasing health variables
decPlayerHealth = 1
decEnemyHealth = 19

# setting the velocities
enemy_yVel = 1
enemyBullet_yVel = 5
player_xVel = 10
playerBullet_yVel = 20

# setting game started to true
run = True

Time = 3
lives = 5

# lives rect
live1Rect = pygame.Rect(10, 470, 8, 10)
live2Rect = pygame.Rect(20, 470, 8, 10)
live3Rect = pygame.Rect(30, 470, 8, 10)
live4Rect = pygame.Rect(40, 470, 8, 10)
live5Rect = pygame.Rect(50, 470, 8, 10)


# Main functioning of game
def mainLoop():
    # setting global variables
    global run, player_xVel, playerRect, enemy1Rect, enemy2Rect, enemy3Rect, enemy1Bullet1Rect, enemy1Bullet2Rect, \
        enemy2Bullet1Rect, enemy2Bullet2Rect, enemy3Bullet1Rect, enemy3Bullet2Rect, playerBulletRect, \
        playerBullet_yVel, Time, enemyBullet_yVel, enemy_yVel, playerHealthRect, enemy1HealthRect, enemy2HealthRect, \
        enemy3HealthRect, decPlayerHealth, playerHitRect, enemy3HitRect, enemy2HitRect, enemy1HitRect, lives, \
        live1Rect, live2Rect, live3Rect, live4Rect, live5Rect

    # Giving time before to start the game
    if Time == 3:
        window.fill(black)
        window.blit(message5, message3Rect)
        window.blit(message1, messageRect)
        Time = 2
    pygame.display.flip()
    pygame.event.pump()
    time.sleep(1)
    if Time == 2:
        window.fill(black)
        window.blit(message5, message3Rect)
        window.blit(message2, messageRect)
        Time = 1
    pygame.display.flip()
    pygame.event.pump()
    time.sleep(1)
    if Time == 1:
        window.fill(black)
        window.blit(message5, message3Rect)
        window.blit(message3, messageRect)
    pygame.display.flip()
    pygame.event.pump()
    time.sleep(1)

    # some more variables
    shoot = 0
    score = 0
    # enemy = [enemy1Rect, enemy2Rect, enemy3Rect]
    # enemy_health = [enemy1HealthRect, enemy2HealthRect, enemy3HealthRect]
    # enemy_hit = [enemy1HitRect, enemy2HitRect, enemy3HitRect]
    enemyBullets = [enemy1Bullet1Rect, enemy1Bullet2Rect, enemy2Bullet1Rect, enemy2Bullet2Rect, enemy3Bullet1Rect,
                    enemy3Bullet2Rect]

    # infinite loop till someone closes the game
    while run:
        # Blitting the background
        window.blit(Assets['bg'], (0, 0))

        # taking user events
        for event in pygame.event.get():
            # for closing the game
            if event.type == QUIT:
                run = False
                print("Score: ", score)
            if event.type == KEYDOWN and (event.key == K_ESCAPE):
                run = False
                print("Score: ", score)

            # movements of main player
            if event.type == KEYDOWN and (event.key == K_LEFT):
                playerRect.x -= player_xVel
                playerHitRect.x -= player_xVel
                playerHealthRect.x -= player_xVel
                if shoot == 0:
                    playerBulletRect.x -= player_xVel
            if event.type == KEYDOWN and (event.key == K_RIGHT):
                playerRect.x += player_xVel
                playerHealthRect.x += player_xVel
                playerHitRect.x += player_xVel
                if shoot == 0:
                    playerBulletRect.x += player_xVel
            if event.type == KEYDOWN and (event.key == K_SPACE):
                shoot = 1

        # player left and right boundary line
        if playerRect.x <= 0:
            playerRect.x += player_xVel
            playerHealthRect.x += player_xVel
            playerHitRect.x += player_xVel
            if shoot == 0:
                playerBulletRect.x += player_xVel
        if playerRect.x >= 295:
            playerRect.x -= player_xVel
            playerHealthRect.x -= player_xVel
            playerHitRect.x -= player_xVel
            if shoot == 0:
                playerBulletRect.x -= player_xVel

        # shooting the bullet
        if shoot == 1:
            playerBulletRect.y -= playerBullet_yVel

        # resetting the bullet position
        if playerBulletRect.y < 0:
            shoot = 0
            playerBulletRect.y = playerRect.y + 25
            playerBulletRect.x = playerRect.x + 26

        # decreasing the player health bar
        for enemyBullet in enemyBullets:
            if enemyBullet.colliderect(playerHitRect):
                playerHealthRect.width -= decPlayerHealth

        # Checking player lives
        if playerHealthRect.width <= 0 and lives > 0:
            lives -= 1
            playerHealthRect.width = 50

        # Setting the enemies(3) into motion
        # enemy 1
        enemy1Rect.y += enemy_yVel
        enemy1HealthRect.y += enemy_yVel
        enemy1HitRect.y += enemy_yVel
        if 0 <= enemy1Rect.y < 427:
            enemy1Bullet1Rect.y += enemyBullet_yVel
            enemy1Bullet2Rect.y += enemyBullet_yVel
        if enemy1Rect.y >= windowHeight:
            lives -= 1
            enemy1Rect.y = -10
            enemy1HealthRect.y = -15
            enemy1HitRect.y = -10
            enemy1Bullet1Rect.y = enemy1Rect.y + 13
            enemy1Bullet2Rect.y = enemy1Rect.y - 13
            x = random.randint(0, 298)
            enemy1Rect.x = x
            enemy1HealthRect.x = x + 2
            enemy1HitRect.x = enemy1HealthRect.x
            enemy1Bullet1Rect.x = x + 19
            enemy1Bullet2Rect.x = x + 19
        if enemy1Bullet1Rect.y >= 650 and enemy1Rect.y < 400:
            enemy1Bullet1Rect.y = enemy1Rect.y + 13
            enemy1Bullet2Rect.y = enemy1Rect.y - 13

        # decreasing the enemy health bar
        if playerBulletRect.colliderect(enemy1HitRect):
            enemy1HealthRect.width -= decEnemyHealth
            shoot = 0
            playerBulletRect.x = playerRect.x + 26
            playerBulletRect.y = playerRect.y + 25

        if enemy1HealthRect.width <= 0:
            score += 1
            enemy1Rect.y = -10
            enemy1HealthRect.y = -15
            enemy1HealthRect.width = 38
            enemy1HitRect.y = -10
            enemy1Bullet1Rect.y = enemy1Rect.y + 13
            enemy1Bullet2Rect.y = enemy1Rect.y - 13
            x = random.randint(0, 298)
            enemy1Rect.x = x
            enemy1HealthRect.x = x + 2
            enemy1HitRect.x = enemy1HealthRect.x
            enemy1Bullet1Rect.x = x + 19
            enemy1Bullet2Rect.x = x + 19

        # enemy 2
        enemy2Rect.y += enemy_yVel
        enemy2HealthRect.y += enemy_yVel
        enemy2HitRect.y += enemy_yVel
        if 0 <= enemy2Rect.y < 427:
            enemy2Bullet1Rect.y += enemyBullet_yVel
            enemy2Bullet2Rect.y += enemyBullet_yVel
        if enemy2Rect.y >= windowHeight:
            lives -= 1
            enemy2Rect.y = -10
            enemy2HealthRect.y = -15
            enemy2HitRect.y = -10
            enemy2Bullet1Rect.y = enemy2Rect.y + 13
            enemy2Bullet2Rect.y = enemy2Rect.y - 13
            x = random.randint(0, 298)
            enemy2Rect.x = x
            enemy2HealthRect.x = x
            enemy2HitRect.x = enemy2HealthRect.x
            enemy2Bullet1Rect.x = x + 19
            enemy2Bullet2Rect.x = x + 19
        if enemy2Bullet1Rect.y >= 650 and enemy2Rect.y < 400:
            enemy2Bullet1Rect.y = enemy2Rect.y + 13
            enemy2Bullet2Rect.y = enemy2Rect.y - 13

        # decreasing the enemy health bar
        if playerBulletRect.colliderect(enemy2HitRect):
            enemy2HealthRect.width -= decEnemyHealth
            shoot = 0
            playerBulletRect.x = playerRect.x + 26
            playerBulletRect.y = playerRect.y + 25

        if enemy2HealthRect.width <= 0:
            score += 1
            enemy2Rect.y = -10
            enemy2HealthRect.y = -15
            enemy2HealthRect.width = 38
            enemy2HitRect.y = -10
            enemy2Bullet1Rect.y = enemy2Rect.y + 13
            enemy2Bullet2Rect.y = enemy2Rect.y - 13
            x = random.randint(0, 298)
            enemy2Rect.x = x
            enemy2HealthRect.x = x
            enemy2HitRect.x = enemy2HealthRect.x
            enemy2Bullet1Rect.x = x + 19
            enemy2Bullet2Rect.x = x + 19

        # enemy 3
        enemy3Rect.y += enemy_yVel
        enemy3HealthRect.y += enemy_yVel
        enemy3HitRect.y += enemy_yVel
        if 0 <= enemy3Rect.y < 427:
            enemy3Bullet1Rect.y += enemyBullet_yVel
            enemy3Bullet2Rect.y += enemyBullet_yVel
        if enemy3Rect.y >= windowHeight:
            lives -= 1
            enemy3Rect.y = -10
            enemy3HealthRect.y = -15
            enemy3HitRect.y = -10
            enemy3Bullet1Rect.y = enemy3Rect.y + 13
            enemy3Bullet2Rect.y = enemy3Rect.y - 13
            x = random.randint(0, 298)
            enemy3Rect.x = x
            enemy3HealthRect.x = x + 2
            enemy3HitRect.x = enemy3HealthRect.x
            enemy3Bullet1Rect.x = x + 19
            enemy3Bullet2Rect.x = x + 19
        if enemy3Bullet1Rect.y >= 650 and enemy3Rect.y < 400:
            enemy3Bullet1Rect.y = enemy3Rect.y + 13
            enemy3Bullet2Rect.y = enemy3Rect.y - 13

        # decreasing the enemy health bar
        if playerBulletRect.colliderect(enemy3HitRect):
            enemy3HealthRect.width -= decEnemyHealth
            shoot = 0
            playerBulletRect.x = playerRect.x + 26
            playerBulletRect.y = playerRect.y + 25

        if enemy3HealthRect.width <= 0:
            score += 1
            enemy3Rect.y = -10
            enemy3HealthRect.y = -15
            enemy3HealthRect.width = 38
            enemy3HitRect.y = -10
            enemy3Bullet1Rect.y = enemy3Rect.y + 13
            enemy3Bullet2Rect.y = enemy3Rect.y - 13
            x = random.randint(0, 298)
            enemy3Rect.x = x
            enemy3HealthRect.x = x + 2
            enemy3HitRect.x = enemy3HealthRect.x
            enemy3Bullet1Rect.x = x + 19
            enemy3Bullet2Rect.x = x + 19

        # collision between player and enemy
        if playerRect.colliderect(enemy1Rect):
            score -= 1
            enemy1Rect.y = -10
            enemy1HealthRect.y = -15
            enemy1HealthRect.width = 38
            enemy1HitRect.y = -10
            enemy1Bullet1Rect.y = enemy1Rect.y + 13
            enemy1Bullet2Rect.y = enemy1Rect.y - 13
            x = random.randint(0, 298)
            enemy1Rect.x = x
            enemy1HealthRect.x = x + 2
            enemy1HitRect.x = enemy1HealthRect.x
            enemy1Bullet1Rect.x = x + 19
            enemy1Bullet2Rect.x = x + 19
        if playerRect.colliderect(enemy2Rect):
            score -= 1
            enemy2Rect.y = -10
            enemy2HealthRect.y = -15
            enemy2HealthRect.width = 38
            enemy2HitRect.y = -10
            enemy2Bullet1Rect.y = enemy2Rect.y + 13
            enemy2Bullet2Rect.y = enemy2Rect.y - 13
            x = random.randint(0, 298)
            enemy2Rect.x = x
            enemy2HealthRect.x = x + 2
            enemy2HitRect.x = enemy2HealthRect.x
            enemy2Bullet1Rect.x = x + 19
            enemy2Bullet2Rect.x = x + 19
        if playerRect.colliderect(enemy3Rect):
            score -= 1
            enemy3Rect.y = -10
            enemy3HealthRect.y = -15
            enemy3HealthRect.width = 38
            enemy3HitRect.y = -10
            enemy3Bullet1Rect.y = enemy3Rect.y + 13
            enemy3Bullet2Rect.y = enemy3Rect.y - 13
            x = random.randint(0, 298)
            enemy3Rect.x = x
            enemy3HealthRect.x = x + 2
            enemy3HitRect.x = enemy3HealthRect.x
            enemy3Bullet1Rect.x = x + 19
            enemy3Bullet2Rect.x = x + 19

        # Drawing the lives on window
        if lives == 5:
            pygame.draw.rect(window, yellow, live1Rect)
            pygame.draw.rect(window, yellow, live2Rect)
            pygame.draw.rect(window, yellow, live3Rect)
            pygame.draw.rect(window, yellow, live4Rect)
            pygame.draw.rect(window, yellow, live5Rect)
        if lives == 4:
            pygame.draw.rect(window, yellow, live1Rect)
            pygame.draw.rect(window, yellow, live2Rect)
            pygame.draw.rect(window, yellow, live3Rect)
            pygame.draw.rect(window, yellow, live4Rect)
        if lives == 3:
            pygame.draw.rect(window, yellow, live1Rect)
            pygame.draw.rect(window, yellow, live2Rect)
            pygame.draw.rect(window, yellow, live3Rect)
        if lives == 2:
            pygame.draw.rect(window, yellow, live1Rect)
            pygame.draw.rect(window, yellow, live2Rect)
        if lives == 1:
            pygame.draw.rect(window, yellow, live1Rect)
        # game over
        if lives == 0:
            window.blit(message4, message2Rect)
            pygame.display.flip()
            pygame.event.pump()
            time.sleep(3)
            run = False
            print("Score: ", score)

        # Drawing player bullet
        window.blit(Assets['playerBullet'], (playerBulletRect.x, playerBulletRect.y))

        # Drawing the enemy 1 and bullets
        window.blit(Assets['enemy1Bullet1'], enemy1Bullet1Rect)
        window.blit(Assets['enemy1Bullet2'], enemy1Bullet2Rect)
        window.blit(Assets['enemy1'], enemy1Rect)
        # enemy 1 health status
        pygame.draw.rect(window, red, (enemy1HealthRect.x, enemy1HealthRect.y, 38, 3))
        pygame.draw.rect(window, green, enemy1HealthRect)

        # Drawing the enemy 2 and bullets
        window.blit(Assets['enemy2Bullet1'], enemy2Bullet1Rect)
        window.blit(Assets['enemy2Bullet2'], enemy2Bullet2Rect)
        window.blit(Assets['enemy2'], enemy2Rect)
        # enemy 2 health status
        pygame.draw.rect(window, red, (enemy2HealthRect.x, enemy2HealthRect.y, 38, 3))
        pygame.draw.rect(window, green, enemy2HealthRect)

        # Drawing the enemy 3 and bullets
        window.blit(Assets['enemy3Bullet1'], enemy3Bullet1Rect)
        window.blit(Assets['enemy3Bullet2'], enemy3Bullet2Rect)
        window.blit(Assets['enemy3'], enemy3Rect)
        # enemy 3 health status
        pygame.draw.rect(window, red, (enemy3HealthRect.x, enemy3HealthRect.y, 38, 3))
        pygame.draw.rect(window, green, enemy3HealthRect)

        # Drawing the player ship
        window.blit(Assets['player'], (playerRect.x, playerRect.y))
        # Drawing the player health status
        pygame.draw.rect(window, red, (playerHealthRect.x, playerHealthRect.y, 50, 5))
        pygame.draw.rect(window, green, playerHealthRect)

        # updating the window
        pygame.display.update()
        clock.tick(fps)
    # quit if run = False
    pygame.quit()


mainLoop()
