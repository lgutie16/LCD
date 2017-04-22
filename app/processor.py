import pdb

class Processor(object):

	def betweenDigits(self, x):
		input_types = (int)
		if isinstance(x, input_types) and x > -1 and x < 6:
			return x
		raise ValueError

	def inputLines(self, line):		
		if ',' not in line:
			raise ValueError
		else:
			vector = line.split(',')
			if len(vector) != 2 or vector[0] == '' or vector[1] == '':
				raise ValueError

		vector[0] = int(vector[0])
		vector[1] = int(vector[1])
		return vector

	

    