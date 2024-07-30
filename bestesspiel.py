from Taste import Taste
from Item import Item, Pickaxe,AK
from Inventar import Inventar
import pygame
from shared import *
from pygame.locals import *
import sys
from wand import Wand
from welt import Welt
from boden import Boden
from spieler import Spieler
from Einstellung import Einstellung
from Regler import Regler
from Startbildschirm import Startbildschirm

"""
Hi,
hab dein Programm bisschen angepasst, leider kann ich auf meinem Arbeitsrechner keine librarys installieren und deswegen
konnte ich nicht testen ob das Programm nun kompiliert oder ob noch Fehler drin sind.

Versuch mal, sollten noch Fehler drin sein, diese selbst zu finden... wenn du wirklich nicht weiter kommst, schreib mir
und ich werd schauen ob ich die Tage dafür Zeit hab. Kann dir aber nichts versprechen.

Was du noch machen solltest ist die "Spieler" Klasse und die "Boden" Klasse (siehe unten) in eigene Dateien zu packen,
genauso wie wir das mit Wand und Welt auch gemacht haben. Denk an die Imports!

Und benenn diese Datei mal in Spiel.py oder so etwas ähnliches um.


Noch ein Tip:
1 Klassen werden immer groß geschrieben:
    class MeineKlasse():

2 Konstanten immer in CAPS:
    MEINEKONST = Math.PI

3 Wenn du einer Methode Parameter übergibst, benutz Leerzeichen nach den Kommas:
    meinobject.meinemethode("param1", 42, "param3")

4 und am Wichtigsten:
    Schreib Kommentare! Sonst verstehst du dein Programm irgendwann nicht mehr.
"""




clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Tutorial")


"""
Neue Variable bodenGruppe
-------------------------
Hier fügen wir alle Boden Elemente ein,
nachher sind das nicht nur der Boden, sondern alle Elemente,
auf die unser Spieler springen kann um nicht einfach durchzufallen
"""



"""
Neue Klasse für Boden
---------------------
Höhe=100 wird definiert und ein rect mit x=0, y=UNTEN-hoehe, w=screenBreite, h=screenHoehe erstellt
"""

 

"""
Spieler Klasse aufgeräumt
-------------------------

Damit es bisschen übersichtlicher und dementsprechend auch leichter zu testen ist
Die Funktionen wie
    * Richtung des Spielers
    * Laufbewegung
    * Sprungbild
musst du wieder ergänzen, die hab ich mal weg gemacht


"""
spieler1 = None
welt = None
gestartet = False
def startespiel(modus):
    global gestartet
    global spieler1
    global welt
    spieler1 = Spieler(screen, 0, 50)
    welt = Welt(screen, spieler1)
    gestartet = True








einstellung = Einstellung(screen)

        


inventar = Inventar(screen)

startscreen = Startbildschirm(screen)
startscreen.onstart(startespiel)

boden = Boden(screen)
bodenGruppe.add(boden)

Pickaxe(screen,1000,HOEHE-boden.gethoehe()-60)
Pickaxe(screen,300,HOEHE-boden.gethoehe()-60)

AK(screen,2,HOEHE-boden.gethoehe()-60)








def zeichnen():
    screen.fill((0,0,0))
    if gestartet:
        welt.zeichnen()
        screen.blit(getFPS(), (10,10))
        boden.zeichnen() # Hier malen wir den Boden ein
        for item in Item.liste:
            item.zeichnen()
        spieler1.zeichen() # hier den Spieler
        inventar.zeichnen()
        for wand in Wand.wandliste:
            wand.zeichnen()
        einstellung.zeichnen()
        for regler in Regler.reglerliste:
            regler.zeichnen()
        for taste in Taste.tastenliste:
            taste.zeichnen()
    else: 
        startscreen.zeichnen()
    pygame.display.update()


# wir erstellen ein Boden Objekt und fügen es der oben erstellten Gruppe ("bodenGruppe") hinzu



go = True

def getFPS():
	fps = str(int(clock.get_fps())) + " FPS"
	return font.render(fps, 1, (0, 0, 0))

rGedrueckt = False
escGedrueckt = False

while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            Regler.mausgedrueckt = False
            if gestartet: spieler1.baueWand()
            startscreen.click()
        if event.type == pygame.MOUSEBUTTONDOWN:
            Regler.mausgedrueckt = True
            einstellung.click()
        if event.type == pygame.KEYDOWN:
            einstellung.tasteGedrueckt(pygame.key.name(event.key))

            
    if gestartet:
        gedrueckt = pygame.key.get_pressed()
        spieler1.bodenKollision()
    
        if gedrueckt[pygame.K_SPACE]:
            spieler1.springen()

        if gedrueckt[pygame.K_r]:
            if not rGedrueckt:
                spieler1.startebauen()
                rGedrueckt = True       
        else:
            rGedrueckt = False


        if gedrueckt[pygame.K_ESCAPE]:
            if not escGedrueckt:
                einstellung.togglesichtbar()
                escGedrueckt = True
        else:
            escGedrueckt = False

        
        
        
        spieler1.update()
        spieler1.bewegen()



    
    zeichnen()
    clock.tick(2000)