import random
import time

def displayIntro():
    print('You are in the land full of dragons.')
    time.sleep(2)
    print('''In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedly and hungry, and will eat you on sight.''', '\n')

def chooseCave():
    cave = ""
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave..')
    time.sleep(2)
    print('It is dark and spooky')
    time.sleep(2)
    print('A large dragon jumps out in front of you. He opens his jaw and...')
    time.sleep(2)

    dragonChoose = random.randint(1,2)

    if chosenCave == str(dragonChoose):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again?')
    playAgain = input()

