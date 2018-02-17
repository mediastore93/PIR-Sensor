#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import datetime

# Use BCM GPIO references
GPIO.setmode(GPIO.BCM)

GPIO_PIR = 27

print ("PIR Module Holding Time Test (CTRL-C to exit)")

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo


def sensor():

    Current_State  = 0
    Previous_State = 0

    print ("Waiting for PIR to settle ...")

    # Loop until PIR output is 0
    while GPIO.input(GPIO_PIR)==1:
        Current_State  = 0
    print ("  Ready")
    # Loop until users quits with CTRL-C
    while True :
        Current_State = GPIO.input(GPIO_PIR)
        if Current_State==1 and Previous_State==0:
    # PIR is triggered
            start_time=time.time()
            time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print (" Motion detected @ %s !" % time_now)
            # Record previous state
            Previous_State=1
        elif Current_State==0 and Previous_State==1:
            # PIR has returned to ready state
            stop_time=time.time()
            print ("  Ready "),
            Previous_State=0


def schedule():


    while True:
        timestamp = datetime.datetime.now().time()
        start = datetime.time(22, 0)
        end = datetime.time(23, 59)
        if(start <= timestamp <= end):
            print("Sensor on at " + str(timestamp))
            sensor()

        timestamp = datetime.datetime.now().time()
        start = datetime.time(0, 1)
        end = datetime.time(7, 0)

        if(start <= timestamp <= end):
            print("Sensor on at " + str(timestamp))
            sensor()
            
        else:
            print('Daytime - not sensing.')
            time.sleep(60)

try:
    schedule()
    time.sleep(1)




except KeyboardInterrupt:
    print ("  Quit")
    # Reset GPIO settings
    GPIO.cleanup()


