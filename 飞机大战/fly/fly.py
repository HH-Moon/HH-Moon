import pygame
import random
import math

#初始化界面
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('飞机大战')  #标题
icon = pygame.image.load('ufo.png')   #游戏窗口
pygame.display.set_icon(icon)
bgImg = pygame.image.load('bg.png')

#添加背景音效
pygame.mixer.music.load('bg.wav')
pygame.mixer.music.play(-1)
#创建射中音效
hit_sound = pygame.mixer.Sound('exp.wav')

#分数
score = 0
# font = pygame.font.Font('freesansbold.ttf', 32)
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

#玩家
playerImg = pygame.image.load('player.png')
#玩家坐标
playerX = 380
playerY = 500
#玩家移动的速度
playerStepX = 0
playerStepY = 0

def process_events():
    # 通过键盘控制飞机移动和发射子弹
    global playerStepX, playerStepY, running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerStepX = 2
            elif event.key == pygame.K_LEFT:
                playerStepX = -2
            elif event.key == pygame.K_UP:
                playerStepY = -2
            elif event.key == pygame.K_DOWN:
                playerStepY = 2
            elif event.key == pygame.K_SPACE:
                bullets.append(Bullet())
        elif event.type == pygame.KEYUP:
            playerStepX, playerStepY = 0, 0
    return True


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
            e.y +=40
            if e.y > 450:
                is_over = True
                enemies.clear()

def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a * a + b * b)

#子弹
class Bullet():
    def __init__(self):
        self.img = pygame.image.load('bullet.png')
        self.x = playerX + 16
        self.y = playerY + 10
        self.step = 3
    #判断击中
    def hit(self):
        global score
        for e in enemies:
            if distance(self.x, self.y, e.x, e.y) < 30:
                #认为射中了
                hit_sound.play()
                bullets.remove(self)
                e.reset()
                score += 1
bullets = []  #保存现有的子弹

#显示并移动子弹
def show_bullets():
    for b in bullets:
        screen.blit(b.img, (b.x, b.y))
        b.hit()

        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)

#游戏主循环
running = True
while running:
    screen.blit(bgImg, (0,0))
    show_score()
    #计算通过键盘使飞机移动的步数
    running = process_events()

    screen.blit(playerImg, (playerX, playerY))
    #实现移动
    move_player()
    show_enemy()
    show_bullets()
    check_is_over()



    pygame.display.update()