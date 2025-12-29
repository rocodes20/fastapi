import pymysql

def get_db():
    connection = pymysql.connect(
        host="localhost",
        user = "root",
        password="Pass123!",
        database="sample",
        cursorclass= pymysql.cursors.DictCursor
    )
    try:
        yield connection
    finally:
        connection.close()