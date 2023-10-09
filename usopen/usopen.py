#!/usr/bin/env python3

import os
import csv

from netmiko import ConnectHandler

def get_csv(fileloc):
    d = {} #start with an empty dictionary to fill up

    with open(fileloc, "r") as foo:
        for row in csv.DictReader(foo):
            keypair = {row['hostname']: row['driver']}
            d.update(keypair)

    return d #returns completed dictionary

def ping_router(hostname):
    response = os.system("ping -c 1 " + hostname)

    if response == 0:
        return True
    else:
        return False

def interface_check(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)

        my_command = open_connection.send_command("show ip int brief")

    except:
        my_command = "** ISSUING COMMAND FAILED **"

    finally: #no matter what, returns this
        return my_command

def login_router(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type,
                                         ip=dev_ip,
                                         username=dev_un,
                                         password=dev_pw)

        # if connection was made with no errors, function returns TRUE
        return True

    except:
        # if error occurred while making connection, function returns FALSE
        return False

def main():
    file_location = input("Host file location [Press ENTER for default: 'host_list.csv']\n>") or "host_list.csv"

    # "entry" is now a dictionary returned from get_csv() function above
    entry = get_csv(file_location)

    # Use a loop to check each device for ICMP responses
    print("\n***** BEGIN ICMP CHECKING *****")
    for switchip in entry:
        if ping_router(switchip):             # check if function returns TRUE or FALSE
            # if func returned TRUE:
            print("\n\t**HOST: - " + switchip + " - responding to ICMP\n")

        else:
            # if func returned FALSE:
            print("\n\t**HOST: - " + switchip + " - NOT responding to ICMP\n")

    # Use a loop to check each device for SSH accessability
    print("\n***** BEGIN SSH CHECKING *****")
    for switchip in entry:
        if login_router(f"{entry[switchip]}",   # check if function returns TRUE or FALSE
                        switchip,
                        "admin",
                        "alta3"):

            # if function returned true, print connectivity is UP
            print("\n\t**HOST: - " + switchip + " - SSH connectivity UP\n")

        else:
            # if function returned false, print connectivity is DOWN
            print("\n\t**HOST: - " + switchip + " - SSH connectivity DOWN\n")

                                              # Use a loop to check each device for ICMP responses
    print("\n***** BEGIN SHOW IP INT BRIEF *****")
    for switchip in entry:
        # pass values needed to make connection into interface_check() function
        # function will save its output to the "result" var
        result= interface_check(f"{entry[switchip]}",
                                switchip,
                                "admin",
                                "alta3")
        print("\n" + result)

if __name__ == "__main__":
    main()
