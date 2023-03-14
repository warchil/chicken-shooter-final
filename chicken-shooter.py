import random

import pygame
import slepice
import zasobnik

pygame.init()

pygame.mixer.init()
zvukVystrelu = pygame.mixer.Sound('zvuky/pistol.wav')
zvukZasahuSlepice = pygame.mixer.Sound('zvuky/zasah.wav')

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

prvniSlepice = slepice.Slepice(100, 5)

hraBezi = True
while hraBezi:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hraBezi = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.Channel(0).play(zvukVystrelu)
            if prvniSlepice.zastrelena(obrazekZamerovace_rect):
                skore = skore + 1
                text = font.render("Skore: " + str(skore), True, pygame.Color("white"))
                text_rect = text.get_rect()
                pygame.mixer.Channel(0).play(zvukZasahuSlepice)
                prvniSlepice.restartuj_se()

    herniOkno.blit(pozadi, (0, 0))

    prvniSlepice.posun_se()
    prvniSlepice.nakresli_se(herniOkno)

    obrazekZamerovace_rect.center = pygame.mouse.get_pos()
    herniOkno.blit(obrazekZamerovace, obrazekZamerovace_rect)

    herniOkno.blit(text, text_rect)

    pygame.display.update()
    hodiny.tick(30)

pygame.quit()

