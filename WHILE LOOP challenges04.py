#WHILE LOOP challenges 04

loop = 'Y'
count = 0

while loop == 'Y':
    name = str(input("Name someone you want to invite to your party: ")).lower()
    print("")
    print(name,"has been invited.")
    print("")
    count = count + 1
    loop = str(input("Would you like to invite anyone else to the party? (Y/N): ")).upper()
    print("")
    
print("You have invited",count,"people to the party.")
