from sys import float_repr_style
import pygame
from pygame.draw import rect
from shared import *
import math


class Regler():
    reglerliste = []
    mausgedrueckt = False   

    def __init__(self,screen,x,y,):
        self.x = x
        self.y = y
        Regler.reglerliste.append(self)
        self.height = 4
        self.width = 120
        self.rect = pygame.Rect(x,y,self.width,self.height)
        self.circle = vec(x,y+ self.height/2)
        self.screen = screen
        self.radius = 10
        self.gedrueckt = False
        self.istsichtbar = True
        self.callback = None
        self.wertvorher = 0


    def zeichnen(self):
        if self.istsichtbar:
            if Regler.mausgedrueckt : 
                x,y = pygame.mouse.get_pos()
                if math.sqrt((x-self.circle.x)**2+(y-self.y)**2)<self.radius:
                    self.gedrueckt = True
            else:
                self.gedrueckt = False
            if self.gedrueckt:
                self.circle.x = max(min(self.rect.right,x),self.rect.left)  
            pygame.draw.rect(self.screen,(0,0,0),self.rect)
            pygame.draw.circle(self.screen,(100,100,100),self.circle,10)
            wert = round(((self.circle.x-self.x)/self.width)*100)
            self.screen.blit(font.render(str(wert)+"%",1,(0,0,0)),(self.rect.right+10,self.rect.top-16))
            if self.callback is not None and wert != self.wertvorher:
                self.callback(wert)
                self.wertvorher = wert


    def setzesichtbar(self,istsichtbar):
        self.istsichtbar = istsichtbar

    def onchange(self,callback):
        self.callback = callback



        