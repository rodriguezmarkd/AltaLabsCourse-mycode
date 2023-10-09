#!/usr/bin/env python3

import paramiko
import os

def main():
    """runtime"""

    #Where to connect to, SSH transport attaches to stream
    t = paramiko.Transport("10.10.2.3", 22)

    #how to connect
    t.connect(username="bender", password="alta3")

    #Make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    #iterate across files within a directory
    for x in os.listdir("/home/student/filestocopy/"):
            if not os.path.isdir("/home/student/filestocopy/"+x):
                sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)

    #close connection
    sftp.close()
    t.close()

if __name__ == "__main__":
    main()
