import pygame
from shared import *

class Startbildschirm():
    def __init__(self,screen):
        self.screen = screen
        self.istsichtbar = True
        self.spielmode_PM = pygame.Rect(854,240,170,39)
        self.callback = None


    def zeichnen(self):
        if self.istsichtbar:
            self.screen.blit(startbildschirm, (0,0))
            #pygame.draw.rect(self.screen,(0,0,0), self.spielmode_PM)

    def click(self):
        if not self.istsichtbar:
            return
        x,y = pygame.mouse.get_pos()
        if self.spielmode_PM.collidepoint(x,y):
            self.starteModus("Practice")

    def starteModus(self,modus):
        print("Starte Modus",modus)
        self.istsichtbar = False
        if self.callback is not None:
            self.callback(modus)

    def onstart(self,callback):
        self.callback = callback


    


        
