# x = 10
# y = 20
# sum = x + y
# print("The sum of ", x, "and", y, "is:", sum)

# x = input("Enter first number:")
# y = input("Enter second number:")

# sum = float(x) + float(y)
# print("The sum of ",x, "and", y, "is:" , sum)
# name = "Himanshu"
# age = 21
# print("My name is " + name + " and I am " + str(age) +" Year old.")

# text = input("Enter Your name :")
# age = input("Enter your age :")
# print("My name is " + text + "and I am " + age + "years old.")

# a = 5
# b = 2
# print("a + b =",a + b)
# print("a - b =", a - b)
# print("a * b =", a * b)
# print("a / b =", a /b)
# print("a % b =",a%b)

# age = int(input("Enter your age:"))
# if age >= 18:
#     print("You are not Eligible for voting")
# else:
#     print("You are Eligible for voting")

# name = input("Enter your name:")

# if name == "Himanshu":
#     print("Welcome Himanshu!")
# else:
#     print("You are not Himanshu") 

# value = int(input("Enter a value :"))
# if value % 2 == 0:
#     print("The value is even")
# else: 
#     print("The vale is not even")

# for i in range(5):
#     print("Iteration number:", i)

# for i in range(1, 11):
#     print("number start from one to ten:", i)

# for i in range(1, 21):
#     print("Odd numbers between 1 to 20:", i)
    
# count = int(input("Enter a number:"))
# while count > 0:
#     print("The count is:" ,count)
#     count -= 1

# nums = [1,2,3,4,5]
# print("The list of numbers are:", nums)
# nums.append(6)
# print("Update List is:", nums)
# nums.remove(3)
# print("List after removing 3 is:", nums)

# Lession functions
# def add(a,b):
#     return a + b

# result = add(5,10)
# print("The sum of a and b is:", result)

# def subtract(a,b):
#     return a-b
# result = subtract(10,5)
# print("The substaction of the vale 1 and value 3 is :", result)
    
# def PrintEvenNumbers(n):
#     even_Number = []
#     for i in range(1, n + 1):
#      if i % 2 == 0:
#         even_Number.append(i)
#     return even_Number
# result = PrintEvenNumbers(20)
# print("Even numbers between 1 to 20 are:",result)

# def check_prime(num):
#    if num > 1:
#          for i in range(2, int(num/2)+ 1):
#             if(num % i)==0:
#                 return False
#             else: 
#                 return True
# result = check_prime(17)
# print("Is 17 a Prime number?:", result)

# def check_prime(num):
#     if num > 1:
#         for i in range (2 , int(num/2) + 1):
#             if(num % i) == 0:
#                 return False
#             else:
#                 return True
# result = check_prime(17)
# print("The number is :" ,result)

# Casting in Python

# x = str(3.0)
# y = int(3)
# z = float(3)

# print("string is", str(x) ,"Integer id" , y ,"floting point value is" , z) 
# print(type(x))

# a = int("4")
# print(type(a))

# y = int(3.4)
# print(type(y))

# Multi line string in the Python
# a = """Hi My name is Himanshu Singh and i am Working as a software developer Tranee Role in Milliman and one day I will work as a  conform Employee Thanks! """
# print(a)

# Here if you want to print any perticular word then using array of any number we will print thease value 
# a = "Himanshu"
# print(a[1])

# Looping Throught the string
# a = "Himanshu"
# for i in "Khushi":
#     print(i)

# print(len(a))

# text = "Hi my name is Himanshu Singh"
# # print("himanshu" in text)
# # using if candition how we use in
# if("himanshu" in text):
#     print("Yes Himanshu is Present")
# else:
#     print("False")

# Slicing in Python

text = " Hello World "
# print(text[2:5])

# # Slice from the start

# print(text[:5])

# # Slice from the end
# print(text[5:])

# print(text[-5:-2])

# print(text.upper())
# print(text.lower())
# print(text.strip())

# print(text.replace("H" , "J"))

# Python List

# myList = ["Banana", "Apple", "Cherry","Apple","Mango","Mango"]
# print(len(myList))

# containDiffrentDataTypeList = ["value", 3,3.5,True,False,"Himanshu"]
# print(containDiffrentDataTypeList)
# print(type(containDiffrentDataTypeList))

# List Constroctor
thisList = list(("Himanshu","Ashish","Shurbhi","Shruti", "Shruti"))
# print(thisList[ 0:])
# if "Himanshu" in thisList:
#     print("Yes Himanshu is Present")
# else:
#     print("Not Present")

# thisList[1] = "Kuldeep"
# print(thisList)
# thisList[1:3] = ["blackcurrant", "watermelon"]
# thisList.append("Sheelu")
# print(thisList)

# thisList.remove("Shruti")
# print(thisList)
# print(thisList)
thisList.remove("Shruti")
print(thisList)

for i in range (0 , len(thisList)):
    print(thisList[i])