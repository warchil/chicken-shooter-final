import pygame
import random

class Slepice:

    def __init__(self, velikost, rychlost):
        self.velikost = velikost
        self.rychlost = rychlost

        self.cisloObrazku = 0
        self.poleObrazku = []
        self.nacti_pole_obrazku()

        self.rect = self.poleObrazku[0].get_rect()
        self.restartuj_se()

    def nacti_pole_obrazku(self):
        obrazek = pygame.image.load("grafika/slepice/slepice00.png")
        print(obrazek.get_height(), obrazek.get_width())
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                           obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        obrazek = pygame.image.load("grafika/slepice/slepice01.png")
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                           obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        obrazek = pygame.image.load("grafika/slepice/slepice02.png")
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                           obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        obrazek = pygame.image.load("grafika/slepice/slepice03.png")
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                           obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        obrazek = pygame.image.load("grafika/slepice/slepice04.png")
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                           obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        obrazek = pygame.image.load("grafika/slepice/slepice05.png")
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                           obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        obrazek = pygame.image.load("grafika/slepice/slepice06.png")
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                 obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        obrazek = pygame.image.load("grafika/slepice/slepice07.png")
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                 obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        obrazek = pygame.image.load("grafika/slepice/slepice08.png")
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                 obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        obrazek = pygame.image.load("grafika/slepice/slepice09.png")
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                 obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        obrazek = pygame.image.load("grafika/slepice/slepice10.png")
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                 obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        obrazek = pygame.image.load("grafika/slepice/slepice11.png")
        upravenyObrazek = pygame.transform.scale(obrazek, (obrazek.get_height() * self.velikost / 100,
                                                 obrazek.get_height() * self.velikost / 100))
        self.poleObrazku.append(upravenyObrazek)

        # self.poleObrazku.append(pygame.image.load("grafika/slepice/slepice01.png"))
        # self.poleObrazku.append(pygame.image.load("grafika/slepice/slepice02.png"))
        # self.poleObrazku.append(pygame.image.load("grafika/slepice/slepice03.png"))
        # self.poleObrazku.append(pygame.image.load("grafika/slepice/slepice04.png"))
        # self.poleObrazku.append(pygame.image.load("grafika/slepice/slepice05.png"))
        # self.poleObrazku.append(pygame.image.load("grafika/slepice/slepice06.png"))
        # self.poleObrazku.append(pygame.image.load("grafika/slepice/slepice07.png"))
        # self.poleObrazku.append(pygame.image.load("grafika/slepice/slepice08.png"))
        # self.poleObrazku.append(pygame.image.load("grafika/slepice/slepice09.png"))
        # self.poleObrazku.append(pygame.image.load("grafika/slepice/slepice10.png"))
        # self.poleObrazku.append(pygame.image.load("grafika/slepice/slepice11.png"))

    def nakresli_se(self, herniOkno):
        herniOkno.blit(self.poleObrazku[self.cisloObrazku], self.rect)

    def restartuj_se(self):
        self.rect.x = 0
        self.rect.y = random.randint(0, random.randint(0, 850))

    def zastrelena(self, zamerovac_rect):
        return self.rect.colliderect(zamerovac_rect)

    def posun_se(self):

        if (self.cisloObrazku >= len(self.poleObrazku) - 1):
            self.cisloObrazku = 0
        else:
            self.cisloObrazku = self.cisloObrazku + 1

        if self.rect.x > 1920:  ## TADY - reseni dorazeni na okraj obrazovky
            self.restartuj_se()

        self.rect.x = self.rect.x + self.rychlost