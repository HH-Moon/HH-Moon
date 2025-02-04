import pygame
import random

#初始化界面
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('飞机大战')  #标题
icon = pygame.image.load('ufo.png')   #游戏窗口
pygame.display.set_icon(icon)
bgImg = pygame.image.load('bg.png')

#玩家
playerImg = pygame.image.load('player.png')
#玩家坐标
playerX = 380
playerY = 500
#玩家移动的速度
playerStepX = 0
playerStepY = 0

def process_events():
    # 通过键盘控制飞机移动
    global playerStepX, playerStepY
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            playerStepX = 2
        elif event.key == pygame.K_LEFT:
            playerStepX = -2
        elif event.key == pygame.K_UP:
            playerStepY = -2
        elif event.key == pygame.K_DOWN:
            playerStepY = 2
    if event.type == pygame.KEYUP:
        playerStepX, playerStepY = 0, 0

def move_player():
    global  playerX, playerY
    playerX += playerStepX
    playerY += playerStepY
    #控制飞机出界
    if playerX > 800 - 64:
        playerX = 800 - 64
    if playerX < 0:
        playerX = 0
    if playerY > 600 - 64:
        playerY = 600 - 64
    if playerY < 0:
        playerY = 0

#敌人
number_of_enemies = 6
class Enemy():
    def __init__(self):
        self.img = pygame.image.load('enemy.png')
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
        self.step = random.randint(1,3)

enemies = []
for i in range(number_of_enemies):
    enemies.append(Enemy())

def show_enemy():
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if e.x > 800 - 64 or e.x < 0:
            e.step *= -1
            e.y +=60

#游戏主循环
running = True
while running:
    screen.blit(bgImg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #计算通过键盘使飞机移动的步数
    process_events()
    screen.blit(playerImg, (playerX, playerY))
    #实现移动
    move_player()
    show_enemy()

    pygame.display.update()