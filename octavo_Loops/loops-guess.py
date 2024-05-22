#A loop is a segment of code that repeats.
# while | for

#"while" loop makes a section of code execute until a certain condition is met.

#we import random -which is a type of library-.

import random

print("Welcome to guess the number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#the next statement will generate a random number between 1 and 10 by using the randint() function of the random module.

number = random.randint(1, 10)

isGuesssRight = False

#the "while loop" will repeat until the number is guessed byt the condition isGuessRight != True

while isGuesssRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) ==number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuesssRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))
