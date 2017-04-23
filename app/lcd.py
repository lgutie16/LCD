import pdb

class LCD(object):
	"""A representation of LCD screen.

    :param betweenDigits: An int, the spaces between digits.
    :param inputLines: A vector of int values with length 2, representing the
                       size and number to be painted.
    """

    def __init__(self, betweenDigits, inputLines):
        self.betweenDigits = betweenDigits
        self.inputLines    = inputLines

    def paint_digits(self):
        print "Name : ", self.betweenDigits, ", InputLines", self.inputLines


       