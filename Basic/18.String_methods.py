name = input("what is your name ?")
# Remove white space from str
name = name.strip()

# Capitalize user's name
name = name.capitalize()

# say hello to user 
print(f"Hello, {name}")

#or also we can use them in 1 
name = name.strip().title()
print(name)
