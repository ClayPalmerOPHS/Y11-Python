##WHILE LOOP challenges 03

number= int(input("Enter a number: "))

total= number

repeatLoop= 'Y'

while repeatLoop == 'Y':
    number2= int(input("Enter another number: "))
    total= number + number2
    repeatLoop= str(input("Do you want to add another number (Y/N): ")).upper()

print("")
print("The total of the numbers you entered is",total,)    
