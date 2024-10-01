import math
import random

import pygame
from pygame import mixer

# initializing the pygame
pygame.init()

# screen settings
screen = pygame.display.set_mode((800, 600))
# background and sound
background = pygame.image.load('bg.png')
mixer.music.load('background.wav')
mixer.music.play(-1)
# Title
pygame.display.set_caption('Space Invaders')
# Get the image to display in icon
icon = pygame.image.load('monster.png')
# load the icon
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('space-invaders (1).png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('monster.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
# ready state means you can't see the bullet on the screen
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('Crashed Scoreboard.ttf', 25)
textX = 10
textY = 10

# Game over Font
over_font=pygame.font.Font('Crashed Scoreboard.ttf',30)

def show_score(x, y):
    score =over_font.render("Score " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
     over_text= over_font.render("Gameover",True, (255, 255, 255))
     screen.blit(over_text,(300,250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# To maintain the screen window until close button is pressed.
running = True
while running:
    # color to the background
    screen.fill((150, 140, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # key down is nothing but a pressing a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_s:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        # when the player releases from the key the position of the image remains still
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # adding the boundaries to our spaceship image by changing th x and y coordinates
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:  # image size - 800
        playerX = 768

    # enemy movements
    for i in range(num_of_enemies):
        # game over
        if enemyY[i]>450:
            for j in range(num_of_enemies):# collecting the enemies and move out of the screen
                enemyY[j]=2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 768:  # image size - 800
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 300
            bullet_state = "ready"
            score_value += 1

            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)
    # bullet movement
    if bulletY <= 0:
        bulletY = 400
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # check for collision

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
