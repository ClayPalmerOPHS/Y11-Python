#FOR LOOP challenges 08

count= str(input("Which way do you want to count? Enter 'u' for up, or enter 'd' for down: "))

if count == 'u':
    topNum = int(input("What number do you want to count up to: "))
    for i in range(1,topNum+1,+1):
        print(i)
elif count == 'd':
    downNum = int(input("Enter a number below 20: "))
    for k in range(20,downNum-1,-1):
        print(k)
else:
    print("I dont understand")
