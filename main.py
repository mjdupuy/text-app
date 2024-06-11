import time

race_list = ['Elves', 'Dwarves', 'Humans', 'Orcs', 'Halflings', 'Gnomes', 'Giants', 'Trolls', 'Centaurs']
class_type_list = ['Paladin', 'Samurai', 'Rogue', 'Ranger', 'Sorcerer','Priest','Summoner','Warrior']
family_name_list = ['Stormrider','Doomclaw','Thunderforge','Aetherborn','Zephyrion','Grimstone']

class Character:

    
    def __init__(self, first_name, last_name, gender, race, class_type): 
        self.first_name  = first_name
        self.last_name = last_name
        self.gender = gender
        self.race = race
        self.class_type = class_type
        

def create_character(self, first_name, last_name, gender, race, class_type):
    print("Welcome to our RPG adventure! Let's start by creating your character. First, what will your name be?")
    first_name = input




#
#
#class User:
#
#   def __init__(self):
#       self.username = ''
#       self.password = ''
#       self.save = ''
#
#
#
#   def login(self, username, password, save):
#
#        self.username = username 
#        self.password = password
#        self.save = save
#    





print("Welcome to the world of Fantasy 07, you will be able to select tasks, options by pressing the number in front of the text.")
time.sleep(.5)
print("For example, below you will have three options:")
time.sleep(.5)
print("1. Play Fantasy 07.")
time.sleep(.5)
print("2. Play Fantasy 07.")
time.sleep(.5)
print("3. Play Fantasy 07.")
    

while True:
    begin = input("")
    if begin == "1":
        print("Good choice, as you notice you can only play Fantasy 07.")
        break
    elif begin == "2":
        print("Incorrect Option, try again")
        continue
    elif begin == "3":
        print("Incorrect Option, try again")
        continue
    else:
        print("Please provide one of the numbers!")
        continue

time.sleep(.5)
print("Welcome to the world of Fantasy 07, let's start by creating your character!")


print("Welcome to our RPG adventure! Let's start by creating your character. First, what will your name be?")
first_name = input("")
print("With each character there is also a Family name, what is your family name?")
family_name_count = 1
for family in family_name_list:
    
    print(str(family_name_count) + '. ' + family)
    family_name_count += 1

family_name = input("")
if family_name_count == family_name_list[family_name_count - 1]:
        print("Welcome " + first_name + " " + family)


    



