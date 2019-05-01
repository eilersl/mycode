#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# function to push commands
def commandpush(devicecmd): # devicecmd==list 
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to send command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

def  devicereboot(ip_list): # ip_list==list
    with open(ip_list, "r") as f:
        for item in ip_list:
            print("Connecting to.. ")
            print("REBOOTING NOW!\n")

# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown\n"]} # data that replaces data stored in file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    #print("\nData set found\n") # replace with function call that reads in data from file

    devicereboot(ip_list)

    ## run 
    commandpush(work2do) # call function to push commands to devices

# call our main function
main()
