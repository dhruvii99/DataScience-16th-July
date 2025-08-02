#First Day

#print("Hello World")

#name="Ayush"
#print("Lenght of the name",len(name))
#name.tittle()
#reverse the string
#print(name[-1])
#print(name[::-1])
#firstname="bbbb"
#lastname=" saini"
#print(firstname+""+ lastname)
#myname="dhruvi"
#upper_case=myname.upper()
#upper_case.upper()
#print(upper_case)

#lower_case=myname.lower()
#lower_case.lower()
#print(lower_case)

#name="Dhruvi"
#myname.tittle()
#name.index()
#print=10
#print(prin

#About List
#lst=[1,2,4,7.7,"Dhruvi",0.1111]
#print("This is my list , lets seee",lst)
#print("This is my type",type(lst))
#print("len of lst:",len(lst))
#print(lst[0])
#no gap works here !
#slicing is done here!
#print(lst[0:5])

#operations to perform
#lst.append(1000) #add element last to the list so we know this !
#print(lst)
#lst.clear() #It makes list clear at one single time 
#print(lst)
#lst.count(1)
#print(lst)
#lst.insert(0,500) #add element in the last 
#print(lst)
#Pop - to remove element from the list
#lst.insert(1,100)
#print(lst)

#TASK (HW)
#lst=[1,2,5,2,5,5[1,5,1,5,2[8,54,8]]]
#print(lst)

# ✅ Creating a tuple with mixed data types (integers and strings)
tpl = (1, 2, 3, 4, "Dhruvi", "Dhruvi")  # syntax of tuple

# ✅ Printing the tuple
print("Printing tuple:", tpl)

# ✅ Checking type of tpl (should be <class 'tuple'>)
print("Type of tpl:", type(tpl))

# ✅ Length of tuple (number of elements)
print("Length of tpl:", len(tpl))

# ✅ Accessing elements by index
print(tpl[0])   # first element (1)
print(tpl[4])   # fifth element ("Dhruvi")

# ✅ Slicing the tuple (prints elements from index 0 to 6 - up to but not including 7)
print(tpl[0:7]) # here index 7 is out of bounds, but slicing ignores it safely

# ✅ Tuple unpacking — the number of variables must match the number of values
a, b, c, d = (9, 1, 6, 8)
print(a)  # 9
print(b)  # 1
print(c)  # 6
print(d)  # 8

# ✅ You can unpack lists too (not just tuples)
a, b, c = [9, 1, 6]
print(a)  # 9
print(b)  # 1
print(c)  # 6

# ❌ Note: You cannot add elements directly to a tuple because tuples are immutable.
# To add elements, convert the tuple to a list, modify it, then convert back:
# Example:
# lst = list(tpl)
# lst.append("new_value")
# tpl = tuple(lst)

#lst=list(tpl)
#print(lst)
#print(type(lst))
#lst.append(1000)
#tpl=tuple(lst)
#print(tpl)
#tpl = (1, 2, 'hello', 3)

#nums = [x for x in tpl if isinstance(x, (int, float))]
#print(max(nums))  # 👉 3

#membership check krna 
#tpl=(1,2,4,3,2,2,122,"Dhruvi")
#print(1 in tpl)
#print(max(tpl))
#print(min(tpl))
#print(sum(tpl))


#Dict
#key value pari contain 
#key is unique

#dct={
   # "name":"Dhruvi",
    #"Class":"2nd year",
    #"Rollno ":21
#}
#name,Class,Rollno >>>>Keys
# value :Dhruvi , 2nd year",:21
#print("This is my first dict",dct)
#print("My type is ",type(dct))
#print("len of dict is ",len(dct))
 
 #Operations on dic
#print("Dct keys are",dct.keys())
#print("DCT value are",dct.values())
#print("Items get",dct.item())
#dct['address']="jaipur"
#print(dct)

#del is used to delete key value pair for this
#del dct["name"]
#rint(dct)
#del dct["Class"]
#print(dct)

#add value in dict
#my_dict = {'a': 1, 'b': 2}

# Add new key 'c'
#my_dict['c'] = 3
#print(my_dict)

#dct['Class']="4th year"
#print(dct)

#Can we store 1 value in 1 key?
#This we will
#my_dict = {}

# Add key 'name' with value 'Dhruvi'
##my_dict['name'] = 'Dhruvi'

#print(my_dict)   # 👉 {'name': 'Dhruvi'}

#1 key can have 1 value only


#sets , unordered , unchangeable but you can add and remove from that 



#WE WILL STUDY ABOUT 



#HW copy funtion , deepcopy , update , get f , for SET-:union , intersection , subset , superset 
#HW function
#Copy function
#Copy function 

#GET
my_dict = {'x': 10}

print(my_dict.get('x'))       # 10
print(my_dict.get('y'))       # None
print(my_dict.get('y', 0))    # 0 → default value if key not found


#Operators type
#arthmetic 
#logical
#bitwise
#relational/assugnment
#membership
#identity
#comparison

#arthmetic operator
print(10 + 5)
print(10 * 5)

#assignment
x=100000
print(x)

#comparision
x=5
y=1000
print(x==y)
print(x!=y)
print(x>y)

#bitwise
print(6 & 3)
print(6 | 3)
#operators

#idenity operators
#is checks whether two variables point to the same object in memory, 
# not just whether their contents are equal.

x = ["apple", "banana"]
y = ["apple", "banana"]
#because z and x points to same object
z = x

#because x and z points to same operator 
print(x is z)  # True


print(x is y)  # False
#because x and y points to different objects 

#because x and y is equal
print(x == y)  # True


#copy and deep copy operator 
#copy
#Outer object: new
#Inner objects: same as original so it is called shallow copy
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

print(original is shallow)  # False → different outer lists
print(original[0] is shallow[0])  # True → same inner list!

#Deep Copy
#A new outer object
#And recursively copies all nested objects too.

 
#data type complete 
# operator done


#conditions statements