print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = int(input("How many people to split the bill? "))

tip_as_float = float("1." + tip.replace(".", ""))
result = round((bill * tip_as_float) / num_people, 2)

print(f"Each person should pay: ${result}")
