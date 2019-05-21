# import curses and GPIO
import curses
import RPi.GPIO as GPIO
import time

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)

#for moving
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

#for claw
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

#Make sure nothing is running
GPIO.output(7,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)

#Forward function
def w():
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,True)
    GPIO.output(15,False)
    print "w"

#Backward function
def s():
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(15,True)
    print "s"

#Right function
def d():
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,True)
    print "d"

#Left function
def a():
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,True)
    GPIO.output(15,False)
    print "a"

#Stop function
def x():
    GPIO.output(7,False)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,False)
    print "x"

#Right curve function
def e():
    while screen.getch() == ord('e'):
        d()
        time.sleep(.15)
        w()
        time.sleep(1.7)
        print 'e'

#Left curve function
def q():
    a()
    time.sleep(.15)
    w()
    time.sleep(1.7)
    print 'q'

#close grippies function
def i():
    GPIO.output(32,True)
    GPIO.output(36,False)
    GPIO.output(38,True)
    GPIO.output(40,False)
    time.sleep(.15)
    GPIO.output(32,False)
    GPIO.output(36,False)
    GPIO.output(38,False)
    GPIO.output(40,False)
    print 'i'

#open grippies function
def u():
    GPIO.output(32,False)
    GPIO.output(36,True)
    GPIO.output(38,False)
    GPIO.output(40,True)
    time.sleep(.15)
    GPIO.output(32,False)
    GPIO.output(36,False)
    GPIO.output(38,False)
    GPIO.output(40,False)
    print 'u'

#Main loop
try:
    while True:
        #Get key pressed
        char = screen.getch()

        # 'N' for exit
        if char == ord('n'):
            break

        # 'I' for close claws
        elif char == ord('i'):
            i()

        # 'U' for open claws
        elif char == ord('u'):
            u()

        # 'W' for forward
        elif char == ord('w'):
            w()

        # 'S' for reverse
        elif char == ord('s'):
            s()

        # 'D' for hard right
        elif char == ord('d'):
            d()

        # 'A' for hard left
        elif char == ord('a'):
            a()

        # 'E' for curve right
        elif char == ord('e'):
            e()

        # 'Q' for curve left
        elif char == ord('q'):
            q()

        # 'X' for stop
        elif char == ord('x'):
            x()

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
