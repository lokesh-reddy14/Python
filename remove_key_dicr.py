'''11.Program to remove a key from a dictionary'''

n = int(input("enter a number of value:"))
dic = {}

for i in range(n):
    keys = input() 
    values = input() 
    dic[keys] = values
print(dic)
dic.pop(input("enter the key to be removed : "))
print(dic)


