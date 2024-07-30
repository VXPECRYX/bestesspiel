from welt import Welt
import pygame
from wand import Wand
from shared import *
from Item import Item

class Spieler(pygame.sprite.Sprite):
    def __init__(self,screen,x,y):
        super().__init__()
        self.springtGerade = False
        self.laeuftGerade = False
        
        self.pos = vec((x, y)) # Position
        self.vel = vec(0,0) # Geschwindigkeit
        self.acc = vec(0,0) # Beschleunigung
        
        self.breite = 96
        self.hoehe = 91

        self.schritte = 0
        
        self.wandabstand = 100

        self.screen = screen
        self.wand = Wand(screen, self.screen.get_width()/2 + self.wandabstand, 0) # wir plazieren die wand in der mitte des bildschirms plus 1.5x der breite des Spielers (bisschen versetzt)
        self.wand.setsichtbar(False)
        self.wand.setzeyvonboden(y+self.hoehe)
        
        self.setzteBild(stand)

        self.richtung = "links"
        self.rect = self.image.get_rect()
        self.hitBox = pygame.Rect(self.pos.x,self.pos.y,self.breite,self.hoehe)

    def setzteBild(self, bild, gespiegelt = False):
        self.image = pygame.transform.scale(bild, (self.breite, self.hoehe))
        self.image = pygame.transform.flip(self.image, gespiegelt, False)

    def update(self):
        ### Hier gehört die Logik rein, welches sprite (Bild/Asset) gemalt wird
        ### z.B. ändere ich die Farbe je nachdem in welche richtung du läufst

        if self.laeuftGerade == True:
            self.richtung = "links" if self.vel.x < 0 else "rechts"

        if self.springtGerade == False and self.laeuftGerade == True:
            self.schritte += 0.11
            if self.schritte >= len(linksGehen)-1:
                self.schritte = 0
            if self.vel.x < 0:
                self.setzteBild(linksGehen[round(self.schritte)])
            else:
                self.setzteBild(linksGehen[round(self.schritte)], True)
        elif self.springtGerade:
            self.setzteBild(sprung)
        else:
            self.setzteBild(stand)
        for item in Item.liste:
            if item.getCollectBox().colliderect(self.hitBox):
                item.setzeBeschreibungSichtbar(True)
            else:
                item.setzeBeschreibungSichtbar(False)

    def bewegen(self):
        self.acc = vec(0,GRAVITATION)

        # Wir schauen ob wir rennen oder nicht abs(int) berechnet den absoluten wert einer zahl (|-2| = 2, |3|=3)
        if abs(self.vel.x) > 0.3:
            self.laeuftGerade = True
        else:
            self.laeuftGerade = False
        
        # Wir fragen Tastendruck ab
        gedrueckt = pygame.key.get_pressed()
        if gedrueckt[pygame.K_a] and not self.hitBox.colliderect(self.wand):
            self.acc.x = -BESCHLEUNIGUNG # nach links (Besch = negativ)
        if gedrueckt[pygame.K_d]:
            self.acc.x = BESCHLEUNIGUNG # nach rechts (Besch = positiv)
        
        # Wir berechnen Physic acc=Beschleunigung, vel=Geschwindigkeit, pos=Position
        self.acc.x += self.vel.x * REIBUNG
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        self.rect.y = self.pos.y
        self.rect.x = self.pos.x - self.breite/2

        self.wand.setzeyvonboden(self.pos.y+self.hoehe)
        self.wand.setzex(self.screen.get_width()/2 + self.wandabstand*(1 if self.richtung=="rechts" else -1))

    def baueWand(self):
        if not self.wand.sichtbar:
            return
        self.wand.setzex(Welt.getPos()+ self.wandabstand*(1 if self.richtung=="rechts" else -1))
        self.wand.bauen()
        bodenGruppe.add(self.wand)
        self.wand = Wand(self.screen, self.screen.get_width()/2 + self.wandabstand, 0)
        self.wand.setzeyvonboden(self.pos.y+self.hoehe)
        self.wand.setsichtbar()

    def bodenKollision(self):
        # Wir testen ob wir den Boden berühren
        hits = pygame.sprite.spritecollide(self, bodenGruppe, False)
        if self.vel.y > 0 and hits: # wenn wir gerade fallen (self.vel.y > 0) und den Boden berühren (hits)
            lowest = hits[0]
            if self.pos.y < lowest.rect.bottom:
                self.pos.y = lowest.rect.top - self.hoehe + 1
                self.vel.y = 0 # stoppe fallen
                self.springtGerade = False # stoppe springen

    def springen(self):
        # wir schauen ob wir den Boden berühren
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, bodenGruppe, False)
        self.rect.x -= 1
        
        
        # wenn wir gerade den Boden berühren können wir springen
        if hits and not self.springtGerade:
           self.springtGerade = True
           self.vel.y = -6
           if soundan == True:
               sprungSound.play()

    def zeichen(self):
        # Hier berechnen wir x = Hälfte von der Bildschirmbreite - Hälfe von der Spielerbreite => Mitte vom Bildschirm
        x, y = self.screen.get_size()
        x = x/2-self.breite/2
        self.screen.blit(self.image, (x, self.pos.y, self.breite, self.hoehe))

        hits = pygame.sprite.spritecollide(self, bodenGruppe, False)
        self.hitBox.x = x
        self.hitBox.y = self.pos.y
        pygame.draw.rect(self.screen, (255, 0, 0) if hits else (0, 255, 0),self.hitBox, 1) # grüne hitbox wenn keine kollision, rote wenn kolission


    def startebauen(self):
        self.wand.togglesichtbar()
        