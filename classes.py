import numpy as np
import curses

class Ball:
	def __init__(self, coord : np.array(2), speed : np.array(2)):
		self.__x = coord[0]
		self.__y = coord[1]
		self.__vx = speed[0]
		self.__vy = speed[1]

	def __repr__(self):
		return "Ball with coordinates of x = {:}, y = {:} and speed of vx = {:}, vy = {:}".format(self.__x, self.__y, self.__vx, self.__vy)

	def bounce(self,signs : np.array(2)):
		self.__vx = signs[0] * self.__vx
		self.__vy = signs[1] * self.__vy

	def move(self):
		self.__x = self.__x + self.__vx
		self.__y = self.__y + self.__vy

	def pos(self):
		return self.__x, self.__y

	def vel(self):
		return self.__vx, self.__vy

	def draw(self, window, color_key):
		window.addch(self.__y, self.__x, ' ', curses.color_pair(color_key))

class Racket:
	def __init__(self, top : int = 0, length : int = 3):
		self.__top = top
		self.__len = length

	def __repr__(self):
		return "Racket at {:} of length {:}".format(self.__top, self.__len)

	def move(self, direction):
		self.__top += direction

	def draw(self, window, color_key, column):
		for item in range(self.__len):
			window.addch(self.__top + item, column, ' ', curses.color_pair(color_key)) # Draw at y = top and at given x column
