import threading
import time

import RPi.GPIO as GPIO


class Led(threading.Thread):
    leds = [19, 26, 13]
    currentIndex = 0

    def __init__(self, event, index_led, end_thread):
        threading.Thread.__init__(self)
        self.event = event
        self.indexLed = index_led
        self.endThread = end_thread

    def run(self):
        print('Led started')
        for led in self.leds:
            GPIO.setup(led, GPIO.OUT)
        while True:
            print('Led index %s' % self.currentIndex)
            if self.event.is_set():
                self.event.clear()
                self.currentIndex = self.indexLed.get()
                self.indexLed.put(self.currentIndex)
                self.event.set()
            print("LED on")
            GPIO.output(self.leds[self.currentIndex % 3], GPIO.HIGH)
            time.sleep(0.5)
            print("LED off")
            GPIO.output(self.leds[self.currentIndex % 3], GPIO.LOW)
            time.sleep(0.5)
            if self.endThread.is_set():
                print('exit Button Pressed')
                break
