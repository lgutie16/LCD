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
		self.VERTICAL      = "|"
		self.HORIZONTAL    = "-"
		self.seg_list      = []
		self.fixed_points  = {10: 0, 11: 0, 20: 0, 21: 0, 30: 0, 31: 0, 40: 0, 
		                      41: 0, 50: 0, 51: 0,} 

		self.options       = {0: self.zero, 1: self.one, 2: self.two, 3: self.three, 
		                      4: self.four, 5: self.five, 6: self.six, 7: self.seven,
		                      8: self.eight, 9: self.nine,}

		self.seg_options  =  {0: self.add_seg_1, 1: self.add_seg_2, 2: self.add_seg_3, 
		                      3: self.add_seg_4, 4: self.add_seg_5, 5: self.add_seg_6, 
		                      6: self.add_seg_7,}


	def paint_digits_X(self, matrix, digit, size, start_point):
		for x in xrange(size):
			i = start_point[1]+x
			j = start_point[0]
			matrix[j][i] = line_character

	def paint_digits_Y(self, matrix, digit, size, start_point):
		for x in xrange(size):
			i = start_point[0]+x
			j = start_point[1]
			matrix[i][j] = line_character


	def add_seg_1(self):
		print self.seg_list

	def add_seg_2(self):
		print self.seg_list

	def add_seg_3(self):
		print self.seg_list

	def add_seg_4(self):
		print self.seg_list

	def add_seg_5(self):
		print self.seg_list

	def add_seg_6(self):
		print self.seg_list

	def add_seg_7(self):
		print self.seg_list


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
			matrix = []
			size = self.input_lines[x][0]
			number = self.input_lines[x][1]			
			number_len = len(str(number))
			digit_cols = size+2
			digit_rows = size*2+3
			total_rows = number_len*digit_cols+number_len*self.between_digits

			fix_point_x = 0
			for c in map(int, str(number)):
				self.fixed_points[11] = fix_point_x
				self.fixed_points[20] = digit_rows / 2
				self.fixed_points[21] = 0 + fix_point_x
				self.fixed_points[30] = digit_rows -1
				self.fixed_points[31] = 0 + fix_point_x
				self.fixed_points[40] = digit_cols -1
				self.fixed_points[41] = digit_rows/2+fix_point_x
				self.fixed_points[51] = digit_cols -1 +fix_point_x
				self.options[c]()

				for seg in xrange(len(self.seg_list)):
					seg_id = self.seg_list[seg]
					self.seg_options[seg_id]()

				fix_point_x = fix_point_x + digit_cols + self.between_digits