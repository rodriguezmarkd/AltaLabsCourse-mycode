#!/usr/bin/env python3

import requests

def main():
    #This creates a request object
    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    #displays methods available to our new object
    print(dir(resp))

if __name__ == "__main__":
    main()
