#WHILE LOOP challenges 05

compnum = 50
guess = int(input("Enter a number: "))
count = 1
anotherGuess = 'Y'

while guess != compnum:
    while anotherGuess == 'Y':
        if guess < compnum:
            print("Your guess is too low")
            anotherGuess = str(input("Do you want another guess? (Y/N): ")).upper()
            guess = int(input("Enter another number: "))
            count = count + 1
        elif guess > compnum:
            print("Your guess is too high")
            anotherGuess = str(input("Do you want another guess? (Y/N): ")).upper()
            guess = int(input("Enter another number: "))
            count = count + 1
        else:
            anotherGuess = 'N'

print("")
print("Well done! You guessed the number in",count,"attempts.")
