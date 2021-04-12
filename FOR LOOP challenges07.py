#FOR LOOP challenges 07

total = 0

for i in range(0,5):
    print("")
    num = int(input("Enter a number: "))
    print("")
    add = str(input("Do you want to add that number to the total,(Y/N): ")).upper()
    if add == 'Y':
        total = total+num
    else:
        total = total

print("")
print("The total of the numbers you entered is",total)
