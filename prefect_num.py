'''9.	Check whether the given input is c) perfect .'''
num=int(input("enter the number="))
x=0
for i in range(1,num-1):
  r=num%i
  if r==0:
    x=x+i
if num==x:
  print("It is a perfect number",num)
else:
  print("It is not a perfect number.")