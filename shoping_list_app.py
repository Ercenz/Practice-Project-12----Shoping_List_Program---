item_list = []


def addItemToList():
    user_add_item = input("Add item to your shopping list: ")
    item_list.append(user_add_item)
    print(user_add_item + " added to list.")


def removeItemFromList():
    user_remove_item = input("Remove an item from your list: ")

    if user_remove_item in item_list:
        item_list.remove(user_remove_item)
        print(user_remove_item + " removed from list.")
    else:
        print(user_remove_item + " is not in the list.")


def showItemsInList():
    if len(item_list) == 0:
        print("Your shopping list is empty.")
    else:
        print("Shopping List:")
        for item in item_list:
            print("- " + item)


def searchItemInList():
    user_search_for_item = input("Search for an item: ")

    if user_search_for_item in item_list:
        print(user_search_for_item + " is in your list.")
    else:
        print(user_search_for_item + " is not in your list.")


def main():

    while True:
        print("\nChoose an option:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Show Items")
        print("4. Search for Item")
        print("5. Exit")

        choice = input("Select 1 - 5: ")

        if choice == "1":
            addItemToList()

        elif choice == "2":
            removeItemFromList()

        elif choice == "3":
            showItemsInList()

        elif choice == "4":
            searchItemInList()

        elif choice == "5":
            print("Cya later aligater!")
            break

        else:
            print("Invalid option. Please choose 1 - 5.")


main()