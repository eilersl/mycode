#!/usr/bin/env python3

## python3 -m pip install --user pyexcel
## python3 -m pip install --user pyexcel--xls


import pyexcel


## What is the name of the excel file?
def excelname():
    varfilename = input("What is the name of the file? Do not include the extension ")
    myexcelval = { }
    varfilename = varfilename + ".xls"


## Dump excel spreadsheet to a record format friendly to python
def readexcel():
    excelrecords = pyexcel.iget_records(file_name=varfilename)
    for x in excelrecords:
        totalsocket = x["ip"] + ":" + str(x["port"])
        myexcelval.update ( { x["service"] : totalsocket } ) ## adds a new
                         ## IP and driver key:value pair to our dictionary

def main():
    excelname()
    readexcel()


main()


print(myexcelval)
