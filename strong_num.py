'''9.	Check whether the given input is b) strong .'''
num=int(input("enter the number="))
sum=0
temp=num
while(num):
  i=1
  fact=1
  rem=num%10
  while(i<=rem):
    fact=fact*i
    i=i+1
  sum=sum+fact
  num=num//10
if sum==temp:
  print("It is a strong number",sum)
else :
  print("it is not a strong number",sum)