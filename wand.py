import pygame 
from shared import *
from welt import Welt


class Wand(pygame.sprite.Sprite):
	wandliste = []

	def __init__(self,screen,x,y):
		super().__init__()
		self.pos = vec(x,y)
		self.screen = screen
		self.istgebaut = False
		self.hoehe = 91
		self.breite = 5
		self.rect = pygame.Rect(x,y,self.breite,self.hoehe)
		self.sichtbar = True
		print("neue wand", Wand.wandliste)
		Wand.wandliste.append(self)

	def zeichnen(self):
		self.rect.x = self.pos.x #- self.breite/2
		self.rect.y = self.pos.y
		if not self.sichtbar:
			return

		if self.istgebaut:
			pygame.draw.rect(self.screen,(240,100,0), (self.rect.x - self.breite / 2 + BREITE/2 - Welt.getPos(), self.rect.y, self.rect.width, self.rect.height))
		else:
			surface = pygame.Surface((self.rect.width,self.rect.height))
			surface.set_alpha(128)
			surface.fill((100,100,100))
			self.screen.blit(surface, (self.rect.x-self.breite/2,self.rect.y))

	def setzex(self, x):
		self.pos.x = x 

	def setzey(self, y):
		self.pos.y = y 

	def setzeyvonboden(self,y):
		self.pos.y = y-self.hoehe

	def bauen(self):
		self.istgebaut = True
		#self.pos.x = Welt.getPos()

	def setsichtbar(self,sichtbar = True):
		self.sichtbar = sichtbar

	def togglesichtbar(self):
		self.sichtbar = not self.sichtbar






