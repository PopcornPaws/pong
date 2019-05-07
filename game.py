import curses
from curses import KEY_UP, KEY_DOWN
import random
import time
from .ball import Ball
from .racket import Racket
from .obstacle import Obstacle

ESCAPE = 27
ROWS = 23
COLUMNS = 79
stdscr = curses.initscr()

def main(stdscr):
	# Initialize ball racket and obstacle	
	ball = Ball([COLUMNS//2, ROWS//2],[random.choice(1,2),random.choice(-2,-1,1,2)]) # x - columns and y - rows
	racket = Racket(2, 6) # top is at y = 0, length is the number of rows
	obstacle = Obstacle(ROWS,COLUMNS)
	# New curses window
	win = curses.newwin(ROWS,COLUMNS)
	curses.noecho()
	curses.cbreak()
	win.keypad(True)
	curses.curs_set(False)

	# Initialize color pairs
	curses.start_color()
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
	curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
	curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)
	curses.init_pair(4, curses.COLOR_RED, curses.COLOR_CYAN)

	# Display welcome screen and wait for user input
	win.clear()
	win.border()
	win.addstr(ROWS//2, COLUMNS//2 - 10, "Press any key to start!", curses.color_pair(4))
	win.refresh()
	q = win.getch()
	win.nodelay(True)

	while True:
		# Draw ball and racket
		win.clear()
		#win.border()
		ball.draw(win)
		racket.draw(win,COLUMNS - 1)
		obstacle.draw(win)
		key = win.getch()
		if key == ESCAPE or key == ord('q'):
			break
		elif key == curses.KEY_UP:
			racket.move(ROWS, -1)
		elif key == curses.KEY_DOWN:
			racket.move(ROWS, 1)

		ball.move()
		if ball.bounce(ROWS, COLUMNS, racket, obstacle):
			win.addstr(ROWS//2,COLUMNS//2,"You lost!",curses.color_pair(4))
			time.sleep(2)
			break
		win.refresh()
		time.sleep(.2)

	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()


if __name__ == '__main__':
	curses.wrapper(main)
