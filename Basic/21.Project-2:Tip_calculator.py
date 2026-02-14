print("Welcome to the tip calculator!")
bill = float(input("What was the total bill ? $"))
tip = int(input("What percentage tip would you like to give ? 10 12 15"))
people = int(input("How many people you wanna split the bill? "))
tip_dibo = tip/100
total_tip = bill* tip_dibo
total_bill = bill + total_tip
bill_per_person = total_bill / people
print("The Bill will be : ", round(bill_per_person,2))