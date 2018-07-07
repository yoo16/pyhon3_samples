import datetime as dt
import psycopg2 as pg 
import psycopg2.extras

class Pgsql:
    conditions = []
    orders = []
    table_name = ''
    columns = {}
    value = {}
    id_column = 'id'
    sql = ''
    host = 'localhost'
    dbname = ''
    port = '5432'
    user = 'postgres'

    def __init__(self, *args, **kwargs):
        self.initWhere()
        self.initOrder()
        self.sql = ''
        self.table_name = ''
        return

    @classmethod
    def setHost(self, host):
        self.host = host
        return self

    @classmethod
    def setDBName(self, dbname):
        self.dbname = dbname
        return self

    @classmethod
    def setTableName(self, table_name):
        self.table_name = table_name
        return self

    @classmethod
    def connect(self):
        self.connection_info = "host=%s port=%s dbname=%s user=%s" % (self.host, self.port, self.dbname, self.user)
        self.connection = pg.connect(self.connection_info)
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return

    @classmethod
    def query(self):
        if self.sql:
           print(self.sql)
           self.connect()
           self.cursor.execute(self.sql)
           self.connection.commit()
        return

    @classmethod
    def fetchAll(self):
        self.query()
        self.values = self.cursor.fetchall()
        return

    @classmethod
    def fetchOne(self):
        self.query()
        self.value = self.cursor.fetchone()
        self.id = id
        return

    @classmethod
    def fetch(self, id):
        self.initWhere()
        self.where(self.id_column, id)
        self.sqlSelect()
        self.fetchOne()
        return

    @classmethod
    def one(self):
        self.sqlSelect()
        self.fetchOne()
        return self
    
    @classmethod
    def all(self):
        self.sqlSelect()
        self.fetchAll()
        return self
    
    @classmethod
    def insert(self, value):
        if value: self.takeValues(value)
        self.sqlInsert()
        self.query()
        return self
    
    @classmethod
    def deletes(self):
        self.sqlDelete()
        self.query()
        return self

    @classmethod
    def takeValues(self, value):
        for column in self.columns:
            if column != 'id':
                self.value[column] = value[column]
        return self
    
    @classmethod
    def sqlSelect(self):
        self.sql = "SELECT * FROM %s" % (self.table_name)
        self.sqlWhere()
        self.sqlOrder()
        return self.sql

    @classmethod
    def sqlWhere(self):
        if self.conditions:
           where = ' AND '.join(self.conditions)
           self.sql += " WHERE " + where
        return

    @classmethod
    def sqlOrder(self):
        order = ''
        if self.orders:
           order = ','.join(self.orders)
           self.sql += " ORDER BY %s" % (order)
        return
    
    @classmethod
    def sqlInsert(self):
        if self.value is None: return ''
        sql_values = []
        sql_columns = []
        for column_name in self.columns:
            if column_name != 'id':
               column = self.columns[column_name]
               value = self.value[column_name]
               value = self.sqlValue(value, column)

               sql_values.append(value)
               sql_columns.append(column_name)

        value = ', '.join(sql_values)
        column_name = ', '.join(sql_columns)

        self.sql = "INSERT INTO %s (%s) VALUES (%s)" % (self.table_name, column_name, value)
        return self.sql

    @classmethod
    def sqlDelete(self):
        self.sql = "DELETE FROM %s" % (self.table_name)
        self.sqlWhere()
        return self.sql

    @classmethod
    def sqlValue(self, value, column):
        #type = column['type']
        if value is None:
            value = 'NULL'
        else:
            value = "'%s'" % (value) 
        return value
        
    @classmethod
    def initWhere(self):
        self.conditions = []
        return self

    @classmethod
    def initOrder(self):
        self.orders = []
        return self

    @classmethod
    def where(self, column, value, inequality = '='):
        condition = "%s %s '%s'" % (column, inequality, value)
        self.conditions.append(condition)
        return self
       
    @classmethod
    def order(self, column, option = 'DESC'):
        order = "%s %s" % (column, option)
        self.orders.append(order)
        return self 
