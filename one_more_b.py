#3.Write a python program that matches a string #that has an a followed by zero or more b's. 
import re
pattern=". *a*b?"
string=input ("Enter the string--")
result=re.match (pattern, string) 
if result:
  print ("Match is found!")
else:
  print("No Match!")
