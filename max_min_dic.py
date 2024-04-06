"""12.Program to get the maximum and minimum value in a dictionary"""

n = int(input("enter a number of value:"))
dic = {}

for i in range(n):
    keys = input() 
    values = input() 
    dic[keys] = values
print(dic)


maxi= max(dic.keys(), key=(lambda k: dic[k]))
mini = min(dic.keys(), key=(lambda k: dic[k]))

print('Maximum Value: ',dic[maxi])
print('Minimum Value: ',dic[mini])

