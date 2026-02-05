import pygame
import random

#Pygame hazırlık
pygame.init()

#pencere
GENISLIK, YUKSEKLIK = 1250,750
pencere=pygame.display.set_mode((GENISLIK,YUKSEKLIK))

#fps
FPS=60
saat=pygame.time.Clock()

#oyun döngüsü

durum=True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False

pygame.quit()
