bonusburgercost = 10
bonushotdogcost = 10
bonushoagiecost = 10
bonusburger = 0
bonushotdog = 0
bonushoagie = 0
burger = 0
hotdog = 0
hoagie = 0
run = False
shoptime = False
gaming = True

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
        if order == "burger" or order == "Burger":
            burger = burger + 1 + bonusburger
            print("You mined " + str(bonusburger + 1) + " burgers!")
        elif order == "hotdog" or order == "Hotdog":
            hotdog = hotdog + 1 + bonushotdog
            print("You mined " + str(bonushotdog + 1) + " hot dogs!")
        elif order == "hoagie" or order == "Hoagie":
            hoagie = hoagie + 1 + bonushoagie
            print("You mined " + str(bonushoagie + 1) + " hoagies!")
        elif order == "exit":
            run = False

def shopfunc():
    global burger, hotdog, hoagie, bonusburger, bonushotdog, bonushoagie, bonusburgercost, bonushotdogcost, bonushoagiecost, shoptime
    while shoptime == True:
        upgrade = str(input("Welcome to the burgernet shop! what would you like to purchase?\nBonus Burger - " + str(bonusburgercost) + " Cost\nBonus Hotdog - " + str(bonushotdogcost) + " Cost\nBonus Hoagie - " + str(bonushoagiecost) + " Cost\nWhat would you like?: "))
        if upgrade == "Bonus Burger":
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
        elif upgrade == "exit":
            shoptime = False
        else:
            print("Please enter only either 'Bonus Burger', 'Bonus Hotdog', 'Bonus Hoagie', or 'exit'.\n")



while gaming == True:
    x = str(input("Pick the shop or the mines\ns/m: "))
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
    else:
        print("Please enter only either 's' or 'm'.")
