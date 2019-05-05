import curses
from curses import KEY_UP, KEY_DOWN
from random import randint
from .classes import Ball, Racket

ESCAPE = 27
ROWS = 23
COLUMNS = 79
stdscr = curses.initscr()

def main(stdscr):
	# Initialize ball and racket	
	ball = Ball([COLUMNS//2 + 1, ROWS//2 + 1],[1,randint(-2,2)]) # x - columns and y - rows
	racket = Racket(0, ROWS) # top is at y = 0, length is the number of rows
	# New curses window
	win = curses.newwin(ROWS,COLUMNS)
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)
	# Initialize color pairs
	curses.start_color()
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
	curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)
	curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)

	# Display welcome screen and wait for user input
	win.refresh()
	q = win.getch()
	win.clear()
	win.border()
	win.nodelay(True)

	while True:
		# Draw ball and racket
		ball.draw(win,1)
		racket.draw(win,2,COLUMNS - 1)
		stdscr.refresh()
		key = win.getch()
		if key == ESCAPE or key == ord('q'):
			break

	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()


if __name__ == '__main__':
	curses.wrapper(main)
