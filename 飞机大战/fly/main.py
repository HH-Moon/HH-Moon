import pygame
import random
import math
import games
import player
import Bullets

#初始化界面
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('飞机大战')         #标题
icon = pygame.image.load('../png/ufo.png')   #游戏窗口
pygame.display.set_icon(icon)
bgImg = pygame.image.load('../png/bg.png')

#添加背景音效
pygame.mixer.music.load('../wav/bg.wav')
pygame.mixer.music.play(-1)

#游戏主循环
running = True
while running:
    screen.blit(bgImg, (0,0))
    games.show_score()
    #计算通过键盘使飞机移动的步数
    running = player.process_events()
    screen.blit(player.my_player.img, (player.my_player.x, player.my_player.y))
    #实现移动
    player.my_player.move_player()
    games.show_enemy()
    Bullets.show_bullets()
    if(player.check_player_enemy()):
        games.is_over = True
        games.enemies.clear()
    games.check_is_over()

    pygame.display.update()