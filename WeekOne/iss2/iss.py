#!/usr/bin/env python3

import requests
import datetime
import reverse_geocoder as rg

URL = "http://api.open-notify.org/iss-now.json"

def main():
    resp = requests.get(URL).json()
    ts = resp['timestamp']
    ts = datetime.datetime.fromtimestamp(ts)

    locator_resp = rg.search((resp['iss_position']['latitude'],resp['iss_position']['longitude']))
    city = locator_resp[0]["name"]
    country = locator_resp[0]["cc"]

    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {ts}")
    print(f"Lon: {resp['iss_position']['longitude']}")
    print(f"Lat: {resp['iss_position']['latitude']}")

    print(f"City/Country: {city}, {country}")

if __name__ == "__main__":
    main()


