# # All the string method and operation in one place 


# """1. String Declaration"""
# #String in python are surrounded by either single or Double quotes marks.
# #'Hello' is the same as "Hello"
# #You can display strings with the print() function:
# ###Example
# print("Hello")
# print('Hello')

# # We can also use quotes Inside Quotes
# #Example
# print("he is called 'Ishaat'")
# print('he is called "Ishaat"')
# # We can also use triple quotes
# #Example
# print('''Hello
# World''')
# print("""Hello
# World""")

# #Assign String to a Variable
# a = "Ishaat"
# print(a)

# #Assign String into Multi Strings
# a = """Ishaat
# Ishaat"""


# """2. String Slicing"""

# # Check if Strings are Arrays  and string slicing 
# a = "Ishaat"
# print(a[1:4]) 
# print(a[1])


# """3. String Looping"""

# # Looping Through String
# #Example
# for x in "Ishaat":
#     print(x)
    
# #String Length
# #Example
# a = "Ishaat"
# print (len(a))


# # Check if "free" is present in the text
# txt = " The Best things in Life are free!"
# if "free" in txt:
#     print("Yes, 'Free' is present.")

# # Check if "expensive" is NOT present in the text
# txt = " The Best things in Life are free!"
# if "expensive" not in txt:
#     print("No, 'expensive' is NOT present.")

# # Check if "free" is NOT present in the text
# txt = " The Best things in Life are free expensive!"
# if "free" not in txt:
#     print("No, 'free' is NOT present.")
# else:  # Add the missing colon here
#     print("Yes, 'free' is present.")



"""4. string_methods"""

x = "yo This Is mY land"
print(x.upper())

y = "this iS not Lower"
print(y.lower())

#Remove Whitespace

"""TO remove white space in string we can use strip() method"""

a = " Hello World ohio "
print(a.strip())

"""NB: The Strip() method removes any whitespace from the beginning or the end of a string. Not Between them """

#The Split() method splits a string into a list.
z = "My Name is Ishaat Dipu"
print(z.split()) #['My', 'Name', 'is', 'Ishaat', 'Dipu']

"""[ , , , , ,]""" """This Represents List"""

#Replace the String 

"""To replace the string we can use replace() method"""
r = "This is the most cruel Place"
print(r.replace("T", "z"))
""" So From here the letter t is replaced by z """

"""Also we can Replace a word """
l = "My school Name is Mymensingh Zilla School"
print(l.replace("Mymensingh", "Dhaka"))


"""We can Also use the replace method to Remove the space Between the Text"""
b = "My Name is Ishaat     Dipu"
print(b.replace("     ", " "))






"""5. concatenating the string"""

# we can add 2 Strings using + operator
a = "Hello"
b = "World"
c= "Ishaat"
print (a+b+c)

# We can Add Space so that it looks Beautiful
print (a + " "+b+ " "+ c)




# """ 6.  F-string """ 

# # We cannot combine strings directly with numbers using '+' in Python
# # Example:
# """
# age = 69
# txt = "My name is Ishaat" + age  # ❌ This will give a TypeError
# """

# # ✅ Correct way: Use f-string for string formatting
# age = 69
# txt0 = "age + is just a number"
# txt = f"{age} is just a number"
# print(txt0) # it wont print the age because we are not mentioning the string 
# print(txt)  # Output: 69 is just a number

# # wE cAN Perform Math operation inside f-string placeholders **
# txt = f"This is {20 *60}"
# print(txt) 