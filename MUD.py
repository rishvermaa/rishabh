import re
import sys, time
from tqdm import tqdm
import termcolor

message = "Welcome to the Dragon Ballz SAGA !! Please enter your name..." 

# printing the message in typewritter stype
def typewritter_style(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)
typewritter_style(message)


# Select and checking gamer's name
def your_name():
    name = input('\n'">>")
    print(f'Did i get your name right, {name} ? (yes/no)')

    answer =input(">>")
    text_file = open("Store.txt", "w")
    text_file.write(name)
    text_file.close()
    
    if "y"  in answer:
        termcolor.cprint("okay you're good to go! \n",'green' )
    elif answer == "no":
        print()

    for i in answer:
        if "n" in answer:
            termcolor.cprint("Please try again",'red')
            name = input("Please enter your name: \n>>")
            print(f'Did i get your name right, {name} ? (yes/no)')
            answer =input(">>")
        else:
            break    
your_name()

# Select password 
termcolor.cprint("Now choose your Password as per below instructions: \n",'yellow')
termcolor.cprint("At least 1 letter between [A-Z]. \nAt least 1 number between [0-9]. \nAt least 1 character from [$#@!*&£%]. \nMinimum length 7 characters. \nMaximum length 14 characters. \n",'magenta')
def validate():
    password = input("Enter your password: ")
    if (len(password) < 7):
        termcolor.cprint("Password must be at least 7 characters long",'red')
    elif (len(password) >= 14):
        print("Password must not be more than 14 characteres long")
    for i in password:
        
        if re.search("[0-9]",password) is None:
            termcolor.cprint("Make sure your password has a number in it", 'red')
            password = input("Enter your password again: ")

        elif re.search('[A-Z]',password) is None: 
            termcolor.cprint("Make sure your password has a capital letter in it",'red')
            password = input("Enter your password again: ")
            
        elif (re.search('[@,#,$,!,&,*,%,£]', password) is None):
            termcolor.cprint("At least one of these characters (@ - # - $ - ! - & - * - % - £) must be included",'red')
            password = input("Enter your password again: ")
        else:
            termcolor.cprint("Your Password is Strong \n",'green')
            break
validate()


# Select characters
termcolor.cprint("Select one from the following race: \n",'yellow')
character = {"Saiyan":"saviour", "Human":"saviour", "Namek":"saviour", "Android":"destroyer", "God":"saviour","Demon":"destroyer","Half-Breed":"destroyer", "Mutant":"hybrid"}
def char(character):
    for characters in character.keys():
        termcolor.cprint(characters,'magenta')
    choose_character = input(">>")
    if choose_character not in character.keys():
        termcolor.cprint("Incorrect selection, Please give respect to anime characters and try again from the list(FYI: Its case sensitive)", 'red')
        for characters in character.keys():
            choose_character = input(">>")
            if choose_character in character.keys():  
                break 
    else:
        pass
char(character)

#health bar
def health():
    pbar = tqdm(total = 10) 
    for i in range(10):
	    time.sleep(0.4)
	    pbar.update(2)
    pbar.close()

#time delay
def wait():
    time.sleep(0.8)

# select players
termcolor.cprint("Select one of the following Character: \n", 'yellow')
player= {"Goku":"Hero", "Gohan":"Hero", "Freiza":"Villian", "Android_17":"Villian", "Cell":"Villian","Majin_Bu":"Villian"}

#loop if any incorrect selection is made
for players in player.keys():
    termcolor.cprint(players, 'magenta')
select_player = input(">>")
if select_player not in player.keys():
    termcolor.cprint("Incorrect selection, Please give respect to anime characters and try again from the list(FYI: Its case sensitive)", 'red') 
    for players in player.keys():
        select_player = input(">>")
        if select_player in player.keys():
            break
    else:
        pass

#creating class
class creatures:
    def __init__(self,name,power, health):
        self.name= name
        self.power=power
        self.health= health

    def attack(self, target):
        print(f'{self.name} attacked you, {target.name} by lazer beam for {self.power} power.' )

    def damage(self, damage):
        self.health -= damage
        print(f'{self.name}, you took {damage} damage, your remaining health is {self.health}.') 
        if self.health <= 10 and self.health <=5:
            termcolor.cprint(f'{self.name} your health is low !! you need to revive ASAP to save the world.','red')  
        if self.health <= 1:
            termcolor.cprint(f'{self.name} you are about to Die....')
            input("Press any button if you want to revive " )
            health()
        sys.exit

class saviours:
    def __init__(self, name, power, health):
        self.name= name
        self.power = power
        self.health = health


    def attack(self, target):
        print(f'{self.name} attacked you,{target.name} by lazer beam for {self.power} power.' )

    def damage(self, damage):
        self.health -= damage
        print(f'{self.name}, you took {damage} damage, your remaining health is {self.health}.') 
        if self.health <= 10 and self.health <=5:
            termcolor.cprint(f'{self.name} your health is low !! you need to revive ASAP to save the world.','red')  
        if self.health <= 1:
            termcolor.cprint(f'{self.name} you are about to Die....')
            input("Press any button if you want to revive " )
            health()
        sys.exit







 