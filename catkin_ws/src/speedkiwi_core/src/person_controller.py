#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import curses

def main():
    """Publishes a movement command based on user input.
    
    The robot will listen for movement commands on the 'move_command' topic.
    This is a text-based user interface that allows us to manually move the
    robot, by publishing to this topic.
    """
    rospy.init_node('person_controller', anonymous=True)
    cmd_publisher = rospy.Publisher('move_command', String, queue_size=10)

    # get the curses screen window
    screen = curses.initscr()     
    # turn off input echoing
    curses.noecho()
    # respond to keys immediately (don't wait for enter)
    curses.cbreak()
    # map arrow keys to special values
    screen.keypad(True)

    try:
        while True:
            cmd = screen.getch()
            if cmd == ord('q'):
                break
            elif cmd == curses.KEY_RIGHT:
                # print doesn't work with curses, use addstr instead
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
                screen.addstr(0, 0, 'Please use the arrow keys.')
                continue

            if cmd == 'up' or cmd == 'down' or cmd == 'left' or cmd == 'right':
                cmd_publisher.publish(cmd)
    finally:
        # shut down cleanly
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()

if __name__ == '__main__':
    main()