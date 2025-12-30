import pymysql

def get_db():
    connection = pymysql.connect(
        host="localhost",
        user = "root",
        password="",
        database="sample",
        cursorclass= pymysql.cursors.DictCursor
    )
    try:
        yield connection
    finally:
        connection.close()