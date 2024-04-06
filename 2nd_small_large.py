'''7.Program to find the second smallest number and second largest number in a list'''
list = []
total = int(input("Enter number of elements : "))
for i in range(0, total):
	num = int(input())
	list.append(num) 
	
print(list,'\n')
list.sort()
print("printing in acsending order:")
print(list)

print('second smallest number',list[1])
print('second largest number',list[total-2])
