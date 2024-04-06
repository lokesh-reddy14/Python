#1.Write a python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

import re
pattern="^[A-Za-z0-9_-]*$"
string=input ("Enter the string--")
result=re.match (pattern, string)
if result:
  print ("Match is found (The given string contains set of charactershaving A-Z,a-z,0-9)")
else:
  print ("No Match")
