#!/usr/bin/env python3

import os
import paramiko

CREDS = [{'ip':'10.10.2.3', 'un':'bender'}, {'ip':'10.10.2.4','un':'fry'},{'ip':'10.10.2.5','un':'zoidberg'}]

def main():
    for host in CREDS:
        t = paramiko.Transport(host.get('ip'),22)
        t.connect(username=host.get('un'),password="alta3")

        sftp = paramiko.SFTPClient.from_transport(t)

        for x in os.listdir("/home/student/filestocopy/"):
            if not os.path.isdir("/home/student/filestocopy/"+x):
                sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)

        sftp.close()
        t.close()

if __name__ == "__main__":
    main()
