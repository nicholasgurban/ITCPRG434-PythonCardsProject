"""
A simple database program for Magic the Gathering cards.
Loads cards from a .CSV file, and lets the user add to the file.

Developed by Nicholas Gurban and Robert Norman
"""


# Open csv, load data
filepath = "sampleCardData.csv"

cardFile = open(filepath)
cardFileText = cardFile.read()
cardFile.close()


# splits csv file into table structure
# newline split to separate cards
cardTable = cardFileText.split("\n")

# loop over each card to split it into its data fields
cardData = []
i = 0
while i < len(cardTable):
    lineData = cardTable[i].split(",")
    cardData.append(lineData)
    i += 1
# finished reading cards from file

###################################################################

# A loop to allow the user to add multiple cards, confirming before each card is added.
anotherCard = input("Do you want to add a new card to the database? (Y/N) ")
while anotherCard.lower() != "n":
    # prompt user to add new card details
    newCardName = input("Please enter the new card's name: ")
    newCardMana = input("Please enter the new card's mana value: ")
    newCardColor = input("Please enter the new card's colors: ")
    newCardType = input("Please enter the new card's type: ")
    newCardRarity = input("Please enter the new card's rarity: ")

    # if card information is wrong, give the user a chance to fix their mistake
    print("Does this match your card's information?")
    print("  " + newCardName + " | " + newCardMana + " | " + newCardColor + " | " + newCardType + " | " + newCardRarity)
    cardCorrect = input("Press 'N' if incorrect, otherwise press Enter.")

    # if card is correct, add card details as a new line on the bottom of csv
    if cardCorrect.lower() != "n":
        # assign card database id, and put details in csv format
        newCardId = len(cardData)
        newCardInfo = "" + newCardName + "," + newCardMana + "," + newCardColor + "," + newCardType + "," + newCardRarity
        newCardLine = "\n" + str(newCardId) + "," + newCardInfo

        # append new line to csv
        cardFile = open(filepath, "a")
        cardFile.write(newCardLine)
        cardFile.close()

    # In case card info is incorrect, print message to acknowledge.
    else:
        print("Card not accepted.")

    # Then allow user to enter a new card.
    anotherCard = input("Do you want to add another card to the database? (Y/N) ")

print("Closing program.")