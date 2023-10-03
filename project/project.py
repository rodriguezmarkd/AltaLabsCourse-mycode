#!/usr/bin/env python3

def write_inv(inv_dict):
    outFile = open("report.inv","w")
    keys = inv_dict.keys()
    for item in keys:
        print(f"Asset: {item} \nDescription: {inv_dict[item][0]} \nQuantity: {inv_dict[item][1]}\n", file=outFile)
    outFile.close()



inventory = {}

while True:
    asset = input("Please enter an item asset number: ")
    description = input("Please enter an item description: ")
    qty = input("Please enter an item quantity: ")

    inventory.update({ asset : [description, qty]})

    print(inventory)
    ans = input("Item has been added, press 'y' to add another: ")
    if ans != "y":
        break


write_inv(inventory)
