import random
import operator

gameEnd = False

stacksList = []
def numOfStacks():
    stacksCount = input("How many stacks should there be total?:")
    global stacksList
    stacksList = []
    for stack in range(int(stacksCount)):
        stacksList.append(stack + 1)
numOfStacks()

stacksDict = {}
def numSticksPerStack():
    global stacksDict
    stacksDict = {}
    for stack in stacksList:
        sticksCount = input(f"How many sticks should be in stack {stack}?:")
        stacksDict["stack " + str(stack) + ":  "] = sticksCount
    pass
numSticksPerStack()

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

bvalues = []
def computerTurn():
    global gameEnd
    global bvalues
    oddness = 0
    stacksSum = 0
    bintotals = {}
    stackssum = 0
    for stack in stacksDict:
        value = stacksDict.setdefault(stack)
        stackssum += int(value)
        bvalues.append(format(int(value),'b'))
    stackssum = format(int(stackssum),'b')
    totals = []
    print(bvalues)
    lastbvalue = 0
    greatest_to_least_bvalues = []
    for bvalue in bvalues:
        if len(bvalue) > lastbvalue:
            greatest_to_least_bvalues = [bvalue] + greatest_to_least_bvalues
        else:
            greatest_to_least_bvalues = greatest_to_least_bvalues + [bvalue]
        lastbvalue = len(bvalue)
    prevlengthbvalue = 0
    for bvalue in greatest_to_least_bvalues:
        for number in bvalue[::-1]:
            totals.append(int(number))
        if prevlengthbvalue == 0:
            bincounter = 0
        else:
            bincounter = prevlengthbvalue - len(bvalue)
        print(bincounter)
        totals = totals[::-1]
        print("total =               " + str(totals))
        for num in range(1,len(totals)+1):
            bintotals.setdefault(num,0)
        print(bintotals)
        for binary in totals: 
            bincounter += 1
            print("       " + str(int(binary)))
            bintotals[bincounter] = bintotals[bincounter] + int(binary)
            print(bintotals[bincounter])
        print("bintotals  " + str(bintotals))
        totals = []
        if prevlengthbvalue == 0:
            prevlengthbvalue = len(bvalue)      
    magiccounter = 1
    xorvalue = ""
    one = 0
    for val in bintotals:
        val = bintotals.setdefault(val)
        if bintotals[magiccounter]%2 == 0:
            bintotals[magiccounter] = 1
            one = 1
        if bintotals[magiccounter]%2 != 0 and bintotals[magiccounter]%2 != 0.5 and one == 1:
            bintotals[magiccounter] = 0
        xorvalue = xorvalue + str(bintotals[magiccounter])
        magiccounter += 1
    print("xor: " + str(bintotals))
    print(greatest_to_least_bvalues)
    for bin_number in greatest_to_least_bvalues:
        print(bin_number)


    
    #for val in bintotals:
    #    val = bintotals[val]
    #    print(val)
    #    if val%2 == 0:
    #        print("even")
    #    else:
    #        oddness = 1
    #        print("odd")
    #print(stackssum)
    #for stack in stacksDict:
    #    value = stacksDict.setdefault(stack)
    #    if format(int(value),'b') == 
    

computerTurn()

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
#nimGame()
