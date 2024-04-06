#4.Write a python program that matches a string that has an a followed by zero or one 'b'. 
import re
pattern="ab?"
string=input ("Enter a string--")
result=re.match (pattern, string) 
if result:
  print ("Match is found!")
else:
  print ("No Match!")
