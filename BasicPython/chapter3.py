#How to add the one list to another list using extand method 
fruits = ["Apple","Lemon","orange","mongo"]
tropical = ["Banana","Papaya","Pineapple","cherry"]

fruits.extend(tropical) 
print(fruits)

fruits.append("Himanshu")
print(fruits)

print(fruits.index("Lemon"))

# if you want to remove all item from the list show that we have to use fruits.clear. method  