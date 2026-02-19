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
    def __init__(self, oyuncu_mermi_grup):
        super().__init__()
        orijinal_resim = pygame.image.load('assets/oyuncu.png').convert_alpha()
        self.image = pygame.transform.scale(orijinal_resim, (100, 100))
        self.rect = self.image.get_rect()
        self.rect=self.image.get_rect()
        self.oyuncu_mermi_grup=oyuncu_mermi_grup
        self.rect.centerx=GENISLIK//2
        self.rect.top=YUKSEKLIK-100

        #oyuncu değişkenleri
        self.hiz=10
        self.can=5
        #mermi ses efekti
        self.mermi_sesi=pygame.mixer.Sound('assets/oyuncu_mermi.wav')

    def update(self):
        tus=pygame.key.get_pressed()
        if tus[pygame.K_LEFT] and self.rect.left>=0:
            self.rect.x-=self.hiz
        if tus[pygame.K_RIGHT] and self.rect.right<=GENISLIK:
            self.rect.x+=self.hiz
    def ates(self):
        pass
    def reset(self):
        self.rect.centerx=GENISLIK//2

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
    def __init__(self,x,y,oyuncu_mermi_grup):
        super().__init__()
        self.image=pygame.image.load('assets/oyuncu_mermi.png')
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        #mermi hız
        self.hiz=10
    def update(self):
        self.rect.y-=self.hiz


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
oyuncu=Oyuncu(oyuncu_mermi)
oyuncu_grup.add(oyuncu)

#uzaylı grup
uzayli_grup=pygame.sprite.Group()

#oyun döngüsü

durum=True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False
    pencere.fill((0,0,0))
    oyuncu_grup.update()
    oyuncu_grup.draw(pencere)

    #penceere güncelleme ve fps tanımlama
    pygame.display.update()
    saat.tick(FPS)

pygame.quit()
