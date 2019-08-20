# -*- coding: utf-8 -*-

import random
import os
import time
from classes import Granolabar
from classes import Bandages
from BuffCreekcalllist import typing


count = None
granola_count = 3
bandages_count = 2
health = 100
enemyh = 100
first = True
food = None
def Ted():
        global health #declaring health as a global variable so I can use it in this function
        os.system("clear\n")
        typing("Ted lunges himself at you ▼\n")
        input()
        os.system("clear\n")
        thit = random.randint(1,100) #generating a random number and assigning it to a variable
        if (thit < 30): #30% chance to trigger a miss
            typing("Ted stumbles over and misses you ▼\n")
            input()
            os.system('clear') #clear terminal screen
            combat()
        elif (30 <= thit < 50): #20% change to trigger a critical hit
            health -= 25
            typing("Ted got a critical hit on you and you lost 25hp! ▼\n")
            input()
            combat()
        elif (50 <= thit <= 100): #50% for a normal hit
            health -= 15
            typing("Ted hit you and you lost 15hp! ▼\n")
            input()
            combat()
def combat(): #main game

    os.system('clear')

    global first
    global health
    global enemyh
    global food
    if first == True: #detects whether the user is going through the game for the first time since running application
        first = False
        typing("Ted approaches you with " + str(enemyh) +"hp!\nFight, Run, Items, or Leave? ▼\n")
    elif first == False:
        if (health > 0) & (enemyh > 0):
            typing("You have " + str(health) + "hp left!\n") #reminds user how much hp they have
            typing("Ted has " + str(enemyh) + "hp left!\n") #reminds user how much hp Ted has
            typing("Fight, Run, Items, or Quit ▼\n")
        elif (health > 0) & (enemyh <= 0):
            typing("You have successfully killed Ted!\n")
            return
        elif health <= 0: #detects if user has died
            typing("You died!\nTry again?\n(yes/no) ▼\n\n")
            answer = input()
            if answer.lower() == "yes":
                health = 100
                enemyh = 100
                food = 3
                first = True
                os.system("clear\n")
                combat()
    response = input()
    if response.lower() == "fight":
        hit = random.randint(1,100) #selecting a random integer between 1 and 100
        os.system("clear\n")
        typing("You swing your knife ▼\n")
        input()
        os.system("clear\n")
        if (hit < 60): #60% chance for a standard hit
            enemyh -= 20
            typing("Ted lost 20hp! ▼\n")
            input()
            os.system("clear\n")
            Ted()
        elif (60 <= hit < 85): #25% chance for a critical hit
            enemyh -= 40
            typing("Critical hit! Ted lost 30hp! ▼\n")
            input()
            os.system("clear\n")
            Ted()
        elif (85 <= hit <= 100): #15% chance to miss
            typing("You swing, but unfortunately Ted jumped out the the way ▼\n")
            input()
            os.system("clear\n")
            Ted()
    elif response.lower() == "run":
        os.system("clear\n")
        typing("You ran away ▼\n")
        input()
        first = True
        enemyh = 100 #restarts enemy hp
        os.system("clear\n")
        combat()
    elif response.lower() == "items": #item menu-ish
        def healing(count, food):
            global health
            if (health == 100) & (food.name == "Granola Bar\n"): #if user has full hp, prevent user from wasting food
                os.system('clear')
                typing("You are not hungry ▼\n")
                input()
                os.system("clear\n")
                items()
            elif (health == 100) & (food.name == "Bandages\n"): #if user has full hp, prevent user from wasting food
                os.system('clear')
                typing("Your hp is full! ▼\n")
                input()
                os.system("clear\n")
                items()
            else:
                count -= 1
                health += food.points
                if health > 100: #if user eats an apple and hp goes over 100, limit hp to 100
                    health = 100
                    os.system('clear')
                    typing("You now have " + str(health) + "hp! ▼\n")
                    input()
                    os.system("clear\n")
                    items()
                elif food.name == "Granola Bar":
                    os.system('clear')
                    typing("You eat a granola bar and gained 20hp! ▼\n")
                    input()
                    os.system("clear\n")
                    items()
                elif food.name == "Bandages":
                    os.system('clear')
                    typing("You applied a bandage and gained 10hp! ▼\n")
                    input()
                    os.system("clear\n")
                    items()
        def items():
            global food
            global health
            global count
            os.system("clear\n")
            typing("Type exit to go back into the fight! ▼\nYou have " + str(granola_count) + " granola bars and " + str(bandages_count) + " bandages!  Please type heal to use items\n")
            itemrsp = input()
            if itemrsp.lower() == "heal":
                need = input("1.Granola Bar\n2.Bandages\n(1 or 2)\n")
                if need == "1":
                    food = Granolabar

                    count = granola_count
                    count -= 1
                    healing(count, food)
                elif need == "2":
                    food = Bandages

                    count = bandages_count
                    count -= 1
                    healing(count, food)
                else:
                    None
            elif itemrsp.lower() == "exit": #exiting item menu
                combat()
            else: #if user gives invalid command
                os.system("clear\n")
                typing("Please enter a valid command ▼\n")
                input()
                items()
        items()
    elif response.lower() == "leave": #quit game
        exit()
    else:
        os.system("clear\n")
        typing("Please enter a valid command! ▼\n")
        input()
        combat()
