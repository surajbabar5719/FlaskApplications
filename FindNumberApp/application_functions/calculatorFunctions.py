def getCalculatorAction(first_number,second_number,ACTION):
    if ACTION == 'ADD':
        return first_number + second_number
    if ACTION == 'SUB':
        return first_number - second_number 
    if ACTION == 'MUL':
        return first_number * second_number 
    if ACTION == 'DIV':
        return first_number / second_number 