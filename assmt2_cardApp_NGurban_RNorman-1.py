# read_card_file: Open CSV file and load data to memory.
def read_card_file(filepath):
    global CardId
    global CardName
    global CardMana
    global CardColor
    global CardType
    global CardRarity

    try:
        card_file = open(filepath)
        card_file_text = card_file.read()
        card_file.close()
        card_table = card_file_text.split("\n")
    except:
        print("Could not load from file: '" + filepath + "' not found.")
        return

    i = 0
    while i < len(card_table):
        line_data = card_table[i].split(",")
        CardId.append(line_data[0])
        CardName.append(line_data[1])
        CardMana.append(line_data[2])
        CardColor.append(line_data[3])
        CardType.append(line_data[4])
        CardRarity.append(line_data[5])
        i += 1
    ##print(card_data)
    print("Cards loaded from file.")

# write_card_data: Write data in memory to the declared file in CSV format.
def write_card_data(filepath):
    # If there is only the header, no save is made.
    if len(CardId) > 1:
        output_text = ""
        i = 0
        while i < len(CardId):
            if i > 0:
                output_text += "\n"
            output_text += CardId[i] + "," + CardName[i] + "," + CardMana[i] + ","
            output_text += CardColor[i] + "," + CardType[i] + "," + CardRarity[i]
            i += 1
        card_file = open(filepath, "w+")
        card_file.write(output_text)
        card_file.close()
    else:
        print("No data to write to file.")

# print_cards_v2: Formats and prints the provided parallel arrays to a neat grid. v2 doesn't use global variables for inputs.
def print_cards_v2(id_arr, nam_arr, man_arr, col_arr, typ_arr, rar_arr):
    if len(id_arr) <= 1:
        print("No cards to show")
    else:
        i = 1
        max_name_len = 9
        max_mana_len = 11
        max_color_len = 5
        max_type_len = 4
        max_rarity_len = 6
        # find maximum field lengths for pretty formatting
        while i < len(id_arr):
            if  max_name_len < len(nam_arr[i]):
                max_name_len = len(nam_arr[i])
            if  max_mana_len < len(man_arr[i]):
                max_mana_len = len(man_arr[i])
            if  max_color_len < len(col_arr[i]):
                max_color_len = len(col_arr[i])
            if  max_type_len < len(typ_arr[i]):
                max_type_len = len(typ_arr[i])
            if  max_rarity_len < len(rar_arr[i]):
                max_rarity_len = len(rar_arr[i])
            i += 1

        line_string = "{0:3}| {1:" + str(max_name_len) + "} | {2:" + str(max_mana_len) + "} | {3:" + str(max_color_len) + "} | {4:" + str(max_type_len) + "} | {5:" + str(max_rarity_len) + "}"
        #print(headerString)
        #print(lineString)

        # print the whole thing
        print(line_string.format("Id", "Name", "Mana Value", "Color", "Type", "Rarity"))
        i = 1
        while i < len(id_arr):
            print(line_string.format(id_arr[i], nam_arr[i], man_arr[i], col_arr[i], typ_arr[i], rar_arr[i]))
            i += 1

# add_cards: Allows the user to add multiple cards, confirming before each card is added.
def add_cards():
    global CardId
    global CardName
    global CardMana
    global CardColor
    global CardType
    global CardRarity

    another_card = input("Do you want to add a new card to the database? (Y/N) ")
    while another_card.lower() != "n":
        # prompt user to add new card details
        new_card_name = input("Please enter the new card's name: ")
        new_card_mana = input("Please enter the new card's mana value: ")
        new_card_color = input("Please enter the new card's colors: ")
        new_card_type = input("Please enter the new card's type: ")
        new_card_rarity = input("Please enter the new card's rarity: ")

        # if card information is wrong, give the user a chance to fix their mistake
        print("Does this match your card's information?")
        print("  " + new_card_name + " | " + new_card_mana + " | " + new_card_color + " | " + new_card_type + " | " + new_card_rarity)
        card_correct = input("Press 'N' if incorrect, otherwise press Enter.")

        # if card is correct, add card details as a new line on the bottom of csv
        if card_correct.lower() != "n":
            # assign card database id, and add to card_data
            CardId.append(str(len(CardId)))
            CardName.append(new_card_name)
            CardMana.append(new_card_mana)
            CardColor.append(new_card_color)
            CardType.append(new_card_type)
            CardRarity.append(new_card_rarity)
        # In case card info is incorrect, print message to acknowledge.
        else:
            print("Card not accepted.")
        # Then allow user to enter a new card.
        another_card = input("Do you want to add another card to the database? (Y/N) ")


# remove_cards: Allows the user to remove multiple cards, confirming before each card is removed.
def remove_cards():
    global CardId
    global CardName
    global CardMana
    global CardColor
    global CardType
    global CardRarity

    another_card = input("Do you want to remove a card from the database? (Y/N) ")
    while another_card.lower() != "n":
        # prompt user to add new card details
        card_id = 0
        input_id = input("Please enter the card ID you wish to remove: ")
        if input_id.isnumeric():
            card_id = int(input_id)
            if card_id == 0:
                card_correct = "n"
            elif card_id > len(CardId):
                card_correct = "n'"
            else:
                # if card information is wrong, give the user a chance to fix their mistake
                print("Does this match your card's information?")
                print("{0:3}| {1:0} | {2:0} | {3:0} | {4:0} | {5:0}".format(CardId[card_id], CardName[card_id], CardMana[card_id], CardColor[card_id], CardType[card_id], CardRarity[card_id]))
                card_correct = input("Press 'N' if incorrect, otherwise press Enter.")
        else:
            card_correct = "n"

        # if card is correct, add card details as a new line on the bottom of csv
        if card_correct.lower() != "n":
            row_removed = False
            new_card_id = []
            new_card_name = []
            new_card_mana = []
            new_card_color = []
            new_card_type = []
            new_card_rarity = []

            i = 0
            while i < len(CardId):
                if i == card_id:
                    row_removed = True
                else:
                    if row_removed:
                        new_card_id.append(str(i - 1))
                    else:
                        new_card_id.append(str(i))
                    new_card_name.append(CardName[i])
                    new_card_mana.append(CardMana[i])
                    new_card_color.append(CardColor[i])
                    new_card_type.append(CardType[i])
                    new_card_rarity.append(CardRarity[i])
                i += 1

            CardId = new_card_id
            CardName = new_card_name
            CardMana = new_card_mana
            CardColor = new_card_color
            CardType = new_card_type
            CardRarity = new_card_rarity
        # In case card info is incorrect, print message to acknowledge.
        else:
            print("Card not accepted.")
        # Then allow user to enter a new card.
        another_card = input("Do you want to remove another card from the database? (Y/N) ")


# card_search: Prompts a user to choose a search field and a search term, then prints all cards in memory that match that criteria.
def card_search(id_arr, nam_arr, man_arr, col_arr, typ_arr, rar_arr):
    # Function is recursive to allow the user to refine search results.
    search_cat_list = []
    no_field_input = True
    while no_field_input:
        no_field_input = False
        search_cat = input("Please enter your search field (Id, Name, Mana Value, Color, Type, Rarity): ")
        if search_cat.lower() in "id":
            search_cat_list = id_arr
        elif search_cat.lower() in "name":
            search_cat_list = nam_arr
        elif search_cat.lower() in "mana value":
            search_cat_list = man_arr
        elif search_cat.lower() in "color":
            search_cat_list = col_arr
        elif search_cat.lower() in "type":
            search_cat_list = typ_arr
        elif search_cat.lower() in "rarity":
            search_cat_list = rar_arr
        else:
            print("--Incorrect search field input, please try again--")
            no_field_input = True

    user_input = input("Please enter your search term: ")

    # result_id always includes 0 to grab the headers. This keeps the array formatting uniform.
    # but then the iteration starts at i = 1, so we don't grab the headers twice.
    result_id = [0]
    i = 1
    while i < len(search_cat_list):
        if user_input.lower() in search_cat_list[i].lower():
            result_id.append(id_arr[i])
        i += 1

    search_card_id = []
    search_card_name = []
    search_card_mana = []
    search_card_color = []
    search_card_type = []
    search_card_rarity = []

    i = 0
    while i < len(result_id):
        search_card_id.append(CardId[int(result_id[i])])
        search_card_name.append(CardName[int(result_id[i])])
        search_card_mana.append(CardMana[int(result_id[i])])
        search_card_color.append(CardColor[int(result_id[i])])
        search_card_type.append(CardType[int(result_id[i])])
        search_card_rarity.append(CardRarity[int(result_id[i])])
        i += 1
    print_cards_v2(search_card_id, search_card_name, search_card_mana, search_card_color, search_card_type, search_card_rarity)

    refine_search = input("Do you want to refine your search? (Y/N) ")
    if refine_search.lower() != "n":
        card_search(search_card_id, search_card_name, search_card_mana, search_card_color, search_card_type, search_card_rarity)



### Main Program ###

print("Welcome to the card database project")

# parallel arrays to hold data
# CardId[]: List of card Ids in parallel array. Ids should equal the position in the array, eg CardId[3] = "3". Stored as strings of integers.
CardId     = []
# CardName[]: List of card names in parallel array. Stored as strings.
CardName   = []
# CardMana[]: List of card mana values in parallel array. Stored as strings.
CardMana   = []
# CardColor[]: List of card color types in parallel array. Stored as strings.
CardColor  = []
# CardType[]: List of card types in parallel array. Stored as strings.
CardType   = []
# CardRarity[]: List of card rarities in parallel array. Stored as strings.
CardRarity = []

# readCardFilePath: string which describes the filePath when "2: Load" option is used.
readCardFilePath = "cardData.csv"
# writeCardFilePath: string which describes the filePath when "6: Save" option is used.
writeCardFilePath = "cardData.csv"
#backupFilePath = "backupCardData.csv"

while True:
    # Menu
    print("What would you like to do?")
    print(" 1: Load records from file")
    print(" 2: See card list")
    print(" 3: Add new card")
    print(" 4: Remove card")
    print(" 5: Search for cards")
    print(" 6: Save records to file")
    print(" 7: Exit")
    ######################################################
    menuInput = input("Please type the menu number item: ")

    if menuInput == "1":
        print("--Loading cards from file: " + readCardFilePath + "--")
        read_card_file(readCardFilePath)

    elif menuInput == "2":
        print("--Showing card list--")
        print_cards_v2(CardId, CardName, CardMana, CardColor, CardType, CardRarity)

    elif menuInput == "3":
        print("--Adding new cards--")
        add_cards()

    elif menuInput == "4":
        print("--Removing cards--")
        remove_cards()

    elif menuInput == "5":
        print("--Card search--")
        card_search(CardId, CardName, CardMana, CardColor, CardType, CardRarity)

    elif menuInput == "6":
        print("--Saving cards to file: " + writeCardFilePath + "--")
        write_card_data(writeCardFilePath)

    elif menuInput == "7":
        print("Exiting program. Have a good day!")
        break

    else:
        print("Invalid choice, please try again.")
