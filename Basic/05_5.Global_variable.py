"""We can Represent Global Variable in 2 Ways :
   1. Declaring the same variable  with Different value or Strong 
   2. Using local variable outside and Global variable inside
"""

#1
x= 20
x= 40
print(x)

#Here The last updated Print will be printed and Every Variable is Global variabble Here

# using The Function

x = "Awesome" #global variable
def myfunc():
    print("Python is" + x)
    
myfunc()  


# we can use "global" variable inside the function to make it global

def myfunc():
    global x
    x = "fantastic"
myfunc()   #This Call modifies the global variable x 

print("Python is" + x)



 
 