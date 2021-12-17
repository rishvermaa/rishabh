
from ascii_creation import *
from MUD import *
from fights_scenes import *

saviour =saviours(select_player, 8, 10) 
creature1= creatures('Vegeta', 3, 10)
wait()
message = "when Vegeta is brought back to life on Planet Earth, he manages to witness some of the battle between Goku and Frieza....." '\n'
typewritter_style(message)

message = f'{select_player}, your first mission is to save the city from incomming attacks and keep the city safe.....' '\n'
typewritter_style(message)
wait()
wait()
creature1.attack(saviour)
fight()
wait()
saviour.damage(creature1.power)
wait()
wait()
print('That was very close 'f'{select_player} You should let your guard down... I sense another enemy coming to our planet.. get ready!!!','\n')

saviour =saviours(select_player, 8, 10) 
creature2= creatures('Moro ', 4, 10)
wait()
message = f'{select_player} : i have never seen you.. Leave immediately or you will face the concequences..' ,'\n'
typewritter_style(message),'\n'
wait()
message= "Moro : Only time will tell who is going to stay alive...hahahahah!!",'\n'
typewritter_style(message),'\n'
wait()
creature2.attack(saviour),'\n'
fight()
wait()
wait()
saviour.damage(creature2.power)

saviour =saviours(select_player, 8, 10) 
creature3= creatures('Beerus', 9, 10)
#new scene
termcolor.cprint('After fighting the battles against the multiverse threats 'f'{select_player} has decided to participate in a fighting battle..'),'\n'
message= "Welcome to the Ultimate Fighting Champianship.. The first match is between..."  '\n'
typewritter_style(message),'\n'
wait()
print(f'{select_player} Vs Beerus'),'\n'
wait()
wait()
creature3.attack(saviour),'\n'
wait()
saviour.damage(creature3.power),'\n'
fight_scene()


