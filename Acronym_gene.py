'''
    16.	Program to Acronym generator for any user input (ex-input is Random memory access then output should be RMA).Example - Random number (RN)
'''
acr=input("enter the name:")
z=""
x=acr.split(" ")
for i in range(0,len(x)):
    y=(x[i])
    z += (y[0])

print("The generated Acronym :",z.upper())

"""
st=input("name: ")
x=st.split(" ")
z=""
print(x)
for i in x:
    y=i[0]
    print(y)
    z=z+y
print(z.upper())
"""