# Data type in python
print("Hello", "World")

Fruits = ["apple" , "Mongo" ,"Orange"]
A , B , C = Fruits
print(A)

# Here, x is a global variable because it is defined outside the function. It can be accessed outside the function.

x = 'awesome'
def Myfunc():
    x = 'fantastic'
Myfunc()
print('Python is '  + x )
#Here we print the output fantastic
x = 'awesome'
def Myfunc():
    x = 'fantastic'
    return x
x = Myfunc()
print('Python is '  + x )

#if we want to make global to any variable value show that we are using global key word

def myfunc():
    global x
    x = "Himanshu"
myfunc()
print(x)

# If i want to calculate the length of the string show that use len
txt = 'Himanshu'
print(txt[4])

# first carrecter of the string txt
print(txt[0])

