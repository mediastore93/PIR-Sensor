#!/usr/bin/env python

# Import required Python libraries
import time
import RPi.GPIO as GPIO
import datetime
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO to use on Pi
GPIO_PIR = 4
 
print "PIR Module Holding Time Test (CTRL-C to exit)"
 
# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo
 
Current_State  = 0
Previous_State = 0
 
try:
 
  print "Waiting for PIR to settle ..."
 
  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0
 
  print "  Ready"
 
  # Loop until users quits with CTRL-C
  while True :
 
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
 
    if Current_State==1 and Previous_State==0:
	# PIR is triggered
	start_time=time.time()
	time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	print "  Motion detected @ %s !" % time_now
	# Record previous state
	Previous_State=1
    elif Current_State==0 and Previous_State==1:
	# PIR has returned to ready state
	stop_time=time.time()
	print "  Ready ",
	Previous_State=0

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()
