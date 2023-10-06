#!/usr/bin/env python3
"""Understanding dictionaries"""

def main():
    """Runtime Function"""

    #Create Dictionary
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor":"cisco"}

    #Display Entire Dictionary
    print(switch)

    #Prove that switch is a dictionary
    print(type(switch))

    #Display parts of a dictionary
    print(switch["hostname"])
    print(switch["ip"])

    #Request a "fake" key
    print(switch["lynx"])

#Call main function
if __name__ == " __main__":
    main()
