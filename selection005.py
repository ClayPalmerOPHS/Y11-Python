#Selection005

raining = str(input("Is it raining? (Yes/No) ")).lower()

if raining == 'yes':
    windy = str(input("Is it windy? (Yes/No) ")).lower()
    if windy == 'yes':
        print("It is too windy for an umbrella")
    elif windy == 'no':
        print("Take an umbrella")
    else:
        print("Invalid input, restart questions.")
elif raining == 'no':
    print("Enjoy your day")
else:
    print("Invalid input, restart questions.")
