#lOcal Defined Inside a Function, Accessible Only inside
#Global Defined outside, accessible Everything, Everywhere

x = 10 # global

def my_func():
    x = 5 # Local
    print(x)
    
my_func() #Calling the Function -- it will give the output of 5
print(x) # it will give the output of 