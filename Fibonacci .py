'''. c) Generate Fibonacci series up to N numbers.'''
num=int(input('enter the number='))
a1=0
a2=1
a3=0
if num==0:
  print(num)
elif (num==1):
  print(num)
else:
  a3=a1+a2
  print(0)
  print(1)
  print(1)
  for i in range(3,num+1):
    a1=a2
    a2=a3
    a3=a1+a2
    print(a3)