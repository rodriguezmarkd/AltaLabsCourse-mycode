#!/usr/bin/python3

while True:
    try:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
    except:
        print("Wrror with that file name! Try again...")

