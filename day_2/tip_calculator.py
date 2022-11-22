print("Welcome to the tip calculator!")

# User inputs bill - Converted to float
bill = float(input("What is the total bill?\n"))

# User inputs tip percentage - Converted to integer
tip_percentage = int(input("What percentage tip to you want to give?\n"))

# User inputs total people splitting the tip - Converted to integer
total_people = int(input("How many people are splitting the bill?\n"))

# Calculate tip ammount
tip_amount = (bill * tip_percentage) / 100

# Calculate total with tip
total_with_tip = bill + tip_amount

# Calulate individual total
individual_total = total_with_tip / total_people

# Print result
print(f"Each person should pay ${round(individual_total, 2)}")
