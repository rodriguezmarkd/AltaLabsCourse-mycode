#!/usr/bin/env python3

# .read() - return files contents as a string
# .readlines() - return file's lies as a list
# .seek() - move the curser around an open file

def main():
    #creates file object in read mode
    configfile = open("vlanconfig.cfg","r")

    #display file to screen
    print(configfile.read())

    #cursor would be at end of file, seeking to place cursor back at begining
    configfile.seek(0,0)

    #make a list of file lines
    configlist = configfile.readlines()
    print(configlist)

    #iterate through configlist
    for x in configlist:
        print(x.strip())

    configfile.close()


if __name__ == "__main__":
    main()
