#!/usr/bin/env python3

import csv

with open("csv_users.txt","r") as csvfile:
    i = 0

    for row in csv.reader(csvfile):
        i = i + 1
        filename = f"admin.rc{i}"

        with open(filename,"w") as rcfile:
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)

# all of the indentation ends, so all files are auto closed

# display this to the screen when all of the looping is over
print("admin.rc files created!")
