from math import pi, cos, sin, tan, asin, acos, atan

def to_rad(ang):
	return ang*pi/180

class Braco:
	def __init__(self, width, height, draw, line):
		self.width  = width
		self.height = height
		self.r1 = int(width/2.3) - 300
		self.r2 = int(width/2.3) - 300

		self.pos_fixa  = [400 , height//2]
		self.pos_move  = [400 + self.r1, height//2]
		self.pos_print = [400 + self.r1+self.r2, height//2]

		draw(self.pos_fixa[0]-20, self.pos_fixa[1]-20, 
				self.pos_fixa[0]+20, self.pos_fixa[1]+20, fill = 'black', tag = 'fixo')
		
		draw(self.pos_move[0]-20, self.pos_move[1]-20, 
				self.pos_move[0]+20, self.pos_move[1]+20, fill = 'black', tag = 'move')

		line(self.pos_fixa, self.pos_move, self.pos_print, width = 5, fill = 'black', tag = 'move')

	def atualiza(self, draw, line, delete, s1, s2):
		self.pos_move[0] = 400 + self.r1*cos(to_rad(s1))
		self.pos_move[1] = self.height//2 + self.r1*sin(to_rad(s1))

		self.pos_print[0] = 400 + self.r1*cos(to_rad(s1)) + self.r2*cos(to_rad(s2-s1))
		self.pos_print[1] = self.height//2 + self.r2*sin(to_rad(-s2+s1)) + self.r1*sin(to_rad(s1))

		delete('move')

		draw(self.pos_move[0]-20, self.pos_move[1]-20, 
				self.pos_move[0]+20, self.pos_move[1]+20, fill = 'black', tag = 'move')

		line(self.pos_fixa, self.pos_move, self.pos_print, width = 5, fill = 'black', tag = 'move')

		draw(self.pos_print[0]-1, self.pos_print[1]-1, 
				self.pos_print[0]+1, self.pos_print[1]+1, fill = 'black')

