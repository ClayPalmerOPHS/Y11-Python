#WHILE LOOP challenges 07
#Clay Palmer

bottles = 10

while bottles > 0:
    print("")
    print("There are",bottles,"green bottles hanging on the wall,")
    print(bottles,"green bottles hanging on the wall,")
    print("And if one green bottle should accidentally fall...")
    print("")
    answer = int(input("How many green bottles will be hanging on the wall? "))
    bottles = bottles - 1
    if answer == bottles:
        print("")
        print("There'll be",bottles,"bottles hanging on the wall!")
    else:
        while answer != bottles:
            print("No, try again.")
            print("")
            answer = int(input("How many green bottles will be hanging on the wall? "))
            print("")
        print("There'll be",bottles,"bottles hanging on the wall!")
        
print("There'll be no green bottles hanging on the wall")
