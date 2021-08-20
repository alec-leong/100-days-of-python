print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

char_counts = {}
for name in (name1, name2):
    for char in name:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

first_digit = 0
for char in "true":
    if char in char_counts:
        first_digit += char_counts[char]

second_digit = 0
for char in "love":
    if char in char_counts:
        first_digit += char_counts[char]

score = int(f"{first_digit}{second_digit}")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
