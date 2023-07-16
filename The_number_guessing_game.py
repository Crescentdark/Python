from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#set a diff
def set_dif():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else:
        return  HARD_LEVEL_TURNS
    


#fn to check the guess against the answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess<  answer:
        print("Too low")
    else:
        print(f"You got it! The answer was {answer}.")


# number choosing
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_dif()
    print(f"You have {turns} attempts remaining to guess the number.")


    guess = 0
    while guess != answer:
    #user guess
        guess = int(input("Make a guess:"))
        check_answer(guess, answer)


game()