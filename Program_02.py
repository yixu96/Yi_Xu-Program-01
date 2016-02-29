#Lab assignment 01
#CSC-201
#Yi Xu

import re
#Use this code to insert expression#

while (True):
#While loop, if it is ture, then print out#

    expr = input('Enter the expression: ')
    digit = re.split('\D', expr)
    #split characteror, return a list of the words of the string#

    operators = ['+', '-', '*', '/']
    #Put '+', '-', '*', '/' in operators#

    for i in operators:
        op = expr.find(i)
        #Find charactor. Use this to find i in operators#
        if op != -1:
            break
        #If you can find, then break#

    while (op == -1):
        print('There is an invalid operator. Please try again!')
        #If op equal -1, that means you put a invaild operator#
        expr = input('Enter the expression: ')
        digit = re.split('\D', expr)
        while '' in digit:
            digit.remove('')
            #Use remove charactor to remove ""#
        for i in operators:
            op = expr.find(i)
            if op != -1:
                break
            #If you can find, then break#


    op = expr.find('+')
    #Use find charactor to find "+"#

    if op != -1:
        result = float(digit[0]) + float(digit[1])
        #If op not equal -1, then we plus digit[0] and digit[1]#
    else:
        op = expr.find('-')
        if op != -1:
            result = float(digit[0]) - float(digit[1])
            ##If op not equal -1, then we minus digit[0] and digit[1]#
        else:
            op = expr.find('*')
            if op != -1:
                result = float(digit[0]) * float(digit[1])
                #If op not equal -1, then digit[0] times digit[1]#
            else:
                op = expr.find('/')
                if op != -1:
                    result = float(digit[0]) / float(digit[1])
                    #If op not equal -1, thendigit[0] divide digit[1]#
    print(expr + ' = ' + str(result))
    #At last, print the results with "="#

    break
    #Then, break the loop#
