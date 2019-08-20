# -*- coding: utf-8 -*-
from random import uniform
import os
from combat import combat
from classes import Granolabar
from classes import Bandages
from BuffCreekcalllist import go_to_woods
from BuffCreekcalllist import drink_water
from BuffCreekcalllist import rest_death
from BuffCreekcalllist import find_knife
from BuffCreekcalllist import walk_right
from BuffCreekcalllist import make_coat
from BuffCreekcalllist import start_fire
from BuffCreekcalllist import man_shoot
from BuffCreekcalllist import refuse_ride
from BuffCreekcalllist import man_see_false
from BuffCreekcalllist import die_hypo
from BuffCreekcalllist import no_drink
from BuffCreekcalllist import typing
from BuffCreekcalllist import kms

def startover():
    typing("Do you wish to retry?\n(yes/no)")
    cont = input()
    if cont.lower() == "yes":
        game()
    elif cont.lower() == "no":
        exit()
    else:
        typing("Please enter a valid command")
        input()
        startover()
def game():
    typing("Welcome to Buffalo Creek!  A game designed by Nathan Hawk and Cole Bohanon\n")
    typing("You awake in a room, and there's nobody around you.  Do you investigate the room?\n")
    answer1=input()
    if answer1.lower() == "no":
        go_to_woods()
        answer3=input()
        if answer3.lower()== "yes":
            typing("You find a bottle of high proof moonshine, which can be used as an antispetic if needed and you put it in your backpack\n")
            kms()
            startover()
        elif answer3.lower()== "no":
            kms()
    elif answer1.lower() == "yes":
        typing("You find a beer bottle and you break it to make a shank\n")
        typing("You have cut your hand and are bleeding everywhere\n")
        typing("Do you sacrifice a bit of your pant leg to stop the bleeding?\n")
        answer2=input()
        if answer2.lower()== "yes":
            typing("The bleeding has stopped and you are ok\n")
            typing("You walk outside and find you are in the middle of the woods, and there is another shack in the distance\n")
            typing("Do you investigate?\n")
            answer3=input()
            if answer3.lower()== "yes":
                typing("You find a bottle of high proof moonshine, which can be used as an antispetic if needed and you put it in your backpack\n")
                typing("You keep walking and out of nowhere, a bobcat jumps out at you and you manage to kill it with your makeshift beer bottle weapon\n")
                typing("You eventually find a path, but it goes in two directions, do you go to the left or right?\n")
                answer4=input()
                if answer4.lower()== "left":
                    typing("You continue walking left\n")
                    typing("You eventually see an abandoned car\n")
                    typing("Do you investigate?\n")
                    answer5=input()
                    if answer5.lower()== "yes":
                        find_knife()
                        answer6=input()
                        if answer6.lower()== "yes":
                            make_coat()
                            answer7=input()
                            if answer7.lower()== "yes":
                                drink_water()
                                if (uniform(1,10)) >7.5:
                                    typing("The water you drank was infected and you have finally succombed to dysentary\n")
                                    typing("You die\n")
                                    typing("GAME OVER\n")
                                    startover()
                                    exit()
                                answer8=input()
                                if answer8.lower()== "yes":
                                    start_fire()
                                    answer9=input()
                                    if answer9.lower()== "yell":
                                        typing("The man in the truck hears you and he stops.  He then tells you of a town not too far up the road he can take you to\n")
                                        typing("Do you enter his truck?\n")
                                        answer10=input()
                                        if answer10.lower()== "no":
                                            refuse_ride()
                                            startover()
                                        if answer10.lower()== "yes":
                                            typing("You get in his truck and you see him reach beside his seat\n")
                                            typing("Do you attack him?\n")
                                            answer11=input()
                                            if answer11.lower()== "yes":
                                                combat()
                                                typing("Congratulations, YOU WIN\n")
                                                exit()
                                            elif answer11.lower()== "no":
                                                man_shoot()
                                                startover()
                                    elif answer9.lower()== "jump":
                                        man_see_false()
                                        startover()
                                elif answer8.lower()== "no":
                                    die_hypo()
                                    startover()
                            elif answer7.lower()== "no":
                                no_drink()
                                startover()
                        elif answer6.lower()== "no":
                            rest_death()
                            startover()
                    elif answer5.lower()== "no":
                        typing("You continue walking\n")
                        typing("The bandage you made from your pant leg is getting very bloody.  Do you make another?\n")
                        answer6=input()
                        if answer6.lower()== "yes":
                            typing("You make another bandage and your wound feels better\n")
                            
                        elif answer6.lower()== "no":
                            typing("You keep the same bandage on and you continue\n")
                elif answer4.lower()== "right":
                    walk_right()
                    startover()
            elif answer3.lower()== "no":
                typing("You keep walking and out of nowhere, a bobcat jumps out at you and you manage to kill it with your makeshift beer bottle weapon\n")
                typing("You eventually find a path, but it goes in two directions, do you go to the left or right?\n")
                answer4=input()
                if answer4.lower()== "left":
                    typing("You continue walking left\n")
                    typing("You eventually see an abandoned car\n")
                    typing("Do you investigate?\n")
                    answer5=input()
                    if answer5.lower()== "yes":
                        find_knife()
                        answer6=input()
                        if answer6.lower()== "yes":
                            make_coat()
                            answer7=input()
                            if answer7.lower()== "yes":
                                drink_water()
                                if (uniform(1,10)) >7.5:
                                    typing("The water you drank was infected and you have caught dysentary\n")
                                    typing("You die\n")
                                    typing("GAME OVER\n")
                                    startover()
                                    exit()
                                answer8=input()
                                if answer8.lower()== "yes":
                                    start_fire()
                                    answer9=input()
                                    if answer9.lower()== "yell":
                                        typing("The man in the truck hears you and he stops.  He then tells you of a town not too far up the road he can take you to\n")
                                        typing("Do you enter his truck?\n")
                                        answer10=input()
                                        if answer10.lower()== "yes":
                                            typing("You get in his truck and you see him reach beside his seat\n")
                                            typing("Do you attack him?\n")
                                            answer11=input()
                                            if answer11.lower()== "yes":
                                                combat()
                                                typing("Congratulations, YOU WIN\n")
                                                exit()
                                            elif answer11.lower()== "no":
                                                man_shoot()
                                                startover()
                                        elif answer10.lower()== "no":
                                            refuse_ride()
                                            startover()
                                    elif answer9.lower()== "jump":
                                        man_see_false()
                                        startover()
                                elif answer8.lower()== "no":
                                    die_hypo()
                                    startover()
                            elif answer7.lower()== "no":
                                no_drink()
                                startover()
                        elif answer6.lower()== "no":
                            rest_death()
                            startover()
                    elif answer5.lower()== "no":
                        typing("You continue walking\n")
                        typing("The bandage you made from your pant leg is getting very bloody.  Do you make another?\n")
                        answer6=input()
                        if answer6.lower()== "yes":
                            typing("You make another bandage and your wound feels better\n")
                        elif answer6.lower()== "no":
                            typing("You keep the same bandage on and you continue\n")
                elif answer4.lower()== "right":
                    walk_right()
                    startover()
        elif answer2.lower()== "no":
            typing("You get an infection and need to find an antiseptic quickly\n")
            typing("You walk outside and find you are in the middle of the woods, and there is another shack in the distance\n")
            typing("Do you investigate?\n")
            answer3=input()
            if answer3.lower()== "yes":
                typing("You find a bottle of high proof moonshine, and use it as an antiseptic, saving your life\n")
                typing("You keep walking and out of nowhere, a bobcat jumps out at you and you manage to kill it with your makeshift beer bottle weapon\n")
                typing("You eventually find a path, but it goes in two directions, do you go to the left or right?\n")
                answer4=input()
                if answer4.lower()== "left":
                    typing("You continue walking left\n")
                    typing("You eventually see an abandoned car\n")
                    typing("Do you investigate?\n")
                    answer5=input()
                    if answer5.lower()== "yes":
                        find_knife()
                        answer6=input()
                        if answer6.lower()== "yes":
                            make_coat()
                            answer7=input()
                            if answer7.lower()== "yes":
                                drink_water()
                                if (uniform(1,10)) >7.5:
                                    typing("The water you drank was infected and you have caught dysentary\n")
                                    typing("You die\n")
                                    typing("GAME OVER\n")
                                    startover()
                                    exit()
                                answer8=input()
                                if answer8.lower()== "yes":
                                    start_fire()
                                    answer9=input()
                                    if answer9.lower()== "yell":
                                        typing("The man in the truck hears you and he stops.  He then tells you of a town not too far up the road he can take you to\n")
                                        typing("Do you enter his truck?\n")
                                        answer10=input()
                                        if answer10.lower()== "yes":
                                            typing("You get in his truck and you see him reach beside his seat\n")
                                            typing("Do you attack him?\n")
                                            answer11=input()
                                            if answer11.lower()== "yes":
                                                combat()
                                                typing("Congratulations, YOU WIN\n")
                                                exit()
                                            elif answer11.lower()== "no":
                                                man_shoot()
                                                startover()
                                        elif answer10.lower() == "no":
                                            refuse_ride()
                                            startover()
                                    elif answer9.lower()== "jump":
                                        man_see_false()
                                        startover()
                                elif answer8.lower()== "no":
                                    die_hypo()
                                    startover()
                            elif answer7.lower()== "no":
                                no_drink()
                                startover()
                        elif answer6.lower()== "no":
                            rest_death()
                            startover()
                    elif answer5.lower()== "no":
                        typing("You continue walking\n")
                        typing("The bandage you made from your pant leg is getting very bloody.  Do you make another?\n")
                        answer6=input()
                        if answer6.lower()== "yes":
                            typing("You make another bandage and your wound feels better\n")
                        elif answer6.lower()== "no":
                            typing("You keep the same bandage on and you continue\n")
                elif answer4.lower()== "right":
                    walk_right()
                    startover()
            elif answer3.lower()== "no":
                typing("you feel terrible as the infection begins to take over your body\n")
                typing("You keep walking and out of nowhere, a bobcat jumps out at you and you manage to kill it with your makeshift beer bottle weapon\n")
                typing("You eventually find a path, but it goes in two directions, do you go to the left or right?\n")
                answer4=input()
                if answer4.lower()== "left":
                    typing("You continue walking left\n")
                    typing("You eventually see an abandoned car\n")
                    typing("Do you investigate?\n")
                    answer5=input()
                    if answer5.lower()== "yes":
                        find_knife()
                        answer6=input()
                        if answer6.lower()== "yes":
                            make_coat()
                            answer7=input()
                            if answer7.lower()== "yes":
                                typing("You drink form the creek and your stomach begins to hurt, you hope it's just the lack of food\n")
                                typing("You continue walking and you find a water proof box on bridge that goes over the creek.  In it, you find a lighter and a few granola bars\n")
                                typing("You eat the granola bars and your stomach feels worse.  You then succomb to influenza and you die\n")
                                typing("GAME OVER\n")
                                startover()
                            elif answer7.lower()== "no":
                                no_drink()
                                startover()
                        elif answer6.lower()== "no":
                            rest_death()
                            startover()
                    elif answer5.lower()== "no":
                        typing("You continue walking\n")
                        typing("The bandage you made from your pant leg is getting very bloody.  Do you make another?\n")
                        answer6=input()
                        if answer6.lower()== "yes":
                            typing("You make another bandage and your wound feels better\n")
                        elif answer6.lower()== "no":
                            typing("You keep the same bandage on and you continue\n")
                elif answer4.lower()== "right":
                    walk_right()
                    startover()


game()
