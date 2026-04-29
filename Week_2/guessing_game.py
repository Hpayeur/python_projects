from random import randint
from art import logo_two

EASY_LEVEL_TURNS = 14
HARD_LEVEL_TURNS = 7


# Function to check user guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
         print("Too High!")
         return turns - 1
    elif user_guess < actual_answer:
         print("Too Low!")
         return turns - 1
    else:
        print(f"You guessed correctly! The Number was {actual_answer}")
        return None


# Function to set difficulty
def set_difficulty():
    level = input("please choose a difficulty level 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print(logo_two)
    # Choosing a random number between 1 and 100.
    print("Hello Welcome to the Number Guessing Game!")
    print("Hmm, I'm thinking of a Number Between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0

    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input ("Let's Make a Guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess Again!")

    #Track the number of turns and reduce by 1 if they get it wrong
game()