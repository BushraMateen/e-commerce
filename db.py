import json
import psycopg2


# need to hnadle error
def create_connection(host,dbname,user,password):
    connection_string= "host= " + host  + " dbname= " + dbname  + "user= " + user + " password= " + password
    conn = psycopg2.connect(connection_string)
    return conn


def create_table():
    conn =  create_connection("localhost","product","postgres","bushra")
    cur = conn.cursor()
    query=("""
        CREATE TABLE product (
            uniq_id integer PRIMARY KEY,
            product_name varchar(50),
            retail_price integer,
            discounted_price integer,
            description     text,
            product_rating  text,
            overall_rating  text,
            brand  text
        )
        """)

#     cur.execute(query)
    print("table created")
       
	# close the communication with the PostgreSQL
    cur.close()
    conn.commit()






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