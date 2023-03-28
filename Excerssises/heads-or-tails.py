#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random as r
#Write the rest of your code below this line 👇
toss = r.randrange(0, 2)
if toss == 1:
    print("Heads")
else:
    print("Tails")
