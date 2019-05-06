import numpy as np
import curses

class Racket:
	def __init__(self, top : int = 0, length : int = 3):
		self.__top = top
		self.__len = length
		self.__color = 2 # blue color

	def __repr__(self):
		return "Racket at {:} of length {:}".format(self.__top, self.__len)

	def move(self, rows, direction : int):
		bottom = self.__top + self.__len - 1
		# If racket is between bounds
		if self.__top > 0 and bottom < rows - 2:
			self.__top += direction
		# If at border
		elif self.__top <= 0 and direction == 1:
			self.__top += direction
		elif bottom >= rows - 2 and direction == -1:
			self.__top += direction
			
	def top(self):
		return self.__top
	
	def length(self):
		return self.__len
		
	def draw(self, window, column):
		for item in range(self.__len):
			window.addch(self.__top + item, column, '_', curses.color_pair(self.__color)) # Draw at y = top and at given x column
