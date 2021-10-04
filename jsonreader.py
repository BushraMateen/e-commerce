# Python program to read
# json file


import json
def loadfile():
# Opening JSON file
    f = open('product.json',encoding='utf8')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    #print(data[2])
    for i in data[2]:
        print(data[2][i])
        
    #print(data[1])
    # Closing file
    f.close()

