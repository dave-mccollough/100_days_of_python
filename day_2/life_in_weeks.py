# Your live in weeks

age = int(input("Please input your age.\n"))

# Assume user will live to 90 years old

years_left = 90 - age

weeks_left = years_left * 52

days_left = years_left * 365


print(
    f"You have {years_left} years, {weeks_left} weeks, and {days_left} days left!")
