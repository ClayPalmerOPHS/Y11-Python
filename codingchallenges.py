#Welcome 
print("Welcome to the game! We hope you enjoy your time playing. Please register a new account")

#Registration
age=int(input("Please enter your age: "))
gender=str(input("Please enter your gender: "))
emailAdd=str(input("Please enter your email address: "))
playerName=str(input("Please enter your player name: "))

#Checking if details are correct
print("")
print("Thank you")
print("")
print("Are these registration details correct?")
print("age=",age)
print("Gender= ",gender)
print("Email address =",emailAdd)
print("Player name=",playerName)
print("")
correct=input("Please enter 'Y' (yes) or 'N' (no), regarding the accuracy of your registration details: ").upper()

#Response to detail check
print("")
if correct == 'Y':
    print("Thank you for registering with us! We hope you enjoy your stay!")
else:
    print("Please re-enter your registration details")
    age=int(input("Please enter your age: "))
    gender=str(input("Please enter your gender: "))
    emailAdd=str(input("Please enter your email address: "))
    playerName=str(input("Please enter your player name: "))
    print("")
    print("Thank you")
    print("")
    print("Are these registration details correct?")
    print("age=",age)
    print("Gender= ",gender)
    print("Email address =",emailAdd)
    print("Player name=",playerName)
    print("")
    correct=input("Please enter; 'Y' (yes) or 'N' (no), regarding the accuracy of your registration details: ").upper()

