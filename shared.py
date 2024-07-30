import pygame

from pygame.locals import *

vec = pygame.math.Vector2
bodenGruppe = pygame.sprite.Group()
itemGruppe = pygame.sprite.Group()


pygame.init()



GRAVITATION = 0.3
BESCHLEUNIGUNG = 0.3
REIBUNG = -0.10
BREITE = 1198
HOEHE = 593

screen = pygame.display.set_mode([BREITE, HOEHE])


"""
Neue Konstanten (Variablen klein, Konstanten groß geschrieben)
---------------
Konstanten bleiben persistent und lassen sich nicht ändern, Variablen schon

"""

font = pygame.font.SysFont("Arial", 30)
angriffLinks = pygame.image.load("./Grafiken/angriffLinks.png")
angriffRechts = pygame.image.load("./Grafiken/angriffRechts.png")
stand = pygame.image.load("./Grafiken/stand.png")
sprung = pygame.image.load("./Grafiken/sprung.png")
#rechtsGehen = [pygame.image.load("Grafiken/rechts1.png"),pygame.image.load("Grafiken/rechts2.png"),pygame.image.load("Grafiken/rechts3.png"),pygame.image.load("Grafiken/rechts4.png"),pygame.image.load("Grafiken/rechts5.png"),pygame.image.load("Grafiken/rechts6.png"),pygame.image.load("Grafiken/rechts7.png"),pygame.image.load("Grafiken/rechts8.png")]
linksGehen = [pygame.image.load("Grafiken/links1.png"),pygame.image.load("Grafiken/links2.png"),pygame.image.load("Grafiken/links3.png"),pygame.image.load("Grafiken/links4.png"),pygame.image.load("Grafiken/links5.png"),pygame.image.load("Grafiken/links6.png"),pygame.image.load("Grafiken/links7.png"),pygame.image.load("Grafiken/links8.png")]
sprungSound = pygame.mixer.Sound("./Sounds/sprung.wav")
soundan = False
einstellungsmenueEinfach = pygame.image.load("./Grafiken/EinstellungenGesamtübersicht.png")
einstellungenTon = pygame.image.load("./Grafiken/EinstellungenGesamtübersicht2 - Kopie (2).png")
einstellungenBildschirm = pygame.image.load("./Grafiken/EinstellungenGesamtübersichtbildschirm.png")
einstellungenSteuerung = pygame.image.load("./Grafiken/EinstellungenGesamtübersichtbildschirmsteuerung.png")
inventar = pygame.image.load("./Grafiken/Inventar.png")
pickaxe = pygame.image.load("./Grafiken/1Pickaxe.png")
startbildschirm = pygame.image.load("./Grafiken/Hintergrund100000.png")
aufheben = pygame.image.load("./Grafiken/aufheben.png")
ak = pygame.image.load("./Grafiken/AK.png")
aufhebenAK = pygame.image.load("./Grafiken/aufheben2.png")







