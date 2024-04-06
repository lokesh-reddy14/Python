'''4.Recursive function to generate Fibonacci series.'''
def Fibonacci(nterms):
  num1, num2 = 0, 1
  count = 0
  if nterms <= 0:
     print("invaild")
  elif nterms == 1:
     print(num1)
  else:
     while count < nterms:
         print(num1)       
         nth = num1 + num2
         num1 = num2
         num2 = nth
         count += 1


no_values = int(input("How many values= "))
Fibonacci(no_values)
