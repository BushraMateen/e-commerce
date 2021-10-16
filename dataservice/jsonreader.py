# Python program to read
# json file

from product import product
import json

def loadfile():
# Opening JSON file
    f = open('dataservice\product.json',encoding='utf8')

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    f.close()
    return data



def get_product_list():
    productlist=[]
    data=loadfile()
    for i in data:
        #print(i["product_name"])
        p1 = product(i["title"],i["price"],i["description"],i["category"],
        i["image"],i["rating"]["rate"],i["rating"]["count"])
        productlist.append(p1)
    return productlist


    # Iterating through the json
    # list
    #print(data[2])
    # for i in data[2]:
    #     print(data[2][i])
    

    
        # for j in i:
        #     print(i)
    #print(data[1])
    # Closing file
  

