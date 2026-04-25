import pygame
import ayarlar
import random

#Oyuncu tanımı
class Oyuncu(pygame.sprite.Sprite):
    def __init__(self, oyuncu_mermi_grup):
        super().__init__()
        oyuncu_resmi = pygame.image.load('assets/oyuncu.png').convert_alpha()
        self.image = pygame.transform.scale(oyuncu_resmi, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = ayarlar.GENISLIK // 2
        self.rect.top = ayarlar.YUKSEKLIK - 100
        self.oyuncu_mermi_grup = oyuncu_mermi_grup
        self.hiz = 10

    def update(self):
        tus = pygame.key.get_pressed()
        if tus[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.hiz
        if tus[pygame.K_RIGHT] and self.rect.right < ayarlar.GENISLIK:
            self.rect.x += self.hiz

    def ates(self):
        if len(self.oyuncu_mermi_grup) < 2:
            OyuncuMermi(self.rect.centerx, self.rect.top, self.oyuncu_mermi_grup)


#Oyuncu mermi ayarları
class OyuncuMermi(pygame.sprite.Sprite):
    def __init__(self, x, y, grup):
        super().__init__()
        self.image = pygame.image.load('assets/oyuncu_mermi.png')
        self.rect = self.image.get_rect(center=(x,y))
        self.hiz = 14
        grup.add(self)

    def update(self):
        self.rect.y -= self.hiz
        if self.rect.bottom < 0:
            self.kill() 


#Uzaylı tanımı
class Uzayli(pygame.sprite.Sprite):
    def __init__(self, x, y, mermi_grup, hiz):
        super().__init__()
        uzayli_resmi = pygame.image.load('assets/uzayli_gemi.png').convert_alpha()
        self.image = pygame.transform.scale(uzayli_resmi,(64, 64))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.basx = x
        self.basy = y
        self.yon  = 1
        self.hiz  = hiz
        self.mermi_grup = mermi_grup
        self.uzayli_mermi_sesi = pygame.mixer.Sound('assets/uzayli_mermi.wav')
        self.uzayli_mermi_sesi.set_volume(0.1)


    def update(self):

        self.rect.x += self.yon * self.hiz
        if self.rect.right >= ayarlar.GENISLIK or self.rect.left <= 0:
            self.yon *= -1
            self.rect.y += 10

        if random.randint(0, 1000) > 998:
            self.ates()

    def ates(self):
        
        UzayliMermi(self.rect.centerx, self.rect.bottom, self.mermi_grup)

    def reset(self):
        self.rect.topleft = (self.basx, self.basy)
        self.yon = 1


class UzayliMermi(pygame.sprite.Sprite):
    def __init__(self, x, y, grup):
        super().__init__()
        self.image = pygame.image.load('assets/uzayli_mermi.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.hiz = 8
        grup.add(self)

    def update(self):
        self.rect.y += self.hiz

        if self.rect.top > ayarlar.YUKSEKLIK:
            self.kill()





