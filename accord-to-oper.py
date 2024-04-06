'''6.Building a mathematical calculator that can perform operations according to user input. 
Use decision making statement.'''
print('!!! it is in int values !!!')
x=int(input('enter the number1:'))
y=int(input('enter the number2:'))
op = input('enter the operation:')
if op == "+" :
 print('sum of two numbers:',x+y)
elif op=="-":
  print("subtract of two numbers:",x-y)
elif op=="*":
  print("multiply of two numbers:",x*y)
elif op=="/":
  print("dividion of two numbers:",x/y)
elif op=='%':
  print("the remanider of two is :",x % y)
else :
  print('invaild operater!')

  
print("!!! It is in float values ")
x=float(input('enter the number1:'))
y=float(input('enter the number2:'))
op = input('enter the operation:')
if op == "+" :
 print('sum of two numbers:',float(x+y))
elif op=="-":
  print("subtract of two numbers:",float(x-y))
elif op=="*":
  print("multiply of two numbers:",float(x*y))
elif op=="/":
  print("dividion of two numbers:",float(x/y))
elif op=='%':
  print("the remanider of two is :",float(x % y))



  