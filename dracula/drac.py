#!/usr/bin/env python3

linecount = 0
outFile = open("outdrac.txt","w")
with open("dracula.txt","r") as foo:

    for line in foo:
        #print(line)
        if "vampire" in line.lower():
            print(line)
            linecount += 1
            print(line,file=outFile)

print(linecount, " lines in the file")
outFile.close()
