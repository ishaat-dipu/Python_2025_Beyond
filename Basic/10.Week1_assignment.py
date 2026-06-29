# 1.  Assignment Name : Maritime Voyage Planner

# 1. String Input- Captain Name
captain_name = input("Enter the captain's Name: ")

# 2. Integer Input - crew size and days at sea
crew_size = int(input("Enter the size of the crew : "))
days_at_sea = int(input("Enter the crew spending time on the sea : "))

# 3. Setting up float and boolean
total_ration_in_kg = 450.5
is_ship_repaired = True

# 4. Arithmetic operators
# Calculate how much food each sailor gets per day
rations_per_person = total_ration_in_kg / crew_size
daily_rations = rations_per_person / days_at_sea

# 5. Comparison & Logical Operators
# A safe voyage requires at least 1.5kg of food per person daily AND a repaired ship
is_voyage_safe = (daily_rations >= 1.55) and is_ship_repaired

# 6. Final Output using an f-string
print("\n" + "="*30)
print(f"Captain {captain_name}'s Voyage Report")
print("="*30)
print(f"Total Crew: {crew_size} sailors")
print(f"Daily Rations: {daily_rations} kg per person")
print(f"Clear to set sail? {is_voyage_safe}")