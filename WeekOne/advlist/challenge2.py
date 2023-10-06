#!/usr/bin/env python3

'''
name = input("What is your name? ")

word1 = input("Tell me a adjective? ")

word2 = input("Tell me a verb? ")

word3 = input("Tell me an activity? ")

word4 = input("Tell me a noun? ")

word5 = input("Tell me a verb? ")

word6 = input("Tell me a superlative? ")

word7 = input("Tell me a adjective? ")

word8 = input("Qualititive statement (higher, lower, etc)? ")


print(f'Python is a {word1} language that lets you {word2} more {word3} and integrate your {word4} more effectively.')

print(f'You can learn to {word5} Python and see almost {word6} {word7} in productivity and {word8} maintanence costs.')

'''
word = []

for i in range(8):
    lib = input("Tell me a noun, adjective or verb: ")
    if lib.isalpha():
        word.append(lib)
    else:
        print("Word not added")
        i = i - 1

print(f'Python is a {word[0]} language that lets you {word[1]} more {word[2]} and integrate your {word[3]} more effectively.')

print(f'You can learn to {word[4]} Python and see almost {word[5]} {word[6]} in productivity and {word[7]} maintanence costs.')

print(word)
