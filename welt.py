import pygame

class Welt():
	x = 0

	def zeichnen(self):
		x, y = self.screen.get_size()
		Welt.x = self.spieler.pos.x
		posx = (x-(self.spieler.pos.x%x)) - x
		self.screen.blit(self.hintergrund, (posx+x-1,0))
		self.screen.blit(self.hintergrund, (posx,0))

	def getPos():
		return Welt.x

	def __init__(self,screen,spieler):
		self.screen = screen
		self.hintergrund = pygame.image.load("Grafiken/hintergrund.png")
		self.spieler = spieler



