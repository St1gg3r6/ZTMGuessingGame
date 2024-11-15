from random import randint
from sys import argv

DEFAULT_FIRST_NUMBER = 1
DEFAULT_LAST_NUMBER = 10


def game():
    # Set default range
    range = (DEFAULT_FIRST_NUMBER, DEFAULT_LAST_NUMBER)

    new_range = check_for_arguments()
    if new_range:
        range = (new_range[0], new_range[1])

    target = randint(range[0], range[1])

    while True:
        try:
            guess = int(input(f"Guess a number between {range[0]} and {range[1]}: "))
            result = process_guess(guess, target, range)
            print(result)
            if result == "Well done! You guessed correctly.":
                break
        except ValueError:
            print(f"You have to guess a whole number between {range[0]} and {range[1]}.")

    print("GAME OVER")

def check_for_arguments():
    has_arguments = False
    first_number = DEFAULT_FIRST_NUMBER
    last_number = DEFAULT_LAST_NUMBER
    if len(argv) == 2:
        try:
            last_number = int(argv[1])
            has_arguments = True
        except:
            print("Invalid parameter value entered.")
    if len(argv) == 3:
        try:
            first_number = int(argv[1])
            last_number = int(argv[2])
            has_arguments = True
        except:
            print("Invalid parameters entered.")
    if has_arguments:
        return first_number, last_number


def process_guess(guess, target, range):
    if guess < range[0] or guess > range[1]:
        raise ValueError
    if guess == target:
        return "Well done! You guessed correctly."
    elif guess > target:
        return "Your guess was too high. Try again."
    else:
        return "Your guess was too low. Try again."


if __name__ == '__main__':
    game()
