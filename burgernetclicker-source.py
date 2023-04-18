import pygame.mixer
from pygame import mixer

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
# Sound
mixer.init()
s_mine = pygame.mixer.Sound('sounds/Pickaxe Sound.mp3')
merch_welcome = pygame.mixer.Sound('sounds/Welcome Merchant.mp3')
merch_bye = pygame.mixer.Sound('sounds/Bye Merchant.mp3')
merch_no = pygame.mixer.Sound('sounds/Not Enough Merchant.mp3')
merch_thank = pygame.mixer.Sound('sounds/Thank You Merchant.mp3')

# this function is unused whoops
def menufunc():
    global gaming, run, shoptime
    menu = str(input("Welcome to burgernet the videogame, would you like to mine for burgers or go to the shop?\nEnter 'm' to go to the mines\nEnter 's' to go to the shop\nEnter 'x' to quit:  "))
    if menu == "m":
        run = True
        gaming = False
    elif menu == "s":
        shoptime = True
        gaming = False

def minerfunc():
    mixer.music.load('sounds/Dark As A Dungeon-slowedandreverbstudio.mp3')
    mixer.music.play(loops = -1)
    global burger, hotdog, hoagie, run
    while run == True:
        order = str(input("What type of food would you like to mine? or enter 'exit' to return.\nBurger/Hotdog/Hoagie?: "))
        if order == "burger" or order == "Burger":
            s_mine.play()
            burger = burger + 1 + bonusburger
            print("You mined " + str(bonusburger + 1) + " burgers!")
        elif order == "hotdog" or order == "Hotdog":
            s_mine.play()
            hotdog = hotdog + 1 + bonushotdog
            print("You mined " + str(bonushotdog + 1) + " hot dogs!")
        elif order == "hoagie" or order == "Hoagie":
            s_mine.play()
            hoagie = hoagie + 1 + bonushoagie
            print("You mined " + str(bonushoagie + 1) + " hoagies!")
        elif order == "exit" or order == "exit":
            mixer.music.stop()
            run = False


def shopfunc():
    global burger, hotdog, hoagie, bonusburger, bonushotdog, bonushoagie, bonusburgercost, bonushotdogcost, bonushoagiecost, shoptime
    mixer.music.load('sounds/Store Theme.mp3')
    mixer.music.play(loops=-1)
    merch_welcome.play()
    while shoptime == True:
        upgrade = str(input("Welcome to the burgernet shop! what would you like to purchase?\nBonus Burger - " + str(bonusburgercost) + " Cost\nBonus Hotdog - " + str(bonushotdogcost) + " Cost\nBonus Hoagie - " + str(bonushoagiecost) + " \nExit - " + str("Exit the Shop") + " \nWhat would you like?: "))
        if upgrade == "Bonus Burger" or upgrade == "Burger" or upgrade == "burger":
            if burger >= bonusburgercost:
                merch_thank.play()
                burger = burger - bonusburgercost
                bonusburger = bonusburger + 1
                bonusburgercost = bonusburgercost + 10
            elif burger < bonusburgercost:
                merch_no.play()
                print("You dont have enough burgers!\n")
        elif upgrade == "Bonus Hotdog" or upgrade == "Hotdog" or upgrade == "hotdog":
            if hotdog >= bonushotdogcost:
                merch_thank.play()
                hotdog = hotdog - bonushotdogcost
                bonushotdog = bonushotdog + 1
                bonushotdogcost = bonushotdogcost + 10
            elif hotdog < bonushotdogcost:
                merch_no.play()
                print("You don't have enough hot dogs!\n")
        elif upgrade == "Bonus Hoagie" or upgrade == "Hotdog" or upgrade == "hotdog":
            if hoagie >= bonushoagiecost:
                merch_thank.play()
                hoagie = hoagie - bonushoagiecost
                bonushoagie = bonushoagie + 1
                bonushoagiecost = bonushoagiecost + 10
            elif hoagie < bonushoagiecost:
                merch_no.play()
                print("You don't have enough hoagies!\n")
        elif upgrade == "exit" or upgrade == "Exit":
            merch_bye.play()
            mixer.music.stop()
            shoptime = False
        else:
            print("Please enter only either 'Bonus Burger', 'Bonus Hotdog', 'Bonus Hoagie', or 'exit'.\n")



while gaming == True:
    print("Pick the Shop or the Mines\n's' = Shop: \n'm' = Mines: \n'Exit' = Close program:")
    x = str(input("What would you like to do?: "))
    if x == "m" or x == "M" or x == "Mine":
        run = True
        minerfunc()
        print("Burgers: " + str(burger))
        print("Hotdogs: " + str(hotdog))
        print("Hoagies: " + str(hoagie))
    elif x == "s" or x == "S" or x == "Shop":
        shoptime = True
        shopfunc()
        print("Burgers: " + str(burger))
        print("Hotdogs: " + str(hotdog))
        print("Hoagies: " + str(hoagie))
    elif x == "exit" or x == "Exit":
        quit()
    else:
        print("Please enter only either 's' or 'm'.")