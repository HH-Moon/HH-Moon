import pygame

#初始化界面
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('飞机大战')  #标题
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
bgImg = pygame.image.load('bg.png')

#游戏主循环
running = True
while running:
    screen.blit(bgImg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()