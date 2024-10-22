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

#Python - Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#add any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#If there are more than one item with the specified value, the remove() method removes the first occurrence
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Remove the last item

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist

#The clear() method empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Through a List
#Print all items in the list, one by one
thislist = ["apple", "banana", "cherry"]
for X in thislist:
    print(x)
    
#List Comprehension
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Python - Sort Lists
#Sort List Alphanumerically
#List objects have a sort() method that will sort the list alphanumerically, ascending, by defaul
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function
def myfunc(n):
      return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Use the slice Operator
#You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#append list2 into list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

