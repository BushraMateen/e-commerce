import json
import psycopg2
from jsonreader import get_product_list
from product import product


# need to hnadle error
def create_connection(host,dbname,user,password):
    connection_string= ("host= " + host  + " dbname= " + dbname  + " user= " + user + " password= " + password)
    conn = psycopg2.connect(connection_string)
    return conn


def create_table():
    conn =  create_connection("localhost","product","postgres","bushra")
    cur = conn.cursor()
    query=("""
        CREATE TABLE product (
            uniq_id varchar PRIMARY KEY,
            product_name text,
            retail_price text,
            discounted_price text,
            image text,
            description     text,
            product_rating  text,
            overall_rating  text,
            brand  text
        )
        """)
    cur.execute(query)
    print("table created")
    conn.commit()
    conn.close()

def add_product():
                                 
    data = get_product_list()

    conn =  create_connection("localhost","product","postgres","bushra")
    cur = conn.cursor()

    for d in data:
        cur.execute("INSERT into product(uniq_id,product_name,retail_price,discounted_price,image,description,product_rating,overall_rating,brand) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)",
        (d.uniq_id,d.product_name,d.retail_price,d.discounted_price,d.image,d.description,d.product_rating,d.overall_rating,d.brand))
  
  
    print("List has been inserted to product table successfully...")

    conn.commit()
    conn.close()



       
	# close the communication with the PostgreSQL
    






# cur.execute("""
#     CREATE TABLE product(
#     uniq_id integer PRIMARY KEY,
#     product_name text,
#     retail_price integer,
#     discounted_price integer,
#     description     text,
#     product_rating  text,
#     overall_rating  text,
#     brand  text

# )
# """)

# Check is the json object was loaded correctly
# try:    
#     print(decoded_data[0])
#     #print(decoded_data[0])
# except KeyError:
    #print("Oops! JSON Data not loaded correctly using json.loads()")