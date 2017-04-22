import pdb

class LCD(object):

	def __init__(self, betweenDigits, inputLines):
		self.betweenDigits = betweenDigits
		self.inputLines    = inputLines

	def paintDigits(self):
		print "Name : ", self.betweenDigits, ", InputLines", self.inputLines


       