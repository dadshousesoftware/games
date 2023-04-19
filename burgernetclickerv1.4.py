# Imports
import random
import importlib
import subprocess
import pygame
from pygame import mixer
# Settings
with open('settings.txt.', 'r') as file:
    bonusburgercost = int(file.readline())
    bonushotdogcost = int(file.readline())
    bonushoagiecost = int(file.readline())
    shovelmax = int(file.readline())
    shoveldur = int(file.readline())
    goldsellprice = int(file.readline())
    rgoldsellprice = int(file.readline())
# Savefile
with open('savefile.txt', 'r') as file:
    burger = int(file.readline())
    hotdog = int(file.readline())
    hoagie = int(file.readline())
    luck = int(file.readline())
    shovel = int(file.readline())
    goodies = int(file.readline())
    poortreasures = int(file.readline())
    normtreasures = int(file.readline())
    goodtreasures = int(file.readline())
    legendarytreasures = int(file.readline())
    mythicaltreasures = int(file.readline())
    poorartifacts = int(file.readline())
    normartifacts = int(file.readline())
    goodartifacts = int(file.readline())
    legendaryartifacts = int(file.readline())
    mythicalartifacts = int(file.readline())
    gold = int(file.readline())
    bonusburger = int(file.readline())
    bonushotdog = int(file.readline())
    bonushoagie = int(file.readline())
# Game states
rolling = False
run = False
shoptime = False
digging = False
gaming = True
# Sound
mixer.init()
s_mine = pygame.mixer.Sound('sounds/Pickaxe Sound.mp3')
merch_welcome = pygame.mixer.Sound('sounds/Welcome Merchant.mp3')
merch_bye = pygame.mixer.Sound('sounds/Bye Merchant.mp3')
merch_no = pygame.mixer.Sound('sounds/Not Enough Merchant.mp3')
merch_thank = pygame.mixer.Sound('sounds/Thank You Merchant.mp3')


# Try to import the Pygame module
try:
    importlib.import_module('pygame')
except ImportError:
    print("Pygame is not installed on this computer. You need Pygame to run this program.")
    install_pygame = input("Do you want to install Pygame? (y/n): ")
    if install_pygame.lower() == 'y':
        try:
            subprocess.check_call(['pip', 'install', 'pygame'])
            print("Pygame has been successfully installed.")
        except subprocess.CalledProcessError as e:
            print("Failed to install Pygame. Error:", e)
    else:
        print("Pygame will not be installed.")
def savegame():
    with open('savefile.txt', 'w') as file:
        file.write(str(burger) + '\n')
        file.write(str(hotdog) + '\n')
        file.write(str(hoagie) + '\n')
        file.write(str(luck) + '\n')
        file.write(str(shovel) + '\n')
        file.write(str(goodies) + '\n')
        file.write(str(poortreasures) + '\n')
        file.write(str(normtreasures) + '\n')
        file.write(str(goodtreasures) + '\n')
        file.write(str(legendarytreasures) + '\n')
        file.write(str(mythicaltreasures) + '\n')
        file.write(str(poorartifacts) + '\n')
        file.write(str(normartifacts) + '\n')
        file.write(str(goodartifacts) + '\n')
        file.write(str(legendaryartifacts) + '\n')
        file.write(str(mythicalartifacts) + '\n')
        file.write(str(gold) + '\n')
        file.write(str(bonusburger) + '\n')
        file.write(str(bonushotdog) + '\n')
        file.write(str(bonushoagie) + '\n')
def rollfortreasure():
    global goodies, rolling
    while rolling == True:
        goodies = (random.sample(range(100), 1))
        goodies = goodies[0] - 30 + luck
        rolling = False
def archaeology():
    global burger, hoagie, hotdog, rolling, shovel, shoveldur, goodies, poortreasures, normtreasures, goodtreasures, legendarytreasures, mythicaltreasures, digging
    while digging == True:
        response = str(input("Welcome to burger cove! If you'd like to dig for treasure, enter 'dig'!: "))
        if response == "dig" and shoveldur > 0 and shovel > 0:
            shoveldur = shoveldur - 1
            if shoveldur == 0:
                shovel = shovel - 1
            rolling = True
            rollfortreasure()
            if goodies <= 10:
                print("You couldn't manage to dig anything up.")
            elif goodies > 10 and goodies <= 25:
                poortreasures = poortreasures + 1
                print("Huh. you dug up a poor treasure.")
            elif goodies > 25 and goodies <= 50:
                normtreasures = normtreasures + 1
                print("Nice, you found an average treasure.")
            elif goodies > 50 and goodies <= 70:
                goodtreasures = goodtreasures + 1
                print("Yippee! you found a rare treasure!")
            elif goodies > 70 and goodies <= 90:
                legendarytreasures = legendarytreasures + 1
                print("OH MY LOOOOORD! You found a legendary treasure!")
            elif goodies > 90 and goodies <= 100:
                mythicaltreasures = mythicaltreasures + 1
                print("YOU FOUND A MYTHICAL TREASURE!!!!")
        if response == "dig" and shovel < 1:
            print("You're out of shovels! get out of the cove!")
            digging = False
        if response == "exit":
            digging = False

def minerfunc():
    mixer.music.load('sounds/Dark As A Dungeon-slowedandreverbstudio.mp3')
    mixer.music.play(loops = -1)
    global burger, hotdog, hoagie, run
    while run == True:
        order = str(input("What type of food would you like to mine? or enter 'exit' to return.\nBurger/Hotdog/Hoagie?: "))
        if order == "burger" or order == "Burger" or order == "b":
            s_mine.play()
            burger = burger + 1 + bonusburger
            print("You mined " + str(bonusburger + 1) + " burgers!")
        elif order == "hotdog" or order == "Hotdog" or order == "h":
            s_mine.play()
            hotdog = hotdog + 1 + bonushotdog
            print("You mined " + str(bonushotdog + 1) + " hot dogs!")
        elif order == "hoagie" or order == "Hoagie" or order == "g":
            s_mine.play()
            hoagie = hoagie + 1 + bonushoagie
            print("You mined " + str(bonushoagie + 1) + " hoagies!")
        elif order == "exit":
            mixer.music.stop()
            run = False

# Current bug: Pressing any non "shop" input shows the black market instead of line 219.
def shopfunc():
    global burger, hotdog, hoagie, bonusburger, bonushotdog, bonushoagie, bonusburgercost, bonushotdogcost, bonushoagiecost, shoptime, shovel, shovelmax, poortreasures, normtreasures, goodtreasures, legendarytreasures, mythicaltreasures, gold, rgoldsellprice, drill
    mixer.music.load('sounds/Store Theme.mp3')
    mixer.music.play(loops=-1)
    merch_welcome.play()
    while shoptime == True:
        upgrade = str(input("Welcome to the burgernet shop! what would you like to purchase? Or would you like to sell?\nBonus Burger - " + str(bonusburgercost) + " Burgers\nBonus Hotdog - " + str(bonushotdogcost) + " Hotdogs\nBonus Hoagie - " + str(bonushoagiecost) + " Hoagies\nDented Shovel - 50 of Each \nWhat would you like?: "))
        if upgrade == "exit":
            merch_bye.play()
            mixer.music.stop()
            shoptime = False
        elif upgrade == "Bonus Burger":
            if burger >= bonusburgercost:
                merch_thank.play()
                burger = burger - bonusburgercost
                bonusburger = bonusburger + 1
                bonusburgercost = bonusburgercost + 10
            elif burger < bonusburgercost:
                merch_no.play()
                print("You dont have enough burgers!\n")
        elif upgrade == "Bonus Hotdog":
            if hotdog >= bonushotdogcost:
                merch_thank.play()
                hotdog = hotdog - bonushotdogcost
                bonushotdog = bonushotdog + 1
                bonushotdogcost = bonushotdogcost + 10
            elif hotdog < bonushotdogcost:
                merch_no.play()
                print("You don't have enough hot dogs!\n")
        elif upgrade == "Bonus Hoagie":
            if hoagie >= bonushoagiecost:
                merch_thank.play()
                hoagie = hoagie - bonushoagiecost
                bonushoagie = bonushoagie + 1
                bonushoagiecost = bonushoagiecost + 10
            elif hoagie < bonushoagiecost:
                merch_no.play()
                print("You don't have enough hoagies!\n")
        elif upgrade == "Dented Shovel" and shovel < shovelmax:
            if burger >= 50 and hotdog >= 50 and hoagie >= 50:
                merch_thank.play()
                burger = burger - 50
                hotdog = hotdog - 50
                hoagie = hoagie - 50
                shovel = shovel + 1
            elif burger < 50 or hotdog < 50 or hoagie < 50:
                print("You don't have enough items to buy this!\n")
        elif upgrade == "sell" or "s" or "Sell":
            print("Your Current Treasures:\nPoor Treasures: " + str(poortreasures) + "\nCommon Treasures: " + str(normtreasures) + "\nRare Treasures: " + str(goodtreasures) + "\nLegendary Treasures: " + str(legendarytreasures) + "\nMythical Treasures: " + str(mythicaltreasures))
            selling = str(input("Welcome to the black market, where we buy yer' treasures! Enter the quality of treasure you'd like to sell, and we'll reward you handsomely.\n"))
            if selling == "exit":
                merch_bye.play()
                mixer.music.stop()
                savegame()
                shoptime = False
            elif selling == "poor" and poortreasures >= 1:
                poortreasures = poortreasures - 1
                goldsellprice = (random.sample(range(20), 1))
                rgoldsellprice = goldsellprice[0]
                gold = gold + rgoldsellprice
                print("Hmm... this thing is a piece of garbage, but I suppose I can give you " + str(rgoldsellprice) + " gold for it.")
            elif selling == "poor" and poortreasures < 1:
                print("You don't have any of those treasures!")
            elif selling == "common" and normtreasures >= 1:
                normtreasures = normtreasures - 1
                goldsellprice = (random.sample(range(50), 1))
                rgoldsellprice = goldsellprice[0]
                gold = gold + rgoldsellprice + 20
                print("This treasure is pretty average... I'll give you " + str(rgoldsellprice) + " gold for it!")
            elif selling == "common" and normtreasures < 1:
                print("You don't have any of those treasures!")
            elif selling == "rare" and goodtreasures >= 1:
                goodtreasures = goodtreasures - 1
                goldsellprice = (random.sample(range(90), 1))
                rgoldsellprice = goldsellprice[0]
                gold = gold + rgoldsellprice + 40
                print("This treasure is pretty rare, so I'll give you " + str(rgoldsellprice) + " gold for it!")
            elif selling == "rare" and goodtreasures < 1:
                print("You don't have any of those treasures!")
            elif selling == "legendary" and legendarytreasures >= 1:
                legendarytreasures = legendarytreasures - 1
                goldsellprice = (random.sample(range(200), 1))
                rgoldsellprice = goldsellprice[0]
                gold = gold + rgoldsellprice + 50
                print("This treasure is extraordinary! I'll give you " + str(rgoldsellprice) + " gold for it!")
            elif selling == "legendary" and legendarytreasures < 1:
                print("You don't have any of those treasures!")
            elif selling == "mythical" and mythicaltreasures >= 1:
                mythicaltreasures = mythicaltreasures - 1
                goldsellprice = (random.sample(range(500), 1))
                rgoldsellprice = goldsellprice[0]
                gold = gold + rgoldsellprice + 90
                print("Good Heavens! You brought me a mythical treasure! I'll give you " + str(rgoldsellprice) + " gold for it!")
            elif selling == "mythical" and mythicaltreasures < 1:
                print("You don't have any of those treasures!")
        else:
            print("Please enter only either 'Bonus Burger', 'Bonus Hotdog', 'Bonus Hoagie', or 'exit'.\n")

while gaming == True:
    x = str(input("Would you like to go to the shop, mines, or cove?\ns/m/c/exit\nYou must run 'exit' to save game: \n"))
    if x == "m" or x == 'M' or x == "Mine" or x == "mine":
        run = True
        minerfunc()
        print("Burgers: " + str(burger))
        print("Hotdogs: " + str(hotdog))
        print("Hoagies: " + str(hoagie))
    elif x == "s" or x == "S" or x == "Shop" or x == "shop":
        shoptime = True
        shopfunc()
        print("Burgers: " + str(burger))
        print("Hotdogs: " + str(hotdog))
        print("Hoagies: " + str(hoagie))
    elif x == "c" or x == "C":
        digging = True
        archaeology()
        print("Burgers: " + str(burger))
        print("Hotdogs: " + str(hotdog))
        print("Hoagies: " + str(hoagie))
    elif x == 'Exit' or x == "exit":
        with open('savefile.txt', 'w') as file:
            savegame()
        quit()
    else:
        print("Please enter only either 's','m' or 'exit'")
