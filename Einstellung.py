from Taste import Taste
from Regler import Regler
import pygame
from shared import *



class Einstellung():
    instance = None
    def __init__(self, screen):
        Einstellung.instance = self 
        self.screen = screen
        self.istsichtbar = False
        self.menue_ton = pygame.Rect(390,8,57,45)
        self.menue_bildschirm = pygame.Rect(554,8,45,45)
        self.menue_steuerung = pygame.Rect(707,8,55,45)
        self.menue = "Ton"
        self.reglerTon = Regler(screen,250,125)
        self.reglerTon.onchange(self.tongeaendert)
        self.tasteAufheben = Taste(screen, 250, 160, "E")
        self.tasteLinkslaufen = Taste(screen, 250, 220, "A")
        self.tasteRechtslaufen = Taste(screen, 250, 280, "D")

    def tongeaendert(self,wert):
        print(wert)

    def tasteGedrueckt(self,key):
        print(key)
        if self.istsichtbar and self.menue == "steuerung":
            for taste in Taste.tastenliste:
                if taste.istAusgewählt():
                    taste.setKey(key)
    
    @staticmethod
    def getKey(art):
        if art == "aufheben":
            return Einstellung.instance.tasteAufheben.getKey()

                     


    
    def zeichnen(self):
        if self.istsichtbar:
            if self.menue == "Ton":
                self.screen.blit(einstellungenTon, (0,0))
                self.reglerTon.setzesichtbar(True)
            else:
                self.reglerTon.setzesichtbar(False)
            if self.menue == "bildschirm":
                self.screen.blit(einstellungenBildschirm, (0,0))
            if self.menue == "steuerung":
                self.screen.blit(einstellungenSteuerung, (0,0))
                self.tasteAufheben.setzesichtbar(True)
                self.tasteLinkslaufen.setzesichtbar(True)
                self.tasteRechtslaufen.setzesichtbar(True)

            else:
                self.tasteAufheben.setzesichtbar(False)
                self.tasteLinkslaufen.setzesichtbar(False)
                self.tasteRechtslaufen.setzesichtbar(False)
        else:
            self.reglerTon.setzesichtbar(False)
            self.tasteAufheben.setzesichtbar(False)
            self.tasteLinkslaufen.setzesichtbar(False)
            self.tasteRechtslaufen.setzesichtbar(False)
            
            
            

    def togglesichtbar(self):
        self.istsichtbar = not self.istsichtbar

    def click(self):
        if not self.istsichtbar:
            return
        x,y = pygame.mouse.get_pos()
        if self.menue_ton.collidepoint(x,y):
            self.menue = "Ton"
        if self.menue_bildschirm.collidepoint(x,y):
            self.menue = "bildschirm"
        if self.menue_steuerung.collidepoint(x,y):
            self.menue = "steuerung"
        if self.menue == "steuerung":
            for taste in Taste.tastenliste:
                taste.click()
            
        print(self.menue)





    

    
