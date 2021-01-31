import pygame
import sys
import numpy

pygame.init()
width = 600
height = 600
red = (255,0,0)
bg_color = (28,170,156)
line_color = (23, 145, 145)
line_width = 15
board_rows = 3
board_cols = 3
circle_rad = 60
circle_width = 15
circle_color = (239, 231, 200)
cross_width = 25
space = 55
cross_color = (66, 66, 66)

screen = pygame.display.set_mode((width, height))
screen.fill(bg_color)
pygame.display.set_caption("TIC TAC TOE")
board = numpy.zeros((board_rows, board_cols))


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

def draw_figures():
	for row in range(board_rows):
		for col in range(board_cols):
			if board[row][col] == 1:
				pygame.draw.circle(screen, circle_color, (int(col * 200 + 100), int(row * 200 + 100)),circle_rad, circle_width)
			elif board[row][col] == 2:
				pygame.draw.line(screen, cross_color, (col * 200 + space, row *200 + 200 - space), (col * 200 + 200 - space, row * 200 +space), cross_width)
				pygame.draw.line(screen, cross_color, (col * 200 + space, row * 200 + space),(col * 200 + 200 - space, row * 200 + 200 - space), cross_width)

def mark_square(row, col, player):
	board[row][col] = player

def avaible_square(row, col):
	return board[row][col] == 0

def is_board_full():
	for row in range(board_rows):
		for col in range(board_cols):
			if board[row][col] == 0:
				return False
	return True

draw_lines()

player = 1

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x = event.pos[0]
			mouse_y = event.pos[1]

			clicked_row = int(mouse_y // 200)
			clicked_col = int(mouse_x // 200)

			if avaible_square(clicked_row, clicked_col):
				if player == 1:
					mark_square(clicked_row, clicked_col, 1)
					player = 2
				elif player == 2:
					mark_square(clicked_row, clicked_col, 2)
					player = 1
				draw_figures()
				print(board)
	pygame.display.update()