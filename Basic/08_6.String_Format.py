# We cannot combine strings directly with numbers using '+' in Python
# Example:
"""
age = 69
txt = "My name is Ishaat" + age  # ❌ This will give a TypeError
"""

# ✅ Correct way: Use f-string for string formatting
age = 69
txt = f"{age} is just a number"
print(txt)  # Output: 69 is just a number

# wE cAN Perform Math operation inside f-string placeholders
txt = f"This is {20 *60}"
print(txt) 