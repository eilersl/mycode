#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

def mac_addr():
    print("\n********** Details of Interface(s) - **********")
    for i in netifaces.interfaces():
        try:     # This is a new line, you also need to indent the next line by 4 spaces
            print("MAC: ", end="")  # This line will always print MAC without an end of line
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]["addr"]) # Prints the MAC address
        except:  # This is a new line
            print("Could not collect adapter information")  # Print an error message

def ip_addr():
    print("\n********** Details of Interface(s) - **********")
    for i in netifaces.interfaces():
        try:
            print("IP: ", end="")
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]["addr"])
        except:
            print("Could not collect adapter information")

def complete():
    print("The program is complete")

def main():
    print("Starting the main function")
    mac_addr()
    ip_addr()
    complete()

main()

