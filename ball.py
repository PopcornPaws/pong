import numpy as np
import curses
from .racket import Racket

class Ball:
	def __init__(self, coord : np.array(2), speed : np.array(2)):
		self.__x = coord[0]
		self.__y = coord[1]
		self.__vx = speed[0]
		self.__vy = speed[1]
		self.__color = 1 # Color key 1 (green)

	def __repr__(self):
		return "Ball with coordinates of x = {:}, y = {:} and speed of vx = {:}, vy = {:}".format(self.__x, self.__y, self.__vx, self.__vy)

	def bounce(self, rows : int, columns : int, racket : Racket):
		# First check if bounced from wall
		if self.__x <= 0:
			self.__vx = -self.__vx
		elif self.__x >= columns - 1:
			for item in range(racket.length()):
				if self.__y == racket.top() + item:
					self.__vx = -self.__vx
					return 0 # If bounced from racket, return 0
			return 1
		if self.__y <= 1 or self.__y >= rows - 2:
			self.__vy = -self.__vy
		return 0

	def move(self):
		self.__x = self.__x + self.__vx
		self.__y = self.__y + self.__vy

	def pos(self):
		return self.__x, self.__y

	def vel(self):
		return self.__vx, self.__vy

	def draw(self, window):
		window.addch(self.__y, self.__x, '*', curses.color_pair(self.__color))