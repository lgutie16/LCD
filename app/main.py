from lcd import LCD
from processor import Processor

processingData = Processor()
lineList = []
line = ''

betweenDigits = input('Space Between Digits (0,5): ')
processingData.between_digits(betweenDigits)
while line != '0,0':
    line = raw_input('Input: ')
    lineACK =  processingData.input_lines(line)
    lineList.append(lineACK)

lcd = LCD(betweenDigits, lineList)
lcd.paint_digits()
       





