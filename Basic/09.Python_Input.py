# """1.Input Function"""
# name = input("Enter your name: ")
# print("Hello " + name)

# """2. The Type Trap (Why int() is necessary)"""
# # Bad Example
# age1 = input("Enter your age: ")
# print("My age is " + age1) # but ultimately it is returning the number as string not an actual digit
# # To get the actual digit we use int(input()) -- it locks in to give the input of integer
# age2 = int(input("Enter your real age"))
# print(f"My real age is {age2}")

# # Task - small
# # Write a program: ask name & age, print a greeting
# name1 = input("Enter your name")
# age3= int(input("how old are you"))
# print(f"Greeting {name1} you are eligible to enter as your age is {age3}")

# # Task 1: Basic Input
# game = input("Enter the name of the game :")
# print(f"oh the game named {game} is a great game  ")

# # Task 2 : wrapping int
# apex_level = int(input("Enter the level of your next apex level : "))
# print(f"your next apex level will be : {apex_level}, so grind hard tonight")

# Task 3 : 
name4 = input("Please enter your User name : ")
age6 = int(input("Enter the age you wanna type : "))
print(f"Hello {name4}, you are {age6} years old!")