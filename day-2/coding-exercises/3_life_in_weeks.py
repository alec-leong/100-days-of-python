age = int(input("What is your current age?"))
max_age = 90
age_difference = 90 - age
months = age_difference * 12
weeks = age_difference * 52
days = age_difference * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
