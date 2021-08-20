from math import ceil

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = ceil(weight / (height ** 2))

if bmi <= 18.5:
    print("Your BMI is {}, you are underweight.".format(bmi))
elif bmi > 18.5 and bmi <= 25:
    print("Your BMI is {}, you have a normal weight.".format(bmi))
elif bmi > 25 and bmi <= 30:
    print("Your BMI is {}, you are slightly overweight.".format(bmi))
elif bmi > 30 and bmi <= 35:
    print("Your BMI is {}, you are obese.".format(bmi))
else:
    print("Your BMI is {}, you are clinically obese.".format(bmi))
