import random

import pygame
import slepice
import zasobnik

pygame.init()

pygame.mixer.init()
zvukVystrelu = pygame.mixer.Sound('zvuky/pistol.wav')
zvukZasahuSlepice = pygame.mixer.Sound('zvuky/zasah.wav')
zvukNabiti = pygame.mixer.Sound('zvuky/nabiti.wav')
zvukPrazdnehoZasobniku = pygame.mixer.Sound('zvuky/prazdny-zasobnik.wav')
hudbaNaPozadi = pygame.mixer.Sound('zvuky/music.mp3')

font = pygame.font.Font("freesansbold.ttf", 32)

herniOkno = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Chicken shooter")

pozadi = pygame.image.load("grafika/pozadi/les.jpg")
pozadi = pygame.transform.scale(pozadi, (1920, 1080))

pygame.mouse.set_visible(False)
obrazekZamerovace = pygame.image.load("grafika/zamerovac/crosshair.png")
obrazekZamerovace = pygame.transform.scale(obrazekZamerovace, (64, 64))
obrazekZamerovace_rect = obrazekZamerovace.get_rect()

skore = 0
hodiny = pygame.time.Clock()

text = font.render("Skore: " + str(skore), True, pygame.Color("white"))
text_rect = text.get_rect()

# prvniSlepice = slepice.Slepice(100, 5)

mnozinaSlepic = {
    slepice.Slepice(random.randint(75, 150), random.randint(3, 15)),
    slepice.Slepice(random.randint(75, 150), random.randint(3, 15)),
    slepice.Slepice(random.randint(75, 150), random.randint(3, 15))
}

pygame.mixer.Channel(7).play(hudbaNaPozadi, -1)

aktualniZasobnik = zasobnik.Zasobnik(8)

hraBezi = True
while hraBezi:

    for event in pygame.event.get():
        # Pokud hrac kliknul na krizek, tak se nastavi promenna "hraBezi" na False (Nepravda)
        if event.type == pygame.QUIT:
            hraBezi = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.button == 1):
                if (aktualniZasobnik.aktualniPocetNaboju > 0):
                    aktualniZasobnik.aktualniPocetNaboju = aktualniZasobnik.aktualniPocetNaboju - 1
                    pygame.mixer.Channel(0).play(zvukVystrelu)
                    for slepice in mnozinaSlepic:
                        if slepice.zastrelena(obrazekZamerovace_rect):
                            skore = skore + 1
                            text = font.render("Skore: " + str(skore), True, pygame.Color("white"))
                            text_rect = text.get_rect()
                            pygame.mixer.Channel(0).play(zvukZasahuSlepice)
                            slepice.restartuj_se()
                else:
                    pygame.mixer.Channel(0).play(zvukPrazdnehoZasobniku)
            else:
                pygame.mixer.Channel(0).play(zvukNabiti)
                aktualniZasobnik.aktualniPocetNaboju = 8

    herniOkno.blit(pozadi, (0, 0))

    aktualniZasobnik.nakresli_se(herniOkno)

    for slepice in mnozinaSlepic:
        slepice.posun_se()
        slepice.nakresli_se(herniOkno)

    obrazekZamerovace_rect.center = pygame.mouse.get_pos()
    herniOkno.blit(obrazekZamerovace, obrazekZamerovace_rect)

    herniOkno.blit(text, text_rect)

    pygame.display.update()
    hodiny.tick(30)

pygame.quit()

