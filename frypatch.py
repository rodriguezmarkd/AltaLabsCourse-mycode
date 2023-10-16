#!/usr/bin/python3
"""A silly little py patch"""

FIXME = "fry"

def main():

    print("Remote Code Execution -RCE- Alert! Critical patch!")
    print("Patching for host {}".format(FIXME))

    hn = input("What is your hostname?")

    backupip = input("What is the IP of the backup server?")

    backuppw = getpass.getpass("What is the password of the backup server?")

    yourip = input("What is the IP of your system?")

    with open("patched.proof", "w") as patching:
        patching.write(hn + "\n")
        patching.write(backupip + "\n")
        patching.write(backuppw + "\n")
        patching.write(yourip + "\n")

if __name__ == "__main__":
    main()

