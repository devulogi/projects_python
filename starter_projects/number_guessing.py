""" Starter Project: Guessing Game """

from random import randint


def guessing_game():
    """A simple number guessing game"""
    # generate random number between 1 and 100
    random_number: int = randint(1, 100)
    # set user attempt
    default_attempt: int = 0

    print("Welcome to this simple number guessing game!")
    print("Provide a number between 1 and 100.")

    # set max attempt
    try:
        max_attempts: int = int(input("Enter maximum attempts: "))
        print(f"Maximum number of attempts {max_attempts}")
    except ValueError:
        print("Provide a valid input")
        return

    while True:
        if default_attempt >= max_attempts:
            print("You have reached maximum attempt. Game over!")
            print(f"The number that we are looking for is: {random_number}.")
            break

        try:
            # get user input
            guess_input = int(input("Prove a guess: "))
            default_attempt += 1
        except ValueError:
            print("Provide a valid input")
            default_attempt = 0
            continue

        if guess_input > random_number:
            print("Too high!")
        elif guess_input < random_number:
            print("Too low!")
        else:
            print("You guessed it!")
            break
