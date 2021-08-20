pizza_sizes = {
    "S": 15,
    "M": 20,
    "L": 25
}

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = pizza_sizes[size]

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:  # size == "M" or size == "L"
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
