#!/usr/bin/python
import RPi.GPIO as GPIO
import subprocess
import time

def wgetIt(wgetUrl):
	subprocess.call(['wget', '-O', '/dev/null' , wgetUrl])

# set the server IP OR hostname here!
remoteServer = '192.169.1.1'

wgetOnBoot = 'http://'+ remoteServer +'/bell/play.php?b=booted'
wgetOnBell = 'http://'+ remoteServer +'/bell/play.php?b=doorBell'


# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel
GPIO.setup(12, GPIO.OUT)

# set RPi board pin 12 high
GPIO.output(12, GPIO.HIGH)

# set up GPIO input with pull-up control
#   (pull_up_down be PUD_OFF, PUD_UP or PUD_DOWN, default PUD_OFF)
#GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )

# input from RPi board pin 11
#input_value = GPIO.input(11)

# send a booted
wgetIt(wgetOnBoot)

# initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0
inputCount = 0
emptyTripCount = 0


# we have to detect ON-OFF-ON.. falshing of the bell-light
# because sometimes it trigers itsef (hardware bug in my optocoppler foo, not raspys fault!)
flashDetection = False


while True:
	# take a reading
	inp = GPIO.input(11)
	
	#print inp
	
	# if the last reading was low and this one high, do stuff
	if ((not prev_input) and inp):
		# reset empty trips
		emptyTripCount = 0
		inputCount += 1
		
		if flashDetection == True:
			# only if X changes detected do something
			if inputCount >= 2:
				inputCount = 0
				wgetIt(wgetOnBell)
				print 'finished playback'
		else:
				wgetIt(wgetOnBell)
				print 'finished playback'
				
	else:
		emptyTripCount += 1
		# on X empty trips reset the input counter for some magic voodoo stuff
		if emptyTripCount >= 20:
			emptyTripCount = 0
			inputCount = 0
	
	#update previous input
	prev_input = inp
	
	#slight pause to debounce
	time.sleep(0.05)

