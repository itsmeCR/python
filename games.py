import random
def whatisthenumber():   
    # This is the amount of tries that you take, it gets increased towards the end of the code depending on
    # how many tries you take
    tries = 1
    num1 = int(input("Input a number between 1 and 10 "))
    # The below code executes a loop that keeps on saying the number is invalid if it is greater than 10
    # or less than 1
    while num1 > 10 or num1 < 1:
        print("Sorry, but that number is invalid, try again!")
        num1 = int(input("Input a number"))  
    # If the number is valid the below code will continue the game
    if num1 <= 10 and num1 >= 1:
        print("Good, we shall continue")
        print("Your partner can now guess the number!")
    num2 = int(input("What is your partner's number, player 2?"))
    # This is the core of the game, telling you that you are wrong until you guess it correctly using a 
    # while loop, it also has a try counter built in by adding 1 to itself every time you guess it wrong
    while num2 != num1:
        print("Wrong, try again!")
        num2 = int(input("What is your partner's number?"))
        tries = tries + 1 
    # This tells you when you correct and the amount of tries you took
    if num2 == num1:
        print("You did it,and it only took " + str(tries) + " trie(s)!")
    input("press enter to exit")

def magiceightball():
    int(input("Type the magic number to initiate the game"))
    magicnumber = random.randint(1,8)
    if magicnumber == 1:
        print("Reptiles are cold blooded")
    elif magicnumber == 2:
        print("Cats are children of the devil")
    elif magicnumber == 3:
        print("Dogs are cool")
    elif magicnumber == 4:
        print("Monkeys like bananas")
    elif magicnumber == 5:
        print("Humans are not robots")
    elif magicnumber == 6:
        print("Gazelle die to lions")
    elif magicnumber == 7:
        print("Meerkats also die to lions")
    elif magicnumber == 8:
        print("Pigs are simultaneously dirty and clean")
    input("press enter to exit")

game = int(input("Choose a game, there is 2 of them, choose a number 1-2 to choose!"))
if game == 1:
    whatisthenumber()
elif game == 2:
    magiceightball()
else:
    print("None of these are valid")



