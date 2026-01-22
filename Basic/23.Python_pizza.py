print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# Todo: Work out How much They Need to pay based on their size choice
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 50
else:
    print("you Are not Valid")

# Todo : Workout How much to add to their bill based on their pepperoni chocie
if pepperoni == "Y":
    if pepperoni == "S":
        bill += 2
    else:
        bill += 3


if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

print(f"Your Final Bill is: ${bill}.")