#The Following Example We Will include The Interpretation of BMI using if/else/elif
#If the the BMI is under 18.5 (not including), print out "Under weight"
#if the bmi is between 18.5 (including) and 25 (not including), Print "Normal Weight"
#if the bmi is 2 (including) or over , print out "Overweight"
# Formula of the bmi is bmi = weight / (height **2)

print("Welcome to the BMI Calculation for your health")
height = float(input("Please enter the value of height you want to print for yourself"))
weight = float(input("Please enter the weight for the value for your given solution"))
bmi = weight/ (height ** 2)
if bmi < 18.5:
    print("You are under Weight")
elif bmi >=18.5 and bmi <25:
    print("The weight is Normal")

else:
    print("You are Overweight")