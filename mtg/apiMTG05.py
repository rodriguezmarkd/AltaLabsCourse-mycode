#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/"

def main():

    resp = requests.get(f"{API}sets")

    cardsets = resp.json().get("sets")

    for cardset in cardsets:
        print(cardset)


if __name__ == "__main__":
    main()
