'''a)Compute the factorial of a given number. '''
numb=int(input("Enter the number="))
fa=1
if numb>=0:
  for i in range(1,numb+1):
    fa=fa*i
print("the factorail",numb," is=",fa)