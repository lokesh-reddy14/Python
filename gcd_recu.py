'''2.Recusive fuction to compute GCD of 2 number'''
import math

def gcd(n,r):
  a = math.gcd(n,r)
  return a

n=int(input('Enter the n:'))
r=int(input('Enter the r:'))
print(gcd(n,r))

