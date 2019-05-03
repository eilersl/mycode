#!/usr/bin/env python3
# Author: LEilers

"""Script to search for a pattern match"""

import os # used to walk the system
import fnmatch # for regex pattern matching
import pyexcel

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

#mypylist = [] 

#def excel_create():
#    print("Hey there! This program will make you a *.xls file!")
#    while(True):
#        mypylist.append(get

def main():
    find("*.py", "/home/student/mycode/")

main()

