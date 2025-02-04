import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('飞机大战')  #标题
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
