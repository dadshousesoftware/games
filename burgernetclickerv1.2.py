import random
bonusburgercost = 10
bonushotdogcost = 10
bonushoagiecost = 10
bonusburger = 0
bonushotdog = 0
bonushoagie = 0
burger = 50
hotdog = 50
hoagie = 50
luck = 0
shovel = 0
shovelmax = 1
shoveldur = 3
goodies = 0
poortreasures = 0
normtreasures = 0
goodtreasures = 0
legendarytreasures = 0
mythicaltreasures = 0
poorartifacts = 0
normartifacts = 0
goodartifacts = 0
legendaryartifacts = 0
mythicalartifacts = 0
gold = 0
goldsellprice = 0
rgoldsellprice = 0
rolling = False
run = False
shoptime = False
digging = False
gaming = True

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




#this function is unused whoops
def menufunc():
    global gaming, run, shoptime
    menu = str(input("welcome to burgernet the videogame, would you like to mine for burgers or go to the shop?\nenter m to go to the mines\nenter s to go to the shop\nenter x to quit:  "))
    if menu == "m":
        run = True
        gaming = False
    elif menu == "s":
        shoptime = True
        gaming = False

def minerfunc():
    global burger, hotdog, hoagie, run
    while run == True:
        order = str(input("What type of food would you like to mine? or enter 'exit' to return.\nBurger/Hotdog/Hoagie?: "))
        if order == "burger" or order == "Burger" or order == "b":
            burger = burger + 1 + bonusburger
            print("You mined " + str(bonusburger + 1) + " burgers!")
        elif order == "hotdog" or order == "Hotdog" or order == "h":
            hotdog = hotdog + 1 + bonushotdog
            print("You mined " + str(bonushotdog + 1) + " hot dogs!")
        elif order == "hoagie" or order == "Hoagie" or order == "g":
            hoagie = hoagie + 1 + bonushoagie
            print("You mined " + str(bonushoagie + 1) + " hoagies!")
        elif order == "exit":
            run = False

def shopfunc():
    global burger, hotdog, hoagie, bonusburger, bonushotdog, bonushoagie, bonusburgercost, bonushotdogcost, bonushoagiecost, shoptime, shovel, shovelmax, poortreasures, normtreasures, goodtreasures, legendarytreasures, mythicaltreasures, gold, rgoldsellprice
    while shoptime == True:
        upgrade = str(input("Welcome to the burgernet shop! what would you like to purchase? Or would you like to sell?\nBonus Burger - " + str(bonusburgercost) + " Burgers\nBonus Hotdog - " + str(bonushotdogcost) + " Hotdogs\nBonus Hoagie - " + str(bonushoagiecost) + " Hoagies\nDented Shovel - 50 of Each \nWhat would you like?: "))
        if upgrade == "exit":
            shoptime = False
        elif upgrade == "Bonus Burger":
            if burger >= bonusburgercost:
                burger = burger - bonusburgercost
                bonusburger = bonusburger + 1
                bonusburgercost = bonusburgercost + 10
            elif burger < bonusburgercost:
                print("You dont have enough burgers!\n")
        elif upgrade == "Bonus Hotdog":
            if hotdog >= bonushotdogcost:
                hotdog = hotdog - bonushotdogcost
                bonushotdog = bonushotdog + 1
                bonushotdogcost = bonushotdogcost + 10
            elif hotdog < bonushotdogcost:
                print("You don't have enough hot dogs!\n")
        elif upgrade == "Bonus Hoagie":
            if hoagie >= bonushoagiecost:
                hoagie = hoagie - bonushoagiecost
                bonushoagie = bonushoagie + 1
                bonushoagiecost = bonushoagiecost + 10
            elif hoagie < bonushoagiecost:
                print("You don't have enough hoagies!\n")
        elif upgrade == "Dented Shovel" and shovel < shovelmax:
            if burger >= 50 and hotdog >= 50 and hoagie >= 50:
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
    x = str(input("Would you like to go to the shop, mines, or cove?\ns/m/c: "))
    if x == "m":
        run = True
        minerfunc()
        print("Burgers: " + str(burger))
        print("Hotdogs: " + str(hotdog))
        print("Hoagies: " + str(hoagie))
    elif x == "s":
        shoptime = True
        shopfunc()
        print("Burgers: " + str(burger))
        print("Hotdogs: " + str(hotdog))
        print("Hoagies: " + str(hoagie))
    elif x == "c":
        digging = True
        archaeology()
        print("Burgers: " + str(burger))
        print("Hotdogs: " + str(hotdog))
        print("Hoagies: " + str(hoagie))
    else:
        print("Please enter only either 's' or 'm'.")
