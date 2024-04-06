'''6.program to get the difference between the two lists'''

list1 = []
total1 = int(input("Enter number of elements of list 1 : "))
for i in range(0, total1):
	num = int(input())
	list1.append(num) 
	
print(list1)
list2 = []
total2 = int(input("Enter number of elements of list 2 : "))
for i in range(0, total2):
	num = int(input())
	list2.append(num) 
	
print(list2)

diff =[]
if total1==total2:
  for i in range(0,total1):
    n=list1[i]-list2[i]
    diff.append(n)
  print('The  difference between the two lists \n',diff)
else:
  print("Invalid")
    