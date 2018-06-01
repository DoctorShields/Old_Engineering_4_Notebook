# Dice Roller
# By Dr. Shields

from random import randint
running = True

print("Dice Roller")

while running:
    userInput = input("Hit Enter to roll or x to end: ")
    if userInput == "x":
        running = False
    elif userInput == "":
        print(randint(1,6))
    else:
        print("Input should be Enter or x!")
        
