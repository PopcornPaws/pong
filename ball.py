import numpy as np
import curses
from random import randint
from .racket import Racket
from .obstacle import Obstacle

class Ball:
	def __init__(self, coord : np.array(2), speed : np.array(2)):
		self.__x = coord[0]
		self.__y = coord[1]
		self.__vx = speed[0]
		self.__vy = speed[1]
		self.__color = 1 # Color key 1 (green)
		self.__shape = '*'

	def __repr__(self):
		return "Ball with coordinates of x = {:}, y = {:} and speed of vx = {:}, vy = {:}".format(self.__x, self.__y, self.__vx, self.__vy)

	def bounce(self, rows : int, columns : int, racket : Racket, obstacle : Obstacle):
		# First check if bounced from wall
		if self.__x <= 0:
			self.__vx = -self.__vx
			return 0
		elif self.__x >= columns - 1:
			for item in range(racket.length()):
				if self.__y == racket.top() + item:
					self.__vx = -self.__vx
					return 0 # If bounced from racket, return 0
			return 1
		if self.__y <= 1 or self.__y >= rows - 2:
			self.__vy = -self.__vy
			return 0
		# Check if bounced from obstacle
		for i in range(obstacle.size()):
			if self.__x == obstacle.x(i) and self.__y == obstacle.y(i):
				obstacle.remove_brick(i)	
				self.__vx = -self.__vx
				self.__vy = randint(-2,2)
		return 0

	def move(self):
		self.__x = self.__x + self.__vx
		self.__y = self.__y + self.__vy

	def pos(self):
		return self.__x, self.__y

	def vel(self):
		return self.__vx, self.__vy

	def draw(self, window):
		window.addch(self.__y, self.__x, self.__shape, curses.color_pair(self.__color))
