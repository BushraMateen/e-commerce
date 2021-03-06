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

    conn =  create_connection("localhost","bushradb","postgres","bushra")
    cur = conn.cursor()

    for d in data:
        cur.execute("INSERT into webapp_products(title,price,description,category,image,rate,count) VALUES (%s, %s,%s,%s,%s,%s,%s)",
        (d.title,d.price,d.description,d.category,d.image,d.rate,d.count))
  
  
    print("List has been inserted to product table successfully...")

    conn.commit()
    conn.close()

