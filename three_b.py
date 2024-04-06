#5.Write a python program that matches a string #that has an a followed by three 'b'.
import re
pattern="ab{3}?"
string=input("Enter the string--")
result=re.match (pattern, string) 
if result:
  print ("Match is found!")
else:
  print("No Match!")
