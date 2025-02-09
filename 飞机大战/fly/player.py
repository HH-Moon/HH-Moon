import pygame
import games
import Bullets

class Player():
    def __init__(self):
        self.img = pygame.image.load('../png/player.png')
        self.x = 380
        self.y = 500
        self.stepX = 0
        self.stepY = 0
    def move_player(self):
        self.x += self.stepX
        self.y += self.stepY
        # 控制飞机出界
        if self.x > 800 - 64:
            self.x = 800 - 64
        if self.x < 0:
            self.x = 0
        if self.y > 600 - 64:
            self.y = 600 - 64
        if self.y < 0:
            self.y = 0
my_player = Player()
def process_events():
    # 通过键盘控制飞机移动和发射子弹
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            elif event.key == pygame.K_RIGHT:
                my_player.stepX = 2
            elif event.key == pygame.K_LEFT:
                my_player.stepX = -2
            elif event.key == pygame.K_UP:
                my_player.stepY = -2
            elif event.key == pygame.K_DOWN:
                my_player.stepY = 2
            elif event.key == pygame.K_SPACE:
                Bullets.bullets.append(Bullets.Bullet())
        elif event.type == pygame.KEYUP:
            my_player.stepX, my_player.stepY = 0, 0
    return True

def check_player_enemy():
        for e in games.enemies:
            if games.distance(my_player.x, my_player.y, e.x, e.y) < 50:
                return True
        return False