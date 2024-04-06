'''8.	Printing all even numbers, odd numbers, count of even numbers, count of odd numbers within a given range.'''
num=int(input('enter the range:'))
count1=0
print('For even numbers:-')
for x in range(0, num):
  if x%2==0:
   print(x)
   count1=count1+1

count2=0
print('For odd numbers:-')
for x in range(0, num):
  if x%2!=0:
   count2=count2+1
   print(x)

print('The number of even numbers are:',count1)
print('The number of odd numbers are:',count2)


