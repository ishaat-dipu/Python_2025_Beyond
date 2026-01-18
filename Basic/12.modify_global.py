# use global keyword to modify the global inside function: 
count = 0
def increase ():
    global count
    count = count +1;
    
increase() # Calling the Function
print(count)