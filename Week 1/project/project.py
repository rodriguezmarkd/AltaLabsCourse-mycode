#!/usr/bin/env python3

#Defining Inventory Dictionary to be used globally
inventory = {}

#Method used to write out Inventory Contents to File
def write_inv():
    #Creating outFile object for output file
    outFile = open("report.inv","w")
    
    #For loop to iterate through dictionary and write out contents to report.inv file
    for item in inventory.keys():
        print(f"Asset: {item} \nDescription: {inventory[item][0]} \nQuantity: {inventory[item][1]}\n", file=outFile)
    
    #Closing out file
    outFile.close()
    
    print("-----\nInventory report has been written to 'report.inv'\n-----")

#Method used to add items to the current dictionary
def add_items():
    print("\n-----\nLet's Add Some Items!!")
    
    #While loop used to allow user to add items until any key but 'y' is pressed
    while True:
        asset = input("\nPlease enter an item asset number: ")
        description = input("Please enter an item description: ")
        qty = input(f"Please enter an item quantity: ")

        #Adds item to inventory using 'asset' as key, with a list as the value
        inventory[asset] = [description, qty]

        #Prompts user if they'd like to add more items
        ans = input(f"\n {description} have been added, press 'y' to add another: ")
        
        #if statement to allow for breaking of loop
        if ans != "y":
            break

#Method used to list out items
def list_items():
    print("\n-----\nCurrent Items In Inventory:\n")
    
    #For loop to iterate through inventory and print out it's contents
    for item in inventory.keys():
        print(f"\nAsset: {item} \nDescription: {inventory[item][0]} \nQuantity: {inventory[item][1]}\n")

    print("-----\n")

#Main function to allow program to operate
def main():
    print("Welcome to the inventory tracking script!")

    #Loop to iterate through menu allowing user to make a selection
    while True:
        ans = input("\nPlease make a selection:\n A | Add item\n B | List Items\n C | Write to File\n D | Quit\nSelection -> ")
        if ans == 'A':
            inventory = add_items()
        elif ans == 'B':
            list_items()
        elif ans == 'C':
            write_inv()
        elif ans == 'D':
            break
        else:
            print("Please make another selection")

#Starting logic to run script
if __name__ == "__main__":
    main()
