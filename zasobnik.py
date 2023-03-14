import pygame

class Zasobnik:

    def __init__(self, aktualniPocetNaboju):
        self.kapacita = 8
        self.aktualniPocetNaboju = aktualniPocetNaboju

        self.obrazekNaboje = pygame.image.load("grafika/naboj/naboj.png")
        self.rect = self.obrazekNaboje.get_rect()

    def vystrel(self):
        if self.aktualniPocetNaboju > 0:
            self.aktualniPocetNaboju = self.aktualniPocetNaboju - 1

    def nabij(self):
        self.aktualniPocetNaboju = 8

    def nakresli_se(self, herniOkno):
        if (self.aktualniPocetNaboju > 0):
            for cisloNaboje in range(0, self.aktualniPocetNaboju):
                self.rect.x = 1450 + (cisloNaboje * 50)
                self.rect.y = 970
                herniOkno.blit(self.obrazekNaboje, self.rect)
