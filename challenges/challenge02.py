#!/usr/bin/env python3
favs = [26, 52, 4, 498, 102]
approved_channels = [26, 52, 4, 498, 102]
message = "We recommend the following channel package: "
for x in favs:
    print("\nSelect one of the following channels: " + x, ends="")
    if channel == 4:
        message = message + "Basic"
    elif channel == 26:
        message = message + "Standard"
    elif channel == 52:
        message = message + "Premium"
    elif channel == 102:
        message == message + "HD"
    elif channel == 498:
        message == message + "Expensive Extras"
    else:
        x not in approved_vendors
        print(" - NOT A RECOGNIZED CHANNEL!", end="")
