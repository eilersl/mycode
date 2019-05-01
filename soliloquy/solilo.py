#!/usr/bin/env python3

with open("sol.txt", "r") as f:
    data = f.read().replace("\n", " ")
    #print(data)
    x = data.split(" ")
    #print(x)
    count_list = []
    for i in x:
       if i not in count_list:
           count_list.append(i)
    print(count_list)

    counted = {}

# put data in counted {}
   
# iterate through a list
    for item in count_list:
        num = {item: x.count(item)} 
        counted.update(num)
#   print(counted)

# v = input("Which word do you want to see the number of times it occurs?: ")
# print(counted[v])

output_file = open("wordcount.txt", "w")
output_file.write(str(counted))
output_file.close()
