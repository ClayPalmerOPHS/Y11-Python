#FOR LOOP challenges 09
#Clay Palmer

invites = int(input("How many people do you want to invite to your party? "))

if invites < 10:
    for i in range(invites):
        print("")
        name = str(input("Enter the name of someone you want to invite: "))
        print("")
        print(name,"has been invited")
    print("")
    print("We have invited as many people as you wanted")
else:
    print("Too many people.")
