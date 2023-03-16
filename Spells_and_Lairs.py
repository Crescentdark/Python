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

door = input("Do you enter trough the backdoor or the front gate?")
action1 = input("You entered trough the backdoor,where do you go next up the stairs or trough the storage?")
action2 = input("You enter a library of sorts,one of these books could be a hidden room which do you choose?")

if door == "front gate":
    print("A living armor has pumelled you.GAME OVER")
elif action1 == "storage":
        print("It was a storage of Highly concentrated Mountain Dew, your bones crumble and your skin melts. GAME OVER")
elif action2 == "White" or "Gold" or "Black":
            print("Unlucky a disentigration spell was cast.GAME OVER")


