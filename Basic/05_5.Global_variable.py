"""We can represent global variables in two ways:
   1. Declaring the same variable with different values
   2. Using a local variable outside and a global variable inside
"""

# Remove the first assignment of x
x = 40
print(x)

# Here the last updated print will be printed and every variable is global.

# Using the function
x = "Awesome"  # global variable
def print_global_variable():
    print("Python is " + x)
    
print_global_variable()  

# We can use "global" variable inside the function to make it global
def modify_global_variable():
    global x
    x = "fantastic"

modify_global_variable()  # This call modifies the global variable x 
print("Python is " + x)
