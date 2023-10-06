#!/usr/bin/env python3

import crayons

def commandpush(devicecmd):

    for ip in devicecmd.keys():
        print(f'Handshaking. .. ... connecting with {crayons.green(ip)}')

        for mycmds in devicecmd[ip]:
            print(f'Attempting to send command --> {crayons.cyan(mycmds)}')

    return None

def devicereboot(ips):
    for ip in ips:
        print(f'Connecting to... {crayons.red(ip)}, REBOOTING NOW!')

def main():

    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print("Welcome to the network device command pusher")

    print("\nData set found\n")

    commandpush(devicecmd)

    ip_list=['192.168.0.1','10.32.1.50']

    devicereboot(ip_list)

main()
