#2.Write a python program that matches a string that #has an a followed by one or more b's. 
import re
pattern=". *ab+?"
string=input ("Enter a string--")
result=re.match (pattern, string) 
if result:
  print ("Match is found!")
else:
  print ("No Match!")
