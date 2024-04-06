"""Read numbers from a file and write even and odd numbers to separate files"""
f=open("even_number","w")
g=open("odd_number","w")
y=int(input("enter the range"))
for i in range(y):
  if i % 2 == 0:
    f=open("even_number","a")
    num=str(i)
    f.write(num+"\n")
    f.close
    
  else:
    g=open("odd_number","a")
    num=str(i)
    g.write(num+"\n")
    g.close


    
