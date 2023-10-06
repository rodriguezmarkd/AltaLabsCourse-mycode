#!/usr/bin/env python3
#imports shutil utility and os tool
import shutil
import os

#sets starting directory for program
os.chdir("/home/student/mycode")

#copy copies a single file, copytree copies an entire directory
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
shutil.copytree("5g_research/", "5g_research_backup/")

