print('''   ,-.            _,---._          
  /  /          .'"       `',         
 (  (          ,'             `',       
  \  \       ,'                 \    
   `-'-.___.'-.                    \  
        `---.._`.                   | 
                `'.                 | 
                ,-"`,                \ 
               .   | \                \
              / `./ /                 ;
             /    \/_.'-.   ,          |
            /          `./  \         ;
           /           /    `        /
          /___________/        \__.' 

                               /\           
                              /  \          
                      /\     /    \     /\  
                     /  \   /      \   /  \ 
                    /    \_/        \_/    \
                   /                          \
             /\   /                            \   /\
            /  \_/          __                  \_/  \
           /          ___-'  ~~--.              __| 
          /      _.-~~            \            /   ;
         /    _-'                  \         _;   /
        /   ,'/;_,;\_|_\\~_      ___\      /    |
       /   (   .   /         \     /|\__   /     |
      / ,_.\  '___/_          \  /' |  |`'      \
     /      `~~~    \         / / / ,-'         ;
    /                 \      |   |,'           /
   /                   ;      \_/           __/
  /                  ,'              ___.-'/ 
 /__               ,'           ___.'""'/--.
 //';_ _,'.----.-'"" // ,--`.
((;.. \ ,-'__.._ ,',;;'~--._//-' \
\
------------------------------------------------
''')
print('''

▓█████▄  ▒█████     ▓██   ██▓ ▒█████   █    ██    ▓█████▄  ▄▄▄       ██▀███  ▓█████ 
▒██▀ ██▌▒██▒  ██▒    ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▒████▄    ▓██ ▒ ██▒▓█   ▀ 
░██   █▌▒██░  ██▒     ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▒███   
░▓█▄   ▌▒██   ██░     ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ 
░▒████▓ ░ ████▓▒░     ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒
 ▒▒▓  ▒ ░ ▒░▒░▒░       ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░
 ░ ▒  ▒   ░ ▒ ▒░     ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░
 ░ ░  ░ ░ ░ ░ ▒      ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░   ░   ▒     ░░   ░    ░   
   ░        ░ ░      ░ ░         ░ ░     ░           ░          ░  ░   ░        ░  ░
 ░                   ░ ░                           ░                                





''')
print("WANDERER! Screams a mad lookin fellar 'Bael Ur Moras Keep WILL EAT YOU ALIVE HAHAHAHAHAHAH'.")
print("Your bounty is to find the ancient artifact in this wretched place, for the noble has paid.")

door = input("Do you enter trough the 'backdoor' or the 'front gate'?").lower()
action2 = input("You enter a library of sorts,one of these books could be a hidden room which do you choose,'Gold','White','Black'?").lower()

if door == "backdoor":
    action1 = input("You entered trough the backdoor,where do you go next up the 'stairs' or trough the 'storage'?").lower()
    if action1 == "stairs":
        action2 = input("You enter a library of sorts,one of these books could be a hidden room which do you choose,'Gold','White','Black'?").lower()
        if action2 == "Black":
            print("You found the artifact,now lets leg it.VICTORY")
        else:
            print("Unlucky a disentigration spell was cast.GAME OVER")

    else:
          print("It was a storage of Highly concentrated Mountain Dew, your bones crumble and your skin melts. GAME OVER")
else:   
    print("A living armor has pumelled you.GAME OVER")