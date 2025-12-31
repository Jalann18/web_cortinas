print ('Ingrese un numero: ')
num1 = int(input())
print ('Ingrese otro numero: ')
num2 = int(input())
print ('Operacion? (+, -, x, /)')
op = input()
if (op == '+'):
    print (num1, '+', num2, '=', num1+num2)
elif (op == '-'):   
    print (num1, '-', num2, '=', num1-num2)
elif (op == 'x'):    
    print (num1, 'x', num2, '=', num1*num2)
elif (op == '/'):    
    print (num1, '/', num2, '=', num1/num2)
else:
    print('Operacion invalida')    
