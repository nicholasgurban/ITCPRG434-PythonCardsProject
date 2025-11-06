def readCardFile(filepath):
    # Open csv, load data
    cardFile = open(filepath)
    cardFileText = cardFile.read()
    cardFile.close()

    cardTable = cardFileText.split("\n")

    cardData = []
    i = 0
    while i < len(cardTable):
        lineData = cardTable[i].split(",")
        cardData.append(lineData)
        i += 1
    ##print(cardData)
    return cardData

def printCards(cardData):
    if len(cardData) == 1:
        print("No cards to show")
    else:
        i = 1
        maxNameLen = 9
        maxManaLen = 11
        maxColorLen = 5
        maxTypeLen = 4
        maxRarityLen = 6
        # find maximum field lengths for pretty formatting
        while i < len(cardData):
            if maxNameLen < len(cardData[i][1]):
                maxNameLen = len(cardData[i][1])
            if maxManaLen < len(cardData[i][2]):
                maxManaLen = len(cardData[i][2])
            if maxColorLen < len(cardData[i][3]):
                maxColorLen = len(cardData[i][3])
            if maxTypeLen < len(cardData[i][4]):
                maxTypeLen = len(cardData[i][4])
            if maxRarityLen < len(cardData[i][5]):
                maxRarityLen = len(cardData[i][5])
            i += 1

        headerString = "Id | {0:" + str(maxNameLen) + "} | {1:" + str(maxManaLen) + "} | {2:" + str(maxColorLen) + "} | {3:" + str(maxTypeLen) + "} | {4:" + str(maxRarityLen) + "}"
        lineString = "{0:3}| {1:" + str(maxNameLen) + "} | {2:" + str(maxManaLen) + "} | {3:" + str(maxColorLen) + "} | {4:" + str(maxTypeLen) + "} | {5:" + str(maxRarityLen) + "}"
        #print(headerString)
        #print(lineString)

        # print the whole thing
        print(headerString.format("Name", "Mana Value", "Color", "Type", "Rarity"))
        i = 1
        while i < len(cardData):
            print(lineString.format(cardData[i][0],cardData[i][1],cardData[i][2],cardData[i][3],cardData[i][4],cardData[i][5]))
            i += 1

def cardSearch(cardData):
    fieldId = -1
    while fieldId < 0:
        i = 0
        userInput = input("Please enter your search field (Id, Name, Mana Value, Color, Type, Rarity): ")
        while i < len(cardData[0]):
            if userInput.lower() in cardData[0][i].lower():
                fieldId = i
                #print(cardData[0][fieldId])
                break
            i += 1
        if fieldId < 0:
            print("--Incorrect search field input, please try again--")

    userInput = input("Please enter your search term: ")
    searchData = []
    searchData.append(cardData[0])
    i = 1
    while i < len(cardData):
        if userInput.lower() in cardData[i][fieldId].lower():
            searchData.append(cardData[i])
        i += 1
    printCards(searchData)

    userInput = input("Do you want to refine your search? (Y/N) ")
    print(userInput)
    if userInput.lower() == "y":
        cardSearch(searchData)



print("Welcome to the card database project")
print("Loading cards...")
while True:
    cardData = readCardFile("sampleCardData.csv")

    # Menu
    print("What would you like to do?")
    print(" 1: See card list")
    print(" 2: Add new card")
    print(" 3: Remove card")
    print(" 4: Search for cards")
    print(" 5: Exit")

    ######################################################
    menuInput = input("Please type the menu number item: ")
    if menuInput == "1":
        print("--Showing card list--")
        printCards(cardData)



    elif menuInput == "2":
        print("--Adding new cards--")

        cardIncorrect = True
        while cardIncorrect:
            newCardName = input("Please enter the new card's name: ")
            newCardMana = input("Please enter the new card's mana value: ")
            newCardColor = input("Please enter the new card's colors: ")
            newcardType = input("Please enter the new card's type: ")
            newCardRarity = input("Please enter the new card's rarity: ")
            print("Does this match your card's information?")
            print("" + newCardName + " | " + newCardMana + " | " + newCardColor + " | " + newcardType + " | " + newCardRarity)
            userInput = input("Press 'N' if incorrect, otherwise press Enter.")
            if userInput.lower() != "n":
                cardIncorrect = False
        
        newCardId = len(cardData)
        newCardInfo = "" + newCardName + "," + newCardMana + "," + newCardColor + "," + newcardType + "," + newCardRarity
        newCardLine = "\n" + str(newCardId) + "," + newCardInfo

        cardFile = open("sampleCardData.csv","a")
        cardFile.write(newCardLine)
        cardFile.close()



    elif menuInput == "3":
        print("--Removing cards--")




    elif menuInput == "4":
        print("--Card search--")
        cardSearch(cardData)

    elif menuInput == "5":
        print("Exiting program. Have a good day!")
        break

    else:
        print("Invalid choice, please try again.")






'''
cardFile = open("sampleCardData.csv","w")
cardFile.write(updatedFileText)
cardFile.close()
'''

"""
updatedFileText = cardFileText + newCardLine

cardFile.write(updatedFileText)
"""




"""
for card in cardTable:
    print(card)


line1 = cardTable[1]
line1split = line1.split(",")
print(line1split)
"""


cardFile.close()