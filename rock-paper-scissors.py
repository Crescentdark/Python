
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random as r

game_images = [rock, paper, scissors]

choice = input(
    "What do you choose? Type 0 for rock, 1 for paper, 2 for scissors \n")
user_choice = int(choice)


if user_choice >= 3 or user_choice < 0:
  print("WRONG NUMBER")
else:
  print(game_images[user_choice])
  
  comp_choice = r.randint(0, 2)
  print("Computer chose: \n")
  print(game_images[comp_choice])


  if user_choice == 0 and comp_choice == 1:
    print("You Wins")
  elif comp_choice == 0 and user_choice == 1:
    print("Computer Wins")
  elif comp_choice > user_choice:
    print("Computer wins")
  elif user_choice > comp_choice:
    print("You win")
  elif user_choice == comp_choice:
    print("Its a Draw")


