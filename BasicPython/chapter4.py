fruits = ["apple", "banana", "pineapple","papaya","orange"]

for x in fruits:
    print(x)

i=0
while i < len(fruits):
   print(fruits)
   i = i+1

#[print(z) for z in fruits]
print(fruits.reverse())

#match in the python 
day = 8
match day :
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("Sunday")
    case _:
        print("I am sorry dude i am not able to find")