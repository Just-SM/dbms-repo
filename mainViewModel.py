from tkinter import E
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class datamodel(object):
    def __init__(self):
        self.username = "postgres"
        self.password = "root"
        self.host = "127.0.0.1"
        self.port = "5432"
        self.listOfSchemas = [('Not Found',)]
        self.listOfTables = [('Not Found',)]
        self.listOfContent = [('Not Found',)]
        self.listOfColumns = [('Not Found',)]
        self.rowAddData = []
        self.cursor = None
        self.currSchema = ""
        self.currTable = ""
        self.currRowPick = -1 
        super().__init__()

    def chekCon(self):
        try:
            # Подключение к существующей базе данных
            connection = psycopg2.connect(user=self.username,
                                        password=self.password,
                                        host=self.host,
                                        port=self.port)
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            # Курсор для выполнения операций с базой данных
            self.cursor = connection.cursor()
            return True
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
            return False
            

    def loadSchemas(self,cursor):
        cursor.execute("""  SELECT TABLE_SCHEMA from INFORMATION_SCHEMA."tables" t
                        WHERE not TABLE_SCHEMA = 'pg_catalog' and not TABLE_SCHEMA = 'information_schema'
                        group by TABLE_SCHEMA""")
        self.listOfSchemas = cursor.fetchall()
        return self.listOfSchemas
    
    def loadTables(self,cursor,schema):
        # print(schema)
        cursor.execute(f"""     SELECT TABLE_NAME from INFORMATION_SCHEMA."tables" t 
                            WHERE TABLE_SCHEMA = '{schema}'""")
        self.listOfTables = cursor.fetchall() 
        return self.listOfTables 

    def loadTableContent(self,cursor,table):
        temp = ""
        for col in self.listOfColumns:
            temp += col[0] + ","
        
        cursor.execute(f"""     SELECT {temp[:-1]} FROM {self.currSchema}.{table}""")
        self.listOfContent = cursor.fetchall()
        return self.listOfContent
  

    def loadTableColumns(self,cursor,table):
        cursor.execute(f"""     SELECT COLUMN_NAME from INFORMATION_SCHEMA."columns"
                            WHERE TABLE_NAME = '{table}'""")
        self.listOfColumns = cursor.fetchall()
        return self.listOfColumns

    def postData(self,cursor):
        temp = ""
        for x in self.listOfColumns:
            temp += x[0] + ","
        print(str(temp))
        try:
            cursor.execute(f"""     INSERT INTO {self.currSchema}.{self.currTable}
                                    ({str(temp)[:-1]})
                                    VALUES({str(self.rowAddData)[1:-1]});""")
        except Exception as e:
            print(str(e))
            return str(e)
    
    def updateVal(self,cursor,data):
        newVal = data[0]
        row = data[1]
        col = data[2]
        where = ""
        for i in range(len(self.listOfColumns)):
            where += str(self.listOfColumns[i][0]) + " = '" + str(self.listOfContent[row][i]) +"' and "
        try:
            cursor.execute(f"""     UPDATE {self.currSchema}.{self.currTable}
                                    SET {self.listOfColumns[col][0]}='{newVal}'
                                    WHERE {where[:-5]}""")
        except Exception as e:
            print(str(e))
            return str(e)


    def deleteVal(self,cursor,row):
        where = ""
        for i in range(len(self.listOfColumns)):
            where += str(self.listOfColumns[i][0]) + " = '" + str(self.listOfContent[row][i]) +"' and "
        try:
            cursor.execute(f"""     DELETE FROM {self.currSchema}.{self.currTable}
                                    WHERE {where[:-5]}""")
            self.currRowPick = -1
        except Exception as e:
            print(str(e))
            return str(e)


    def runQuery(self,cursor,query):
        if cursor is None:
            return "Non connected to DB!"
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
            return str(e)

    def createNewTable(self,cursor,tableName,dataList):
        try:
            cursor.execute(f"""     CREATE TABLE {self.currSchema}.{tableName}
                                    ({dataList});""")
        except Exception as e:
            print(str(e))
            return str(e)
