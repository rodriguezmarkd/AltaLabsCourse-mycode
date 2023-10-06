#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=5&category=15&difficulty=medium&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()


    print(data)

    for i in range(0,5):
        print(data['results'][i]['question'])
        print("\t", data['results'][i]['incorrect_answers'])
        print("\t", data['results'][i]['correct_answer'])

if __name__ == "__main__":
    main()
