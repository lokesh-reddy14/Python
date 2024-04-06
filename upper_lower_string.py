"""17.	Python function that accepts a string and calculates the number of uppercase letters and lowercase letters"""

print("enter the stament :")

line=input()

upper = sum(1 for i in line if i.isupper())
low = sum(1 for i in line if i.islower())
print( "Number of Uppercase letter :",(upper))
print("Number of Lowercase letter :",(low))
