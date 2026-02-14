#Ask User for their name 
# We use f-string because it help us to realize that f-string can be used to to delclare the Variable in the same qoutation
name = input("What is your name?")

#say_hello_to_user
print(f"Hello, {name}")

# we cant Really use like  print("Hello, {name}") -- we have to write like print("hello" ,name)
print("hello", name)