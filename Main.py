import threading

import Queue
import RPi.GPIO as GPIO

import Led
import Switch

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

indexLed = Queue.Queue()
indexLed.put(0)
event = threading.Event()
endThread = threading.Event()
event.set()

led = Led.Led(event, indexLed, endThread)
switch = Switch.Switch(event, indexLed, endThread)

switch.start()
led.start()
switch.join()
led.join()   

GPIO.cleanup()
