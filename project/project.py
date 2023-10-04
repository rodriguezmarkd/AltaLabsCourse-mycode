#!/usr/bin/env python3

def write_inv(inv_dict):
    outFile = open("report.inv","w")
    keys = inv_dict.keys()
    for item in keys:
        print(f"Asset: {item} \nDescription: {inv_dict[item][0]} \nQuantity: {inv_dict[item][1]}\n", file=outFile)
    outFile.close()
    print("----------------\nInventory report has been written to 'report.inv'")

def add_items():
    tmp_inv = {}
    
    print("Welcome to the inventory tracking script!\n")
    while True:
        asset = input("\nPlease enter an item asset number: ")
        description = input("Please enter an item description: ")
        qty = input("Please enter an item quantity: ")

        tmp_inv.update({ asset : [description, qty]})

        ans = input(f"\n{description} have been added, press 'y' to add another: ")
        if ans != "y":
            break
    return tmp_inv

def list_items(inv_dict):
    keys = inv_dict.keys()
    for item in keys:
        print(f"Asset: {item} \nDescription: {inv_dict[item][0]} \nQuantity: {inv_dict[item][1]}\n")

def menu():
    inventory = {}
    print("Welcome to the inventory tracking script!")

    while True:
        ans = input("Please make a selection:\n A | Add item\n B | List Items\n C | Write to File\n D | Quit\nSelection -> ")
        if ans == 'A':
            inventory = add_items()
        elif ans == 'B':
            list_items(inventory)
        elif ans == 'C':
            write_inv(inventory)
        elif ans == 'D':
            break
        else:
            print("Please make another selection")

menu()
