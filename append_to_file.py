"""append text to a file and display the text"""
f=open(input("enter the name of the file: "),"a")
f.write(input("write the information: "))
f.close()
#now the line is appended 
f=open(input("enter the name of the file: "),"r")
print(f.read())