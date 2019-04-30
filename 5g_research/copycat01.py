#!/usr/bin/env python3

## import the shutil function
import shutil

## import the os function
import os

## change to the mycode directory
os.chdir("/home/student/mycode/")

## make a copy of the sdn_network.txt file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

## create a backup of the 5g_research directory
shutil.copytree("5g_research/", "5g_research_backup/")
