import pygame
import random
import math
import player

pygame.init()
screen = pygame.display.set_mode((800, 600))

#分数
score = 0
font = pygame.font.SysFont('kaiti', 32)
font.set_bold(True)
def show_score():
    text = f"分数：{score}"
    score_render = font.render(text, True, (255, 255, 0))
    screen.blit(score_render, (10, 10))

#游戏结束
is_over = False
over_font = pygame.font.SysFont('kaiti', 64)
over_font.set_bold(True)
def check_is_over():
    if is_over:
        text = "游戏结束！！！"
        render = over_font.render(text, True, (255, 0, 0))
        screen.blit(render, (200, 250))


#敌人
number_of_enemies = 6
class Enemy():
    def __init__(self):
        self.img = pygame.image.load('../png/enemy.png')
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
        self.step = 1
    #当被射中时 重置敌人的位置
    def reset(self):
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
enemies = []
for i in range(number_of_enemies):
    enemies.append(Enemy())

def show_enemy():
    global is_over
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if e.x > 800 - 64 or e.x < 0:
            e.step *= -1
            e.y += 40
            if e.y > 450:
                is_over = True
                enemies.clear()

def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a * a + b * b)