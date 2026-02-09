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

class Oyun():
    def __init__(self):
        pass
    def update(self):
        pass
    def cizdir(self):
        pass
    def uzayli_konum_degistir(self):
        pass
    def temas(self):
        pass
    def bitir(self):
        pass
    def bolum(self):
        pass
    def oyun_durumu(self):
        pass
    def tamamlandi(self):
        pass
    def durdur(self):
        pass
    def oyun_reset(self):
        pass


class Oyuncu(pygame.sprite.Sprite):
    def __init__(self):
        pass
    def update(self):
        pass
    def ates(self):
        pass
    def reset(self):
        pass

class Uzayli(pygame.sprite.Sprite):
    def __init__(self):
        pass
    def update(self):
        pass
    def ates(self):
        pass
    def reset(self):
        pass

class oyuncuMermi(pygame.sprite.Sprite):
    def __init__(self):
        pass
    def update(self):
        pass

class uzayliMermi(pygame.sprite.Sprite):
    def __init__(self):
        pass
    def update(self):
        pass

#Mermi Grup
oyuncu_mermi=pygame.sprite.Group()
uzayli_mermi=pygame.sprite.Group()

#Oyuncu Tanımlama
oyuncu_grup=pygame.sprite.Group()
oyuncu=Oyuncu()
oyuncu_grup.add(oyuncu)

#uzaylı grup
uzayli_grup=pygame.sprite.Group()

#oyun döngüsü

durum=True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False

    #penceere güncelleme ve fps tanımlama
    pygame.display.update()
    saat.tick(FPS)

pygame.quit()
