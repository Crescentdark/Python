from art import logo
from art import vs
from game_data import data
import random

#Format said data
def format_data(account):
    account_name = account["name"]
    account_desc= account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    
    else:
        return guess == "b"

#disply art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    #Random account generation
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    #ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    #check if user correct
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    ## Clear screen
        #clear fucntion here
        #print

    #Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You are right! Currect score: {scorfe}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong.Final score: {score}")


#Score storage

#Replayable

# make account at pos B become the next A

#Screen clearing between rounds