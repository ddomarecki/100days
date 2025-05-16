from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def check_answer(user_guess, actual_answer,turns):
    if user_guess > actual_answer:
        print("To High")
        return turns - 1
    elif user_guess < actual_answer:
        print("To low")
        return turns - 1
    else:
        print("You got it!")

def set_difficulty():
    level = input("Chose dificulty easy or hard: ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1, 100)

    turns = set_difficulty()


    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You lose :(")
            return
        if guess != answer:
            print("Guess again")
game()