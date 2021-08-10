# File: GuessingGame.py
# Student: Nicole Grimaldos
# UT EID: ng23476
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/03/20
# Date Last Modified: 10/11/20
# Description of Program: There is a set number and user has 10 tries to guess the secret number. The program will
# tell the user if the guess is too high or too low.

print("Welcome to the guessing game. You have ten tries to guess my number.")
guess = int(input("Please enter your guess: "))
tries = 1
secret_num = 1458
while guess != secret_num and tries <= 10:
    if 0 < guess < 9999:
        if guess < 1458:
            print("Your guess is too low.")

            print("Guesses so far:", tries)
            tries += 1
            if tries <= 10:
                guess = int(input("Please enter your guess: "))
        else:
            print("Your guess is too high.")

            print("Guesses so far:", tries)
            tries += 1
            if tries <= 10:
                guess = int(input("Please enter your guess: "))
    else:
        print("Your guess must be between 0001 and 9999.")
        guess = int(input("Please enter a valid guess: "))
if tries == 1:
    print("That’s correct!")
    print("Congratulations! You guessed it on the first try!")
elif tries > 10:
    print("Game over: you ran out of guesses")
else:
    print("That’s correct!")
    print("Congratulations! You guessed it in", tries, "guesses.")