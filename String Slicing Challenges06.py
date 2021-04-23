#String Slicing Challenges 06
#Clay Palmer

firstName = str(input("Enter your first name: "))
firstNameU = (firstName).upper()
firstNameL = (firstName).lower()


length = len(firstName)

if length < 5:
    lastName = str(input("Enter your last name: "))
    fullname = firstName + lastName
    firstName
    print(firstNameU)
else:
    print(firstNameL)
