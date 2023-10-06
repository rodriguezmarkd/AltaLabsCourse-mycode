#!/usr/bin/env python3

import requests

#Defines the base API
API = "https://api.magicthegathering.io/v1/"

def main():
    #Creates resp, which is request object
    resp = requests.get(f"{API}sets")

    print(resp.json())

if __name__ == "__main__":
    main()
