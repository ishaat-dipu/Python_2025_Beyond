"""We are going to see the different types of variables and data types in python"""

"""Python has lots of data types among them we have numeric, Dictionary, boolean, Set, Sequence type
   Numeric has 2 : i. Integer ii. Float and a special --  Complex data type
   Sequence type has three data type --> i. String ii. Tuple  and iii. List"""

# Lets check a data type of and integer number 
a = 46
print (a)
print(type(a)) #Type is used to represents the data type of the variable we assigned 

#So we get the <class int> which represents the integer data type here 

"""Lets check about a string data type"""
p = 'asian'
print(p)
print(type(p)) # may be we get the string type data from it lets see 
# here the < class 'str' represents the data type of string

"""Let's See the float type data"""
s = 50.24
print(s)
print(type(s)) # So it shows that it is the float data type 

"""List are mutable Collection that is used to store the multiple item in Single variable
   Lists are represents on []"""
a = [4, 5, 6]
print (a)

b =["ishaat", 6, 8, "geek"] # So be can take all data types when we use the lists
print(b) 
# lets see the data type of the list if we even can get it or not 
print(type(b))

b = ["Ragnarok", 5, 6, 9]
print(b[3])
print(b[-3])

# NB: Always remember that list is mutable or changeable

# Tuple are also collection of multiple item but unchangeable
d =  ("Roark", 2, 8 , 5, 7)
print (d)
print(type(d))
print(d[4])
print(d[-3])

e = (2,) # if we want to use the single element we need to remember that we have to use a comma for that
print(e)


"""Dictionary are use as key value pairs, each key must be unique"""
r = {1: "Ishaat" , 2: "dipu" , 3:"Geeks"}
print(r)
print(type(r))
print(r[2])

"""Practice: storing my name age, height and is student"""
u = {"name" : "ishaat", "age": 22, "height": 56 , "is_student": True}
print(u)
print(u["age"])

"""Practice Storing product_name,price , quantity_in_stock, is_available"""
store = {"product_name": "brois", "price": 20 , "quantity_in_stock": 50, "is_available":True }
print(store)
print(store["product_name"], ["is_available"])

""" NB: Python splits this into two completely independent pieces separated by the comma:

Piece 1: store["product_name"]

Python thinks: "Okay, go look inside the store dictionary and find the product name." (Result: "brois")

Piece 2: ["is_available"]

Python thinks: "Oh, here is just a brand new list containing a piece of text." Because store isn't attached to it, Python has no idea you wanted to look inside the dictionary again."""

#More_Data_Type_Simplified


# Data Type is Set when You assign a value to the Variable

# For an Example Suppose:

# Integer
x = 2
print(type(x))  # <class 'int'>

# Float
y = 3.14
print(type(y))  # <class 'float'>

# String
z = "Hello"
print(type(z))  # <class 'str'>

# List
a = [1, 2, 3]
print(type(a))  # <class 'list'>

# Tuple
b = (1, 2, 3)
print(type(b))  # <class 'tuple'>

# Dictionary
c = {"key": "value"}
print(type(c))  # <class 'dict'>

# Set
d = {1, 2, 3}
print(type(d))  # <class 'set'>

# Boolean
e = True
print(type(e))  # <class 'bool'>


#Same Just Like this We can use
a = "Hello world"
b = 20.5
c = 1j
d = ["apple", "banana", "cherry"]
e =("apple", "banana", "cherry")
f = range(6)
g = {"name": "John", "age": 30, "city": "New York" }
h = True
i = bytearray(4)
print(type (x), (a), (b), (c), (d), (e), (f), (g), (h))
