# Check if "free" is present in the text
txt = " The Best things in Life are free!"
if "free" in txt:
    print("Yes, 'Free' is present.")

# Check if "expensive" is NOT present in the text
txt = " The Best things in Life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Check if "free" is NOT present in the text
txt = " The Best things in Life are free expensive!"
if "free" not in txt:
    print("No, 'free' is NOT present.")
else:  # Add the missing colon here
    print("Yes, 'free' is present.")