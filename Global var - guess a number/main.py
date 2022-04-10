from art import logo
import random


# global variables
CHILL_MODE = 10
INTENSE_MODE = 5


def set_attempt():
    """Set game difficulty. Return easy or hard mode."""
    level = input("'Chill' mode or 'intense' mode? ").lower()
    if level == "chill":
        return CHILL_MODE
    elif level == "intense":
        return INTENSE_MODE
    else:
        print("Make up your mind! 'Chill' or 'intense'?")
        return set_attempt()


def compare(guess, answer, attempt):
    """Compare guess to answer. Return if the guess is correct."""
    if guess > answer:
        print("\nToo high")
        return False
    elif guess < answer:
        print("\nToo low")
        return False
    else:
        print("\nBingo! You got it right.")
        return True


def start_game():
    print(logo)

    # define answer between starting and ending values
    a = 1
    b = 100
    answer = random.randint(a, b)
    print(f"Try your luck. Guess a number between {a} and {b}.")

    # define attempt remaining
    attempt = set_attempt()

    # loop until all attempt has been used
    while attempt > 0:
        print(f"\nYou have {attempt} attempts remaining.")
        guess = int(input("Make a guess. "))
        if compare(guess, answer, attempt) == False:
            attempt -= 1
        else:
            attempt = 0
    
    print(f"It was {answer}.")


start_game()