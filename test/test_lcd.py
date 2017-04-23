import unittest
from app.lcd import LCD
from app.processor import Processor
 
class Test(unittest.TestCase):

    def setUp(self):
        self.processor = Processor()

    def test_space_between_digits_values(self):
        result = self.processor.between_digits(2)
        self.assertEqual(2, result)

    def test_space_between_digits_values_major_value_case(self):
        self.assertRaises(ValueError, self.processor.between_digits, 9)

    def test_space_between_digits_values_negative_value_case(self):
        self.assertRaises(ValueError, self.processor.between_digits, -4)

    def test_space_between_digits_values_string_value_case(self):
        self.assertRaises(ValueError, self.processor.between_digits, 'five')

    def test_input_lines(self):
        result = self.processor.input_lines('2,2')
        self.assertEqual([2,2], result)

    def test_input_lines_string_coma_case(self):
        self.assertRaises(ValueError, self.processor.input_lines, 'two,')

    def test_input_lines_coma_string_case(self):
        self.assertRaises(ValueError, self.processor.input_lines, ',two')

    def test_input_lines_string_coma_string_case(self):
        self.assertRaises(ValueError, self.processor.input_lines, 'two,one')

    def test_input_lines_int_coma_string_case(self):
        self.assertRaises(ValueError, self.processor.input_lines, '1,two')

    def test_input_lines_string_coma_int_case(self):
        self.assertRaises(ValueError, self.processor.input_lines, 'two,2')

    def test_input_lines_no_in_range_value_major_case(self):
        self.assertRaises(ValueError, self.processor.input_lines, '11,2')

    def test_input_lines_no_in_range_value_minor_case(self):
        self.assertRaises(ValueError, self.processor.input_lines, '-2,2')

    if __name__ == '__main__':
        unittest.main()