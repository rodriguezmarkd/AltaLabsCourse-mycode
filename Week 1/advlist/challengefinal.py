#!/usr/bin/env python3

word = []

for i in range(8):
    lib = input("Tell me a noun, adjective or verb: ")
    while lib.isalpha() == False:
        print("Word not added")
        lib = input("Tell me a noun, adjective or verb: ")
        if lib.isalpha():
            break
    word.append(lib)

print(f'Python is a {word[0]} language that lets you {word[1]} more {word[2]} and integrate your {word[3]} more effectively.')

print(f'You can learn to {word[4]} Python and see almost {word[5]} {word[6]} in productivity and {word[7]} maintanence costs.')

