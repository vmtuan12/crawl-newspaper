import mysql.connector
from . import constants

db = mysql.connector.connect(
    host=constants.HOST,
    user=constants.USER,
    password=constants.PASSWORD,
    database=constants.DATABASE,
    port=constants.PORT
)
cursor = db.cursor()

def get_all_websites(): 
    cursor.execute("select * from website")
    rows = cursor.fetchall()

    result = []
    for row in rows: 
        result.append(row)
    
    return result

def get_categories(website_id: int):
    cursor.execute("select * from x_path_category where website_id = " + str(website_id))
    rows = cursor.fetchall()

    result = []
    for row in rows: 
        result.append(row[2])
    
    return result

def get_contents(website_id: int):
    cursor.execute("select * from x_path_content where website_id = " + str(website_id))
    rows = cursor.fetchall()

    result = []
    for row in rows: 
        result.append({"title": row[2], "content": row[3], "date": row[4]})

    return result