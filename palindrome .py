'''9.	Check whether the given input is a) palindrome '''
num=input("enter the number =")
i=0
for i in range(len(num)):
  if num[i]!=num[-1-i]:
    print('it is not pallindrome')
    break
  else:
    print(num,"it is pallindrome!")
    break