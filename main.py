import math
from re import A
print("Hello World!")
print(5+8)
print(5**2)
#This is a comment
'''
This is a multiline comment
'''
print(math.gcd(3,6))
e=31
e=float(e)
print(e)
e=str(445)
print(type(e))
name="    Tony    "
#strip() ignores the spaces
print(name.strip())
print("Length of string is " + str(len(name)))
#format() function
animal="dog"
action="bite"
temp="Does your {0} {1}?".format(animal,action)
print(temp)
temp=f"Does your {animal} {action}?"
print(temp)

#list
list=[61,2,3,4,6,41]
var=type(list)
list[2]=45
var=list[2]
list.append(100)
#list.insert(1,100)
var=list
print(var)
list.remove(61)
print(var)
list.pop() #end element pops out
print(var)
#to delete a specific element use del and then the index of the element
del list[3]
print(var)
list.clear()
print(var)

#tuple
a=("Ram","Sham","Lakhan")
var=a
var=type(a)
#cannot do this a[0]="Vikrant"
print(var)

#set
s1={2,2,2,2,3,3,4,5,6,2,2,2,4,56,7,8,8}
s1.add(444)
s1.update([12,22,33,44])#to add more than one value
print(s1)
print(len(s1))
s1.remove(33)#enter the element that is to be removed
#s1.discard(1111) does not give an error even if the element is not present
print(s1)
#like list : .pop, .clear, del
#and, intersection, union

#dictionary
aDict={
    "Name":"Anvita",
    "Class":"11th",
    "Marks":33
}
print(aDict)
print(aDict["Marks"])
aDict["Marks"]=36
print(aDict)
print(aDict["Marks"])#gets updated
#.pop, .del, .clear, .update 

'''
OUTPUT:-
Hello World!
13
25
3
31.0
<class 'str'>
Tony
Length of string is 12
Does your dog bite?
Does your dog bite?
[61, 2, 45, 4, 6, 41, 100]
[2, 45, 4, 6, 41, 100]
[2, 45, 4, 6, 41]
[2, 45, 4, 41]
[]
<class 'tuple'>
{33, 2, 3, 4, 5, 6, 7, 8, 12, 44, 22, 56, 444}
13
{2, 3, 4, 5, 6, 7, 8, 12, 44, 22, 56, 444}
{'Name': 'Anvita', 'Class': '11th', 'Marks': 33}
33
{'Name': 'Anvita', 'Class': '11th', 'Marks': 36}
36
'''



