# Convert inputs to float immediately after receiving them
height_str = input("Enter the value of Height you want (in meters): ")
weight_str = input("Enter the value of weight you want for now (in kg): ")

height = float(height_str)
weight = float(weight_str)

# Calculate BMI using floats and parentheses for clarity
bmi = weight / (height ** 2)

print("Your Exact BMI will be : ", bmi)
