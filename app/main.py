from lcd import LCD
from processor import Processor

processingData = Processor()

betweenDigits = input('Space Between Digits (0,5): ')
if(processingData.betweenDigits(betweenDigits) != None):
    line = ''
    while line != '0,0':
        line = raw_input('Input: ')
        lineACK =  processingData.inputLines(line)
        if(lineACK != None):
            lcd = LCD(betweenDigits, lineACK)
            lcd.paint_digits()
        else:
            print "Nothing is going to be painted"





