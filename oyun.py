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
        #mermi ses ayarı
        self.mermi_sesi=pygame.mixer.Sound('assets/oyuncu_mermi.wav')
        self.mermi_sesi.set_volume(0.1)

    def update(self):
        tus=pygame.key.get_pressed()
        if tus[pygame.K_LEFT] and self.rect.left>=0:
            self.rect.x-=self.hiz
        if tus[pygame.K_RIGHT] and self.rect.right<=GENISLIK:
            self.rect.x+=self.hiz
    def ates(self):
        if len(self.oyuncu_mermi_grup)<2:
         self.mermi_sesi.play()
         oyuncuMermi(self.rect.centerx,self.rect.top,self.oyuncu_mermi_grup)
    def reset(self):
        self.rect.centerx=GENISLIK//2

class Uzayli(pygame.sprite.Sprite):
    def __init__(self ,x ,y ,mermi_grup, hiz):
        super().__init__()
        self.image=pygame.image.load("assets/uzayli_gemi.png")
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

        #Uzaylı değişken
        self.basx=x
        self.basy=y
        self.yon=1
        self.hiz=hiz
        self.mermi_grup=mermi_grup
        self.uzayli_mermi_sesi=pygame.mixer.Sound("assets/uzayli_mermi.wav")
    def update(self):
        self.rect.x+=self.yon*self.hiz
        if self.rect.right >= GENISLIK or self.rect.left <= 0:
            self.yon *= -1
            self.rect.y += 10
    def ates(self):
        pass
    def reset(self):
        self.rect.topleft=(self.basx,self.basy)
        self.yon=1

class oyuncuMermi(pygame.sprite.Sprite):
    def __init__(self,x,y,oyuncu_mermi_grup):
        super().__init__()
        self.image=pygame.image.load('assets/oyuncu_mermi.png')
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        #mermi hız
        oyuncu_mermi_grup.add(self)
        self.hiz=14
    def update(self):
        self.rect.y-=self.hiz
        if self.rect.bottom<0:
            self.kill()


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

#test
for i in range(10):
    uzayli=Uzayli(64+i*64,100,uzayli_mermi, 4)
    uzayli_grup.add(uzayli)

#müzik ayarı
pygame.mixer.music.load('assets/arka_plan_sarki.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)
#oyun döngüsü

durum=True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False
        if etkinlik.type==pygame.KEYDOWN:
            if etkinlik.key==pygame.K_SPACE:
                oyuncu.ates()
    pencere.fill((0,0,0))
    oyuncu_grup.update()
    oyuncu_grup.draw(pencere)

    oyuncu_mermi.update()
    oyuncu_mermi.draw(pencere)

    uzayli_grup.update()
    uzayli_grup.draw(pencere)

    pygame.sprite.groupcollide(oyuncu_mermi, uzayli_grup, True, True)

    #penceere güncelleme ve fps tanımlama
    pygame.display.update()
    saat.tick(FPS)

pygame.quit()
