from nesneler import Oyuncu, Uzayli
import pygame
import ayarlar

#başlatma
pygame.init()
pencere = pygame.display.set_mode((ayarlar.GENISLIK, ayarlar.YUKSEKLIK))
pygame.display.set_caption('Uzay İstilacıları')
saat = pygame.time.Clock()

#Gruplar
oyuncu_mermi_grup = pygame.sprite.Group()
uzayli_mermi_grup = pygame.sprite.Group()
uzayli_grup = pygame.sprite.Group()
oyuncu_grup = pygame.sprite.Group()

oyuncu = Oyuncu(oyuncu_mermi_grup)
oyuncu_grup.add(oyuncu)

#Background music settings
pygame.mixer.music.load('assets/arka_plan_sarki.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

for i in range(10):
    yeni_uzayli = Uzayli(64 + i*80, 100, uzayli_mermi_grup, 4)
    uzayli_grup.add(yeni_uzayli)


durum = True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False

        if etkinlik.type == pygame.KEYDOWN:
            if etkinlik.key == pygame.K_SPACE:
                oyuncu.ates()


    oyuncu_grup.update()
    uzayli_grup.update()
    oyuncu_mermi_grup.update()
    uzayli_mermi_grup.update()


    pygame.sprite.groupcollide(oyuncu_mermi_grup, uzayli_grup, True, True)


    pencere.fill(ayarlar.SIYAH)

    oyuncu_grup.draw(pencere)
    uzayli_grup.draw(pencere)
    oyuncu_mermi_grup.draw(pencere)
    uzayli_mermi_grup.draw(pencere)

    pygame.display.update()
    saat.tick(ayarlar.FPS)


pygame.quit()