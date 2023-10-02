import mysql.connector

__cnx = None


def get_connection():
    global __cnx
    __cnx = mysql.connector.connect(user='root', password='guru2430',
                                    host='127.0.0.1',
                                    database='grocery')
    # print(__cnx)
    return __cnx
# get_connection()
