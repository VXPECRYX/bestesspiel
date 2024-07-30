from welt import Welt
import pygame
from shared import *
from Einstellung import Einstellung

class Item():
    liste = []
    schriftKlein = pygame.font.Font(None,14)
    schriftGroß = pygame.font.Font(None,24)
    def __init__(self,screen,x,y):
        self.screen = screen 
        self.pos = vec(x,y)
        self.groesse = 60
        self.breiteBeschreibung = 120
        self.beschreibung = None
        self.rect = pygame.Rect(x,y,self.groesse,self.groesse)
        self.image = None
        Item.liste.append(self)
        self.collectDistance = 100
        self.collectBox = pygame.Rect(x,y,self.collectDistance,self.collectDistance)
        self.beschreibungSichtbar = False
        self.itemname = ""
        self.seltenheit = ""

    def setzeitemname(self,name):
        self.itemname = name 
    
    def setzeseltenheit(self,seltenheit):
        self.seltenheit = seltenheit


    def getCollectBox(self):
        return self.collectBox

    def setzeBeschreibungSichtbar(self,sichtbar):
        self.beschreibungSichtbar = sichtbar
        

      

    def zeichnen(self):
        x = self.pos.x-Welt.getPos()
        self.collectBox.x = x+self.groesse/2-self.collectDistance/2
        pygame.draw.rect(self.screen,(255,0,0), self.collectBox,1)
        self.screen.blit(self.image,(x,self.pos.y))
        if self.beschreibung is not None and self.beschreibungSichtbar:
            self.screen.blit(self.beschreibung,((x+self.groesse/2-self.breiteBeschreibung/2),self.pos.y-self.beschreibung.get_height()))
            titel = Item.schriftKlein.render(self.itemname, 1, (0, 0, 0))
            self.screen.blit(titel, (x-titel.get_rect().width/2+50,self.pos.y-self.beschreibung.get_height()+15))
            rare = Item.schriftKlein.render(self.seltenheit, 1, (100, 100, 100))
            self.screen.blit(rare, (x-rare.get_rect().width/2+50,self.pos.y-self.beschreibung.get_height()+35))
            key = Item.schriftGroß.render(Einstellung.getKey("aufheben"), 1, (0, 0, 0))
            self.screen.blit(key, (x-key.get_rect().width/2-5,self.pos.y-self.beschreibung.get_height()/2-key.get_rect().height/2+3))





    def setzteBild(self, bild, gespiegelt = False):
        self.image = pygame.transform.scale(bild, (self.groesse, self.groesse))
        self.image = pygame.transform.flip(self.image, gespiegelt, False)

    def setzteBeschreibung(self, bild):
        self.beschreibung = pygame.transform.scale(bild, (self.breiteBeschreibung,round((bild.get_height()/bild.get_width())*self.breiteBeschreibung)))
     

class Pickaxe(Item):
    def __init__(self,screen,x,y):
        super().__init__(screen,x,y)
        self.setzteBild(pickaxe)
        self.setzteBeschreibung(aufheben)
        self.setzeitemname("Pickaxe")
        self.setzeseltenheit("Gewöhnlich")


class AK(Item):
    def __init__(self,screen,x,y):
        super().__init__(screen,x,y)
        self.setzteBild(ak)
        self.setzteBeschreibung(aufhebenAK)
        self.setzeitemname("AK")
        self.setzeseltenheit("Normal")

    