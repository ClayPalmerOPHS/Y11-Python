number = int(input("Enter a number between 10 and 20: "))

while number < 10 or number > 20:
    if number < 10:
        print("Your number is too low")
        number = int(input("Enter a number between 10 and 20: "))
    elif number > 20:
        print("Your number is too high")
        number = int(input("Enter a number between 10 and 20: "))
    else:
        print("Invalid entry")

print("Thank you")
