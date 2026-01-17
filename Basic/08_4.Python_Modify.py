x = "yo This Is mY land"
print(x.upper())

y = "this iS not Lower"
print(y.lower())

#Remove Whitespace

"""TO remove white space in string we can use strip() method"""

a = " Hello World ohio "
print(a.strip())

"""NB: The Strip() method removes any whitespace from the beginning or the end of a string. Not Between them """

#Replace the String 
"""To replace the string we can use replace() method"""
r = "This is the most cruel Place"
print(r.replace("t", "z"))
""" So From here the letter t is replaced by z """

"""Also we can Replace a word """
l = "My school Name is Mymensingh Zilla School"
print(l.replace("Mymensingh", "Dhaka"))


"""We can Also use the replace method to Remove the space Between the Text"""
b = "My Name is Ishaat     Dipu"
print(b.replace("     ", " "))


"""Split String"""
#The Split() method splits a string into a list.
z = "My Name is Ishaat Dipu"
print(z.split()) #['My', 'Name', 'is', 'Ishaat', 'Dipu']

"""[ , , , , ,]""" """This Represents List"""
 