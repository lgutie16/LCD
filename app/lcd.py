import pdb

class LCD(object):
	"""A representation of LCD screen.

    :param between_digits: An int, the spaces between digits.
    :param input_lines: A vector of int values with length 2, representing the
                       size and number to be painted.
    """

	def __init__(self, between_digits, input_lines):
		self.between_digits = between_digits
		self.input_lines   = input_lines
		self.VERTICAL      = '|'
		self.HORIZONTAL    = '-'
		self.matrix		   = [[]]
		self.seg_list      = []
		self.current_size  = 0
		self.fixed_points  = {10: 0, 11: 0, 20: 0, 21: 0, 30: 0, 31: 0, 40: 0, 
		                      41: 0, 50: 0, 51: 0,} 

		self.options       = {0: self.zero, 1: self.one, 2: self.two, 3: self.three, 
		                      4: self.four, 5: self.five, 6: self.six, 7: self.seven,
		                      8: self.eight, 9: self.nine,}

		self.seg_options  =  {1: self.add_seg_1, 2: self.add_seg_2, 3: self.add_seg_3, 
		                      4: self.add_seg_4, 5: self.add_seg_5, 6: self.add_seg_6, 
		                      7: self.add_seg_7,}


	def paint_line_X(self, point_1, point_2):
		for x in xrange(self.current_size):
			i = point_2+x+1
			j = point_1
			print 'X'
			print i 
			print j
			self.matrix[j][i] = self.HORIZONTAL

	def paint_line_Y(self, point_1, point_2):
		for x in xrange(self.current_size):
			i = point_1+x+1
			j = point_2	
			print 'Y'
			print i
			print j
			self.matrix[i][j] = self.VERTICAL


	def add_seg_1(self):
		self.paint_line_Y(self.fixed_points[10], self.fixed_points[11])

	def add_seg_2(self):
		self.paint_line_Y(self.fixed_points[20], self.fixed_points[21])

	def add_seg_3(self):
		self.paint_line_Y(self.fixed_points[50], self.fixed_points[51])

	def add_seg_4(self):
		self.paint_line_Y(self.fixed_points[40], self.fixed_points[41])

	def add_seg_5(self):
		self.paint_line_X(self.fixed_points[10], self.fixed_points[11])

	def add_seg_6(self):
		self.paint_line_X(self.fixed_points[20], self.fixed_points[21])

	def add_seg_7(self):
		self.paint_line_X(self.fixed_points[30], self.fixed_points[31])

	def zero(self):
		self.seg_list.append([1,2,3,4,5,7])

	def one(self):
		self.seg_list.append([3,4])

	def two(self):
		self.seg_list.append([5,3,6,2,7])

	def three(self):
		self.seg_list.append([5,3,6,4,7])

	def four(self):
		self.seg_list.append([1,6,3,4])

	def five(self):
		self.seg_list.append([5,1,6,4,7])

	def six(self):
		self.seg_list.append([5,1,6,2,7,4])

	def seven(self):
		self.seg_list.append([5,3,4])

	def eight(self):
	    self.seg_list.append([1,2,3,4,5,6,7])

	def nine(self):
		self.seg_list.append([1,2,34,5,7])
		
	def paint_number(self):
		for x in xrange(len(self.input_lines)):
			size = self.input_lines[x][0]
			number = self.input_lines[x][1]			
			number_len = len(str(number))
			digit_cols = size+2
			digit_rows = size*2+3
			total_cols = number_len*digit_cols+number_len*self.between_digits
			self.matrix = [[' ' for i in xrange(total_cols)] for i in xrange(digit_rows)]
			self.current_size = size

			fix_point_x = 0
			for c in map(int, str(number)):
				self.fixed_points[11] = 0 + fix_point_x
				self.fixed_points[20] = digit_rows / 2
				self.fixed_points[21] = 0 + fix_point_x
				self.fixed_points[30] = digit_rows -1
				self.fixed_points[31] = 0 + fix_point_x
				self.fixed_points[40] = digit_cols -1
				self.fixed_points[41] = digit_rows/2+fix_point_x
				self.fixed_points[51] = digit_cols -1 +fix_point_x
				self.options[c]()

				for seg in xrange(len(self.seg_list[0])):
					seg_ref = self.seg_list[0][seg]
					self.seg_options[seg_ref]()

				del self.seg_list[:]
				fix_point_x = fix_point_x + digit_cols + self.between_digits
			

			print ' ',
			for i in range(len(self.matrix[1])):
				print i,
			print
			for i, element in enumerate(self.matrix):
				print i, ' '.join(element)

			