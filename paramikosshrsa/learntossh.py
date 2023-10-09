#!/usr/bin/python3

import os
import paramiko

def commandissue(command_to_issue, sshsession):
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read()

def main():
    sshsession = paramiko.SSHClient()

    #Mykey is private key
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    #If we never went to this host, add fingerprint to known host file
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #creds to connect
    sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

    #Simple list of commands to issue
    our_commands = ["touch sshworked.txt", "touch create.txt", "touch file3.txt", "ls"]

    for x in our_commands:
        print(commandissue(x, sshsession).decode('utf-8'))

main()
