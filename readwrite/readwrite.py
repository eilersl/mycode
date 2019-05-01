#!/usr/bin/env python3

firstfile = open("firstfile.txt", "w")
print("First text!\n", file=firstfile)
firstfile.close()

myfile = open("mytxtfile.txt", "w")
myfile.write("My SECOND Text!\n")
myfile.close()

with open("thirdfile.txt", "w") as f:
    f.write("third text\n")
    print("Where does this go?")

print("All done")

with open("thirdfile.txt", "r") as r:
    ourtext = r.read()
    print(ourtext)
