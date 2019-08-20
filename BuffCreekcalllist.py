from random import uniform
from time import sleep
import sys


def kms():
    typing("You continue walking and out of nowhere, a bobcat jumps out at you and kills you as you have no weapon to defend yourself\n")
    typing("GAME OVER\n")
    startover()

def go_to_woods():
    typing("You yell but nobody hears you\n")
    typing("You walk outside and find you are in the middle of the woods, and there is another shack in the distance\n")
    typing("Do you investigate?\n")

def typing(string, time=0.01):
    for char in string:
        sleep(time)
        sys.stdout.write(char)
        sys.stdout.flush()


def drink_water():
    typing("You drink form the creek and your stomach begins to hurt, you hope it's just the lack of food\n")
    typing("You continue walking and you find a water proof box on bridge that goes over the creek.  In it, you find a lighter and a few granola bars\n")
    typing("You eat a few granola bars and hope your stomach feels better.  You are also still cold.  Do you start a fire with the lighter you found?\n")


def rest_death():
    typing("You start to get very cold\n")
    typing("After another thirty minutes of walking, you start to get very tired so you lay down to rest for a little while\n")
    typing("Because you are freezing already, the only thing that kept you alive was your body movement.  You die\n")
    typing("GAME OVER\n")



def find_knife():
    typing("You find a bowie knife and banages\n")
    typing("You begin to feel a little cold, do you cut the seats to make a makeshift coat?\n")



def walk_right():
    typing("You continue walking right\n")
    typing("You fall into a shallow hole and sprain your ankle\n")
    typing("You can no longer continue and you freeze to death\n")
    typing("GAME OVER\n")


def start():
    typing("Welcome to Nathan's (probably) failed attempt at making a game\n")
    typing("You awake in a room, and there's nobody around you.  Do you investigate the room?\n")


def make_coat():
    if (uniform(1,10)) >7.5:
        typing("You have cut your hand while you were trying to cut the seat\n")
        typing("You hurridly use some of the bandages that you luckily found while searching the car\n")
    typing("You start to warm up\n")
    typing("After an hour of walking, you begin to feel thirsty.  Luckily, you see a creek up ahead.\n")
    typing("Do you drink from the creek?\n")


def start_fire():
    typing("You start a fire and warm up, but you notice the fire is getting too big and you try to put it out, but fail\n")
    typing("You start running in order to escape the massive blaze you've started and you make it to a safe spot\n")
    typing("You see a truck going down the road you are near.  You walk near the edge of the road\n")
    typing("Do you jump into the road so you know he'll see you, or do you yell for him to come help you?\n")
    typing("Please type jump or yell\n")




def man_shoot():
    typing("The man shoots you in the chest, then stabs you until you die\n")
    typing("GAME OVER\n")


def refuse_ride():
    typing("You refuse to get into his truck, but you head towards the town\n")
    typing("You see the man drive away and you think nothing more of him\n")
    typing("As you are walking towards the town, the man comes out of nowhere and stabs you.  You bleed out and die\n")
    typing("GAME OVER\n")



def man_see_false():
    typing("The man in the truck doesn't see you in time and he hits you.  You die\n")
    typing("GAME OVER\n")



def die_hypo():
    typing("You die from hypothermia\n")
    typing("GAME OVER\n")






def no_drink():
    typing("You don't drink from the creek to avoid sickness, but you pass out from dehydration and die\n")
    typing("GAME OVER\n")
