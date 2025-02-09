import pygame
import player
import games
from 飞机大战.fly.player import my_player

pygame.init()
screen = pygame.display.set_mode((800, 600))

#创建射中音效
hit_sound = pygame.mixer.Sound('../wav/exp.wav')

bullets = []  #保存现有的子弹
#子弹
class Bullet():
    def __init__(self):
        self.img = pygame.image.load('../png/bullet.png')
        self.x = player.my_player.x + 16
        self.y = player.my_player.y + 10
        self.step = 3
    #判断击中
    def hit(self):
        for e in games.enemies:
            if games.distance(self.x, self.y, e.x, e.y) < 30:
                #认为射中了
                hit_sound.play()
                bullets.remove(self)
                e.reset()
                games.score += 1

#显示并移动子弹
def show_bullets():
    for b in bullets:
        screen.blit(b.img, (b.x, b.y))
        b.hit()
        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)