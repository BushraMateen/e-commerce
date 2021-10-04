

class product:
    
    def __init__(self,uniq_id,product_name,retail_price,discounted_price,image,description,product_rating,overall_rating,brand):
        self.uniq_id = uniq_id
        self.product_name = product_name
        self.retail_price = retail_price
        self.discounted_price = discounted_price
        self.image = image
        self.description = description
        self.product_rating = product_rating
        self.overall_rating = overall_rating
        self.brand = brand

# product_string = ('{"uniq_id":"c2d766ca982eca8304150849735ffef9","product_name" : "Alisha Solid Women's Cycling Shorts","retail_price":999
# "discounted_price":379, "image":"http://img5a.flixcart.com/image/short/u/4/a/altht-3p-21-alisha-38-original-imaeh2d5vm5zbtgg.jpeg",
# "http://img5a.flixcart.com/image/short/p/j/z/altght4p-26-alisha-38-original-imaeh2d5kbufss6n.jpeg",
# "http://img5a.flixcart.com/image/short/p/j/z/altght4p-26-alisha-38-original-imaeh2d5npdybzyt.jpeg",
# "http://img5a.flixcart.com/image/short/z/j/7/altght-7-alisha-38-original-imaeh2d5jsz2ghd6.jpeg", "description" : "Key Features of Alisha Solid Women's Cycling Shorts Cotton Lycra Navy,Red, Navy,Specifications of Alisha Solid Women's Cycling Shorts Shorts Details Number of Contents in Sales Package Pack of 3 Fabric Cotton Lycra Type Cycling Shorts General Details Pattern Solid Ideal For Women's Fabric Care Gentle Machine Wash in Lukewarm Water, Do Not Bleach Additional Details Style Code ALTHT_3P_21 In the Box 3 shorts",
# "product_rating":"No rating available","overall_rating": "No rating available" ,"brand" : "Alisha"}')                    '
# product_dict=json.loads(product_string)
# product_object = product(**product)

# print(product_object)

# print(product.name)
  