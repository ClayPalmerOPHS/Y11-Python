#String Slicing Challenges 04
#Clay Palmer

rhyme = str(input("Enter the first line of a nursery rhyme: "))
length = len(rhyme)
print("This has",length,"letters in it")

startNum = int(input("Enter a starting number: "))
endNum = int(input("Enter an ending number: "))

section = rhyme[startNum:endNum]
print(section)
