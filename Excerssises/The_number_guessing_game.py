from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



#fn to check the guess against the answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess<  answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        

#set a diff
def set_dif():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else:
        return  HARD_LEVEL_TURNS
    

# number choosing
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_dif()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
    #user guess
        guess = int(input("Make a guess:"))
        
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses")
            return
        elif guess != answer:
            print("GUess again.")


game()