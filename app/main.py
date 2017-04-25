from lcd import LCD
from processor import Processor

processingData = Processor()
line_list = []
between_digits = input('Space Between Digits (0,5): ')
processingData.between_digits(between_digits)

line = raw_input('Input: ')
while line != '0,0':
    line_vector =  processingData.input_lines(line)
    line_list.append(line_vector)
    line = raw_input('Input: ')

lcd = LCD(between_digits, line_list)
lcd.paint_number()
     





