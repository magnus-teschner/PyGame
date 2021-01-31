import pygame
import sys

pygame.init()
width = 600
height = 600
#red, green, blue
red = (255,0,0)
bg_color = (28,170,156)

#width, hight
screen = pygame.display.set_mode((width, height))

#hintergrundfarbee
screen.fill(bg_color)
pygame.display.set_caption("TIC TAC TOE")
line_color = (23, 145, 145)
line_width = 15

def draw_lines():
	#1 Horizontale:
	# wo, farbe, startpunkt, endpunkt, dicke

	pygame.draw.line(screen, line_color, (0, 200), (600, 200), line_width)
	#2 Horizontale:
	pygame.draw.line(screen, line_color, (0, 400), (600, 400), line_width)
	#1 Vertikale:
	pygame.draw.line(screen, line_color, (200, 0), (200, 600), line_width)
	#2 Vertikale:
	pygame.draw.line(screen, line_color, (400, 0), (400, 600), line_width)

draw_lines()

#pygame coordinats: oben links 0,0
#y wert nimmt nach unten hin zu
#x werte nehmen ganz normal nach rechts zu

#mainloop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	pygame.display.update()