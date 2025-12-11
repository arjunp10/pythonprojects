import random
numguess = 0
numsize = int(input("Enter the maximum number for the range (minimum is 0): "))
if numsize <= 0:
    print("input a number greater than 0")
    quit()

guessnum = random.randrange(numsize)

while True:
    guess = int(input("Enter your gueess: "))
    numguess += 1
    if guess < guessnum:
        print("Too low! Try again.")
    elif guess > guessnum:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number", guessnum, "in", numguess, "tries.")
        quit()
