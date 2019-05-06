import numpy as np
import curses
from random import randint

class Obstacle:
	def __init__(rows : int, columns : int):
		# Knowing the window size, generate random shape
		# First just generate a square
		self.__bricks = 25
		self.__shape = "square" # later could be random, circle, triangle, etc
		self.__y = [5,6,7,8,9]
		self.__x = [2,3,4,5,6]
	def __repr__():
		return "Obstacle of shape {:}".format(self.__shape)
	def square_coordinate(self, i : int):
		if i >= self.__bricks or i < 0:
			return 0, 0
		else:

		

