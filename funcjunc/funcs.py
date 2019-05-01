#!/usr/bin/env python3

def word_counter(infile, outfile):
    print("This is our word counter function")
    with open(infile, "r") as f:
        data = f.read().replace("\n", " ")
        x = data.split(" ")
        count_list = []
        for i in x:
           if i not in count_list:
               count_list.append(i)

        counted = {}

# iterate through a list
    for item in count_list:
        num = {item: x.count(item)}
        counted.update(num)

    output_file = open(outfile, "w")
    output_file.write(str(counted))
    output_file.close()

def last_func():
    ff = input("What is your input file?: ")
    lf = input("What is your output file?: ")
    return ff, lf

print(last_func())

def main():
    print("Starting the script")
    a, b = last_func()
    word_counter(a, b)

main()
