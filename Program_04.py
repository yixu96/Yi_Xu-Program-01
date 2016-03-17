project 1
def simpleExpressionIsValid(stringin):
    operators = ['+', '-', '*', '/']
    for i in operators:
        n = i in stringin
        if n == True:
            lis = stringin.split(i)

            for j in lis:
                if j != '':
                    m = j.isdigit()
                else:
                    m = 'False'
                    break

            if n == True and m == True:
                n = True
            else:
                n = False
            break
    return n


project 2
def evaluateSimpleExpression(stringin):
    operators = ['+', '-', '*', '/']

    for i in operators:
        op = stringin.find(i)
        if op != -1:
            digit = stringin.split(i)
            result = eval('%d%s%d'%(float(digit[0]), i, float(digit[1])))

    stringout = stringin + ' = ' + str(result)
    return result, stringout


project 3
while (True):
    strin = input('Enter a simple expression: ')

    if strin == 'end':
        break

    v = simpleExpressionIsValid(strin)

    if v == True:
        re, out = evaluateSimpleExpression(strin)
        print(out)
    else:
        print('invalid expression')


project 4
listofexpr = []

while (True):
    strin = input('Enter a simple expression: ')

    if strin == 'end':
        break

    v = simpleExpressionIsValid(strin)

    if v == True:
        res, expr = evaluateSimpleExpression(strin)
        listofexpr.append(expr)
    else:
        print('invalid expression')

print(listofexpr)


project 5

def simpleExpressionIsValid(stringin):
    operators = ['(', ')', '+', '-', '*', '/']

    for i in operators:
        stringin = stringin.replace(i, '')

    n = stringin.isdigit()

    return n


def evaluateSimpleExpression(stringin):
    operators = ['+', '-', '*', '/']

    for i in operators:
        op = stringin.find(i)
        if op != -1:
            digit = stringin.split(i)
            result = eval('%d%s%d'%(float(digit[0]), i, float(digit[1])))

    stringout = stringin + ' = ' + str(result)
    return result, stringout


lstofexprs = []
while (True):
    expr = input('Enter a complex expression: ')
    operators = ['(', ')', '+', '-', '*', '/']
    # lstofpartexprs = []
    lstofresults= []

    if expr == 'end':
          break
    elif expr == 'last':
        print(lstofexprs)

    v = simpleExpressionIsValid(expr)

    if v == True:
        expr1 = expr
        k = expr1.find(operators[0])

        while k!= -1:
            c = expr1.find(operators[1])
            stringin = expr1[(k+1):c]
            result, re = evaluateSimpleExpression(stringin)

            expr1 = expr1.replace(expr1[k:(c+1)], '')
            # lstofpartexprs.append(re)
            lstofresults.append(result)

            k = expr1.find(operators[0])

        finalre = eval('%d%s%d%s%d'%(float(lstofresults[0]), expr1[0], float(lstofresults[1]), expr1[1], float(lstofresults[2])))
        ex = expr + ' = ' + str(finalre)
        print(ex)
        lstofexprs.append(ex)
    else:
        print('invalid expression')



project 6

def simpleExpressionIsValid(stringin):
    operators = ['(', ')', '+', '-', '*', '/']

    for i in operators:
        stringin = stringin.replace(i, '')

    n = stringin.isdigit()

    return n


def evaluateSimpleExpression(stringin):
    operators = ['+', '-', '*', '/']

    for i in operators:
        op = stringin.find(i)
        if op != -1:
            digit = stringin.split(i)
            result = eval('%d%s%d'%(float(digit[0]), i, float(digit[1])))

    stringout = stringin + ' = ' + str(result)
    return result, stringout


lstofexprs = []
while (True):
    expr = input('Enter a complex expression: ')
    operators = ['(', ')', '+', '-', '*', '/']
    lstofresults= []

    if expr == 'end':
         break
    elif expr == 'last':
        print(lstofexprs)

    v = simpleExpressionIsValid(expr)

    if v == True:
        expr1 = expr
        k = expr1.find(operators[0])

        while k!= -1:
            c = expr1.find(operators[1])
            stringin = expr1[(k+1):c]
            result, re = evaluateSimpleExpression(stringin)

            expr1 = expr1.replace(expr1[k:(c+1)], '')
            lstofresults.append(result)

            k = expr1.find(operators[0])

        finalre = float(lstofresults[0])

        for o in range(len(expr1)):
            finalre = eval('%d%s%d'%(finalre, expr1[o], float(lstofresults[o+1])))

        ex = expr + ' = ' + str(finalre)
        print(ex)
        lstofexprs.append(ex)
    else:
        print('invalid expression')
