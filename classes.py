import random
import curses
import numpy as np

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

class Racket:
	def __init__(self, pos : np.array):
		self.__pos = pos
	def __repr__(self):
		return "Racket of length {:}".format(len(self.__pos))
	def move(self):
		for 
xy = [3,4]
vxy = [5,6]
ball = Ball(xy,vxy)
print(ball)
ball.move()
print(ball)
