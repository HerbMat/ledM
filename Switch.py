import threading
import time

import RPi.GPIO as GPIO


class Switch(threading.Thread):
    switchButton = 14
    exitButton = 15

    def __init__(self, event, index_led, end_thread):
        threading.Thread.__init__(self)
        self.event = event
        self.indexLed = index_led
        self.endThread = end_thread

    def run(self):
        print('Switch started')
        GPIO.setup(self.switchButton, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.exitButton, GPIO.IN, GPIO.PUD_UP)
        while True:
            if not GPIO.input(self.switchButton):
                self.event.wait()
                print('Switch Button Pressed')
                new_index = self.indexLed.get()
                new_index += 1
                self.indexLed.put(new_index)
                print('Switch index %s' % new_index)
                time.sleep(1)
                self.event.set()
            if not GPIO.input(self.exitButton):
                print('exit Button Pressed')
                self.endThread.set()
                break
