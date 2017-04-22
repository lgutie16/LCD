import unittest
from app.lcd import LCD
from app.processor import Processor
 
class Test(unittest.TestCase):

	def setUp(self):
		self.processor = Processor()

	def test_betweenDigitsValues(self):
	    result = self.processor.betweenDigits(2)
	    self.assertEqual(2, result)

	def test_inputLinesCase1(self):
		self.assertRaises(ValueError, self.processor.betweenDigits, 9)

	def test_inputLinesCase1(self):
		self.assertRaises(ValueError, self.processor.betweenDigits, -4)

	def test_inputLinesCase2(self):
		self.assertRaises(ValueError, self.processor.betweenDigits, 'cadena')


	def test_inputLines(self):
	    result = self.processor.inputLines('2,2')
	    self.assertEqual([2,2], result)

	def test_inputLinesCase1(self):
		self.assertRaises(ValueError, self.processor.inputLines, 'two,')

	def test_inputLinesCase2(self):
		self.assertRaises(ValueError, self.processor.inputLines, ',two')

	def test_inputLinesCase3(self):
		self.assertRaises(ValueError, self.processor.inputLines, 'two,one')

	def test_inputLinesCase4(self):
		self.assertRaises(ValueError, self.processor.inputLines, '1,two')

	def test_inputLinesCase5(self):
		self.assertRaises(ValueError, self.processor.inputLines, 'two,2')

	if __name__ == '__main__':
		unittest.main()