# Import the random module here
import random as r
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
num_items = len(names)

random_choice = r.randint(0, num_items - 1)
payer = names[random_choice]
print(payer + " is going to buy the meal today!")
#Write your code below this line 👇