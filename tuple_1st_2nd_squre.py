'''8.Given a list of numbers of list, write a Python program to create a list of tuples 
having first element as the number and second element as the square of the 
number'''

list1= []
total = int(input("Enter number of elements : "))
for i in range(0, total):
	num = int(input("enter the value {} :".format(i)))
	list1.append(num) 
print(list1)

result = [(val, pow(val, 2)) for val in list1]
print(result)
    