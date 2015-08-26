#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import curses


def main():
    """
    Publishes a movement command based on arrow key input.
    Used for the EducatedPerson class.

    Credits to:
    http://www.codehaven.co.uk/using-arrow-keys-with-inputs-python/
    https://github.com/hcrlab/randomwalker
    """
    rospy.init_node('person_controller', anonymous=True)
    cmd_publisher = rospy.Publisher('move_command', String, queue_size=10)

    # Get the curses screen window
    screen = curses.initscr()
    # Turn off input echoing
    curses.noecho()
    # Respond to keys immediately (don't wait for enter)
    curses.cbreak()
    # Map arrow keys to special values
    screen.keypad(True)

    try:
        while True:
            cmd = screen.getch()
            if cmd == ord('q'):
                break
            elif cmd == curses.KEY_RIGHT:
                screen.addstr(0, 0, 'right')
                cmd = 'right'
            elif cmd == curses.KEY_LEFT:
                screen.addstr(0, 0, 'left ')
                cmd = 'left'
            elif cmd == curses.KEY_UP:
                screen.addstr(0, 0, 'up   ')
                cmd = 'up'
            elif cmd == curses.KEY_DOWN:
                screen.addstr(0, 0, 'down ')
                cmd = 'down'
            else:
                screen.addstr(0, 0, 'Use the arrow keys.')
                continue

            if cmd == 'up' or cmd == 'down' or cmd == 'left' or cmd == 'right':
                cmd_publisher.publish(cmd)
    finally:
        # Shut down cleanly
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()

if __name__ == '__main__':
    main()
