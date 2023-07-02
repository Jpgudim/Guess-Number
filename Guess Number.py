import random

print ("Guess a number 1-10!")
print ("You have 3 guesses")
guess = input("Guess: ")

def check_guess(num):
    if num in "012345678910":
        num = int(num)
    while type(num) != int:
        num = input("That doesn't work, try again: ")
        if num in "012345678910":
            num = int(num)
    return num

guess = check_guess(guess)

number = random.randrange(1,11)
number = int(number)
turn = 3

while turn > 0:
    turn -= 1
    if guess == number:
        print ()
        print ("You guessed correctly! The random number was %s." % number)
        print()
        break
    if turn > 0:
        print ("You guessed wrong! You have %s guesses left." % turn) 
        guess = input("Guess again: ")
        guess = check_guess(guess)
    else:
        print ()
        print ("You are out of guesses!")
        print ("The random number was %s" % number)
        print ()
        

