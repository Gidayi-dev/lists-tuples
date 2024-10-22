#Python Lists
#Lists are used to store multiple items in a single variable.
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist)) #List Length
print(type(mylist)) #type() <class 'list'>

#The list() Constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

set_data = {1, 2, 3}
set_list = list(set_data)
print(set_list)  # Output: [1, 2, 3]

#Python - Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing
#-1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["appl", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
    print("not on the list")
    
#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" #Change the second item:
print(thislist)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #Insert "watermelon" as the third item
print(thislist)