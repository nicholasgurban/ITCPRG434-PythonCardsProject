"""
A simple database program for Magic the Gathering cards.
Takes user input and adds that data to a storage array.

Developed by Nicholas Gurban and Robert Norman
"""

##########################
## Parallel Arrays go here
CardId     = [          1,               2,                 3,             4,           5]
CardName   = ["Worldfire","Galewind Moose", "Phyrexian Altar", "Dark Ritual",    "Island"]
CardMana   = [          9,               6,                 3,             1,           0]
CardColor  = [      "Red",         "Green",       "Colorless",       "Black", "Colorless"]
CardType   = [  "Sorcery",      "Creature",        "Artifact",     "Sorcery",      "Land"]
CardRarity = [   "Mythic",      "Uncommon",            "Rare",      "Common",    "Common"]
##########################

# A loop to allow the user to add multiple cards.
anotherCard = input("Do you want to add a new card to the database? (Y/N) ")
while anotherCard.lower() != "n":
    # prompt user to add new card details
    newCardName = input("Please enter the new card's name: ")
    newCardMana = input("Please enter the new card's mana value: ")
    newCardColor = input("Please enter the new card's colors: ")
    newCardType = input("Please enter the new card's type: ")
    newCardRarity = input("Please enter the new card's rarity: ")

    # add card details as a new line on the bottom of csv
    CardId.append(len(CardId) + 1)
    CardName.append(newCardName)
    CardMana.append(int(newCardMana))
    CardColor.append(newCardColor)
    CardType.append(newCardType)
    CardRarity.append(newCardRarity)

    # Then allow user to enter a new card.
    anotherCard = input("Do you want to add another card to the database? (Y/N) ")

print("Closing program.")