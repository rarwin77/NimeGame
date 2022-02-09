import random

gameEnd = False

stacksList = []
def numOfStacks():
    stacksCount = input("How many stacks should there be total?:")
    global stacksList
    stacksList = []
    for stack in range(int(stacksCount)):
        stacksList.append(stack + 1)
#numOfStacks()

stacksDict = {}
def numSticksPerStack():
    global stacksDict
    stacksDict = {}
    for stack in stacksList:
        sticksCount = input(f"How many sticks should be in stack {stack}?:")
        stacksDict["stack " + str(stack) + ":  "] = sticksCount
    pass
#numSticksPerStack()

firstOrSecond = 0
def chooseFirstOrSecond():
    global firstOrSecond
    firstOrSecond = int(input("Type 1 to go first, type 2 to go second:"))
    pass

def printStacks():
    for stack in stacksDict:
        sticksCount = ""
        for count in range(int(stacksDict[stack])):
            sticksCount = sticksCount + "I "
        print(stack + str(stacksDict[stack])+ "    " + sticksCount)


def playerTurn():
    global gameEnd
    stacksSum = 0
    printStacks()
    playerStackChoice = input("From which stack would you like to remove sticks?:")
    playerStickRemovalCount = input("How many sticks do you want to remove?:")
    stacksDict["stack " + str(playerStackChoice) + ":  "] = int(stacksDict["stack " + str(playerStackChoice) + ":  "]) - int(playerStickRemovalCount)
    for stack in stacksDict:
        sticks = int(stacksDict.setdefault(stack))
        stacksSum += sticks
    if stacksSum == 0:
        gameEnd = True
        print('You win')
    pass
#playerTurn()

def computerTurn():
    global gameEnd
    stacksSum = 0
    printStacks()
    succesful = 0
    while True:
        computerStackChoice = random.randint(1,len(stacksDict))
        if succesful == 1:
            break
        if stacksDict["stack " + str(computerStackChoice) + ":  "] != 0:
            computerSticksRemoveCount = int(random.randint(1, int(stacksDict["stack " + str(computerStackChoice) + ":  "])))
            stacksDict["stack " + str(computerStackChoice) + ":  "] = int(stacksDict["stack " + str(computerStackChoice) + ":  "]) - computerSticksRemoveCount
            print(f"Computer removes {computerSticksRemoveCount} sticks from " + "stack " + str(computerStackChoice) + ":  ")
            succesful = 1
            for stack in stacksDict:
                sticks = int(stacksDict.setdefault(stack))
                stacksSum += sticks
            if stacksSum == 0:
                gameEnd = True
                print('You lose')
                break 
#computerTurn()

def nimGame():
    playAgain = 0
    global gameEnd
    gameEnd = False
    numOfStacks()
    numSticksPerStack()
    chooseFirstOrSecond()
    while gameEnd == False:
        if firstOrSecond == 1:
            playerTurn()
            if gameEnd == True:
                break
            computerTurn()
        if firstOrSecond == 2:
            computerTurn()
            if gameEnd == True:
                break
            playerTurn()
    playAgain = input("Input 'yes' to play again, input 'no' to not play again:")
    if playAgain == 'yes':
        nimGame()
nimGame()
