from locale import currency
from tkinter.tix import Select
from unicodedata import name
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def getShemas(cursor):
    cursor.execute("""  SELECT TABLE_SCHEMA from INFORMATION_SCHEMA."tables" t
                        WHERE not TABLE_SCHEMA = 'pg_catalog' and not TABLE_SCHEMA = 'information_schema'  
                        group by TABLE_SCHEMA""")
    return cursor.fetchall()
def getTables(cursor,schema):
    cursor.execute(f"""     SELECT TABLE_NAME from INFORMATION_SCHEMA."tables" t 
                            WHERE TABLE_SCHEMA = '{schema}'""")
    return cursor.fetchall()
def getColumns(cursor,table):
    cursor.execute(f"""     SELECT COLUMN_NAME from INFORMATION_SCHEMA."columns"
                            WHERE TABLE_NAME = '{table}'""")
    return cursor.fetchall()


try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    cursor.execute("ALTER USER postgres SET search_path = CMS,private,public;")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.execute("")
        cursor.execute("select * from player")
        info = cursor.fetchall()
        print(len(info))
        print(len(info[0]))
        for x in info :
            print (x)   
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
