print("Welcome to the tip calculator!")

bill = float(input("What was your total bill? $"))
tip = int(input("How much tip would you like to give in percent? "))
people = int(input("How many people are splitting the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill_amount = bill + total_tip_amount
bill_per_person = total_bill_amount / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")


