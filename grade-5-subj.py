'''7.Accepting 5 different subject marks from user and displaying the grade of the student.
'''
eng=int(input('Enter the english marks:'))
math=int(input('Enter the maths marks:'))
comp=int(input('Enter the computer marks'))
soc=int(input('Enter the social marks'))
clad=int(input('Enter the CLAD marks'))
total_marks=eng+math+comp+soc+clad
print('the total marks is:',total_marks)
avg=(total_marks/500)*100
print('the average:',avg)
if(avg>90 and avg<=100):
    print('grade is 10')
elif(avg>80 and avg <=90):
    print('grade is 9')
elif(avg>70 and avg <=80):
    print('grade is 8')
elif(avg>60 and avg <=70):
    print('grade is 7')
elif(avg>50 and avg <=60):
    print('grade is 6')
elif(avg>40 and avg <=50):
    print('grade is 5')
elif(avg>30 and avg <=40):
    print('grade is 4')
elif(avg>20 and avg <=30):
    print('grade is 3')
elif(avg>10 and avg <=20):
    print('grade is 2')
elif(avg>0 and avg <=10):
    print('grade is 1')
    