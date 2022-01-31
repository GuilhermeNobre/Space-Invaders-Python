import pygame as pyg
from random import randint
from math import sqrt, pow

# Variable global
player_speed = 2.5
enemy_speed = 1.2
bullet_speed = 3

# Initialize the pygame
pyg.init()

# create the screen
screen = pyg.display.set_mode((800, 600))

#Background

background = pyg.image.load("Image/Background.png")

# Title and Icon
pyg.display.set_caption("SPACE INVANDERS")
icon = pyg.image.load("Image/spaceship.png")
pyg.display.set_icon(icon)

# Player
playerImg = pyg.image.load("Image/spaceship_player.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pyg.image.load("Image/enemy.png")
enemyX = randint(0, 800)
enemyY = randint(50, 150)
enemyX_change = enemy_speed
enemyY_change = 40

#Bullet

#Ready - You can't see the bullet on the screen
#Fire - The Bullet is currently moving 

bulletImg = pyg.image.load("Image/bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = bullet_speed
bullet_state = "ready"

score =  0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = sqrt(pow(enemyX - bulletX, 2) + pow(enemyY - bulletY, 2)) 
    if distance < 27: 
        return True
    else:
        return False 

# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))

    #Background add
    screen.blit(background, (0, 0))

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

        # If keastroke ins press check / faz um check pra vê foi clicado
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_LEFT or event.key == pyg.K_a:
                playerX_change = -player_speed
            
            if event.key == pyg.K_RIGHT or event.key == pyg.K_d:
                playerX_change = player_speed
            
            if event.key == pyg.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pyg.KEYUP:
            if event.key == pyg.K_LEFT or event.key == pyg.K_RIGHT \
                    or event.key == pyg.K_d or event.key == pyg.K_a:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = enemy_speed
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -enemy_speed
        enemyY += enemyY_change

    # Bullet Movement pygame
    if bulletY <= -100:
        bulletY = 480
        bullet_state = "ready"


    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #Collision 
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pyg.display.update()

