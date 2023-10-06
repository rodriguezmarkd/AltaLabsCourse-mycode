#!/usr/bin/env python3

import requests

#This is the base API
API = "https://api.magicthegathering.io/v1"

def main():

    #creates resp, which is the request object
    resp = requests.get(f"{API}sets")

    print(dir(resp))

if __name__ == "__main__":
    main()
