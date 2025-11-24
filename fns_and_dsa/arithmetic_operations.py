def perform_operation(num1,num2,operator):
    num1 = float(input('enter the first number:'))
    num2 = float(input('enter the second number:'))
    operator = input('Enter the operation (Enter the operation (add, subtract, multiply, divide):').strip().lower()
    if(operator=='add'):
        return num1+num2
    elif(operator=='subtract'):
        return num1-num2
    elif(operator=='multiply'):
        return  num1*num2
    elif(operator=='divide'):
        if(num2==0):
            return'cannot divide by 0'
        else:
            return num1/num2

    