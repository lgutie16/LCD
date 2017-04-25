class Processor(object):

    def between_digits(self, x):
        input_types = (int)
        if isinstance(x, input_types) and x > -1 and x < 6:
            return x
        raise ValueError('The given value is invalid, please type a number'+
                         ' between 0 and 5')

    def input_lines(self, line):		
        if ',' not in line:
            raise ValueError('The format of you input is wrong, please type two'+
                             ' numbers separated with coma, ex: 8,332')
        else:
            vector = line.split(',')
            if len(vector) != 2 or vector[0] == '' or vector[1] == '':
                raise ValueError('The given value is invalid, please type a '+
                                 'number between 0 and 5')
            else:
                vector[0] = int(vector[0])
                if(vector[0] < 1 or vector[0] >10):
                    raise ValueError('The size should be a number between 1 and 10')
                vector[1] = int(vector[1])

        return vector

	

    