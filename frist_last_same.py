'''
18.	Program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings Sample List : ['abc', 'xyz', 'aba', '1221']	Expected Result : 2

'''
x=[]
count=0
num=int(input("enter the length of list:"))
for i in range(0,num):
    num1=input()
    x.append(num1)
print(x)
for i in range(0,num):
    y=(x[i])
    
    z=len(y)
    
    if (y[0])==(y[z-1]):
        count= count+1
print(count)

