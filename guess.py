import random

correctNum = random.randint(1, 100)

def guessNum():
    guess = input("Guess an integer from 1 to 100: ")
    try:
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Please guess between 1 and 100.\n")
            guessNum()
        elif guess > correctNum:
            print("Too high! Guess again.\n")
            guessNum()
        elif guess < correctNum:
                print("Too low! Guess again.\n")
                guessNum()
        else:
            guess == correctNum
            print("Good job, you guessed correctly!\nThe number is " + str(correctNum) + ".\n")
    except ValueError:
        print("Please guess an integer. \n")
        guessNum()

guessNum()
close = input("Press enter to exit this program. ")