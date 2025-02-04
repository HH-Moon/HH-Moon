import pygame

#初始化界面
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('飞机大战')  #标题
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
bgImg = pygame.image.load('bg.png')

playerImg = pygame.image.load('player.png')
playerX = 380
playerY = 500
playerStepX = 0
playerStepY = 0

#游戏主循环
running = True
while running:
    screen.blit(bgImg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#通过键盘控制飞机移动
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerStepX = 3
            elif event.key == pygame.K_LEFT:
                playerStepX = -3
            elif event.key == pygame.K_UP:
                playerStepY = -3
            elif event.key == pygame.K_DOWN:
                playerStepY = 3
        if event.type == pygame.KEYUP:
            playerStepX, playerStepY = 0, 0

    screen.blit(playerImg, (playerX, playerY))
    playerX += playerStepX
    playerY += playerStepY

    if playerX > 800 - 64:
        playerX = 800 - 64
    if playerX < 0:
        playerX = 0
    if playerY > 600 - 64:
        playerY = 600 - 64
    if playerY < 0:
        playerY = 0


    pygame.display.update()