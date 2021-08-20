def is_leap_year(year):
    flag = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                flag = True
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            flag = True
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

    return flag


if __name__ == "__main__":
    year = int(input("Which year do you want to check? "))
    is_leap_year(year)
