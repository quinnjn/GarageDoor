import time

import RPi.GPIO as GPIO

class GarageDoor:
	RELAY1 = 18
	ON = 1
	OFF = 0
	
	#Time in seconds to keep the action on.
	ACTION_TIME = 0.5

	def __init__(self):
		self.__setup()
		print "GarageDoor:Init"

	def __setup(self):
		GPIO.cleanup()
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.RELAY1, GPIO.OUT)

	def __del__(self):
		GPIO.cleanup()

	def open(self):
		self.__action()
		print "GarageDoor::Open"

	def close(self):
		self.__action()
		print "GarageDoor::Close"

	def __action(self):
		GPIO.output(self.RELAY1, self.ON)
		time.sleep(self.ACTION_TIME)
		GPIO.output(self.RELAY1, self.OFF)
