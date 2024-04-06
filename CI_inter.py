'''
10.	Compute compound interest using loop for a certain principal and interest amount
'''
p=int(input("enter the principle ="))
r=float(input("enter the rate ="))
t=int(input("enter the time ="))
for i in range(t):
  c=p*(pow((1+r/100),t))
print(c)