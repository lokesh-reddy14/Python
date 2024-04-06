'''1.Create a function which accepts two inputs from the user and computer nCr'''
import math
def my_cnr(n,r):
  a = math.factorial(n)
  b = math.factorial(r)
  c = math.factorial((n-r))
  nCr=a/(b*c)
  print('the nCr =',nCr)

n=int(input('Enter the n:'))
r=int(input('Enter the r:'))
my_cnr(n,r)


