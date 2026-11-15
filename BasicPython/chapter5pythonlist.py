"""
List id use to store the multiple item in a singlr varibale 
list created using the square brackets
"""
thisList =  ["apple" , "banana" , "cherrry" ]
print (thisList)

""" List item is ordered, chnageable, and allow duplicate values
    List items are indexed first item has indexd, the first item index is [0] and the second is [1]
    if we add new item in the list alwyes placed at the last in the list
"""

thisList1 = ["apple" , "apple" , "banana" , "cherry" , "cherry"]
print(thisList1)

"""List item data type 
list item data type any type like its store string and bool int any thing
"""

list1 = ["abc" , 34 , True , 40 , "male"]
print(list1)

""" type in python 
    From Python's perspective, list are defined as object with the data type 'list':
    <class 'list'>
"""
typechecklist = ["apple", "banana" , "cherry"]
print(type(typechecklist))


"""The list() constructor"""

thislistconstructor = list(("apple" , "banana" , "cherry"))
print(thislistconstructor) 

""" Acccess Items"""

#Print Second item of the list:
print(thislistconstructor[2])

#Negative indexing in the python 
print(thislistconstructor[-1])

""" Range of indexes 
you can specify a range of indexes by specifying where to start and where to end the range.
when specifying a range, the return value will be a new list with the specified items.
"""

thislist = ["apple" , "mango" , "kiwi" , "melon" , "orange" ,"banana" , "cheery", "orange"]
print(thislist[2:5])

"""Add List item in the list"""

listitems = ["himanshu", "Ravi","Aditya" , "adviik"]
listitems.append("navin")
print(listitems)

thislist1 = ["Apple" , "mango" ,"Banana"]
thislist1.insert(1 , "Orange")
print(thislist1)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislistfruites = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Papaya", "Pineapple", "Watermelon", "Muskmelon", "Guava", "Pomegranate", "Strawberry", "Cherry", "Kiwi"]
for i in range(len(thislistfruites)):
    print(i , "Postion of element" , thislistfruites[i])