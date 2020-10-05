#Values
entry=10
uk=1
us=1.5
au=2
e=35
c=20

#Welcome message

print("Welcome to the online registration for popular card game, 'You dunn know'")

#Detail entry
emailAddress=str(input("Please enter your email address: "))
skill=str(input("Please enter your skill level, 'E' (Expert) or 'C' (Casual): ")).upper()
country=str(input("Please enter your country as either 'US' , 'UK' or 'AU': ")).upper()

#Calculator
def calculator():
    if country == 'US':
        if skill == 'E':
            price=entry + (us*e)
            print("")
            print("You have to pay USD",price,"to enter")
        else:
            price=entry + (us*c)
            print("")
            print("You have to pay USD",price,"to enter")
    elif country == 'AU':
        if skill == 'E':
            price=entry + (au*e)
            print("")
            print("You have to pay AUD",price,"to enter")
        else:
            price=entry + (au*c)
            print("")
            print("You have to pay AUD",price,"to enter")
    else:
        country == 'UK'
        if skill == 'E':
            price=entry + (uk*e)
            print("")
            print("You have to pay GBP",price,"to enter")
        else:
            price=entry + (uk*c)
            print("")
            print("You have to pay GBP",price,"to enter")

calculator()   
