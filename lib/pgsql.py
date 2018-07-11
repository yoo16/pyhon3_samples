import os
import configparser
import psycopg2
import psycopg2.extras
import datetime as dt

class Pgsql:
    connection_info = ''
    connection = None
    cursor = None
    conditions = []
    orders = []
    table_name = ''
    columns = {}
    foreigns = {}
    unique = {}
    id = 0
    values = {}
    value = {}
    before_value = {}
    id_column = 'id'
    sql = ''
    host = 'localhost'
    dbname = ''
    port = '5432'
    user = 'postgres'
    except_columns = ['created_at', 'updated_at']

    def __init__(self):
        self.initWhere()
        self.initOrder()
        self.sql = ''

        if os.path.exists('config.ini'):
            config = configparser.ConfigParser()
            config.read('config.ini', 'UTF-8')
            if config:
                pgsql_setting = config.items('pgsql')
                self.setSetting(pgsql_setting)
        return

    def setSetting(self, pgsql_settings):
        if pgsql_settings:
            for pgsql_setting in pgsql_settings:
                key = pgsql_setting[0]
                value = pgsql_setting[1]
                if key == 'host':
                    self.setHost(value)
                if key == 'dbname':
                    self.setDBName(value)
                if key == 'user':
                    self.setUser(value)
                if key == 'port':
                    self.setPort(value)
        return

    def setHost(self, host):
        self.host = host
        return self

    def setDBName(self, dbname):
        self.dbname = dbname
        return self

    def setUser(self, user):
        self.user = user
        return self

    def setPort(self, port):
        self.port = port
        return self

    def setTableName(self, table_name):
        self.table_name = table_name
        return self

    def connect(self):
        connection_info = "host=%s port=%s dbname=%s user=%s" % (
            self.host, self.port, self.dbname, self.user)
        self.connection = psycopg2.connect(connection_info)
        print(self.host)
        print(self.dbname)
        return self.connection

    def query(self, sql):
        if self.sql:
            with self.connect() as con:
                with con.cursor() as cur:
                    cur.execute(sql)
                    cur.close()
            con.close()
        return self

    def queryCommit(self, sql):
        if self.sql:
            with self.connect() as con:
                with con.cursor() as cur:
                    cur.execute(sql)
                    con.commit()
                    cur.close()
            con.close()
        return self

    def fetchAll(self):
        with self.connect() as con:
            with con.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(self.sql)
                self.values = cur.fetchall()
                cur.close()
        con.close()
        print(self.sql)
        return

    def fetchOne(self):
        with self.connect() as con:
            with con.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(self.sql)
                self.value = cur.fetchone()
                cur.close()
        con.close()
        if self.value:
            self.id = self.value[self.id_column]
        return

    def fetch(self, _id):
        self.initWhere()
        self.where(self.id_column, _id)
        self.sqlSelect()
        self.fetchOne()
        return

    def one(self):
        self.sqlSelect()
        self.fetchOne()
        return self

    def all(self):
        self.sqlSelect()
        self.fetchAll()
        return self

    def insert(self, value):
        if value:
            self.takeValues(value)
        sql = self.sqlInsert()
        self.queryCommit(sql)
        return self

    def update(self, value, _id = None):
        if _id: self.fetch(_id)
        if self.value is None: return self

        if self.id > 0 and value:
            self.before_value = self.value

            sql = self.sqlUpdate(value)
            self.where(self.id_column, self.id)
            self.queryCommit(sql)
        return self

    def delete(self, _id):
        self.where(self.id_column, _id)

        sql = self.sqlDelete()
        self.query(sql)
        return self

    def deletes(self):
        sql = self.sqlDelete()
        self.query(sql)
        return self

    def takeValues(self, value):
        for column in self.columns:
            if column != self.id_column:
                self.value[column] = value[column]
        return self

    def changes(self):
        update_value = {}
        if self.value:
            for column_name in self.value:
                if not column_name in self.except_columns:
                    if self.value[column_name] != self.before_value[column_name]:
                        update_value[column_name] = self.value[column_name]

        return update_value

    def sqlSelect(self):
        self.sql = "SELECT * FROM %s" % (self.table_name)
        self.sqlWhere()
        self.sqlOrder()
        self.sql += ";"
        return self.sql

    def sqlWhere(self):
        if self.conditions:
            where = ' AND '.join(self.conditions)
            self.sql += " WHERE " + where
        return

    def sqlOrder(self):
        order = ''
        if self.orders:
            order = ','.join(self.orders)
            self.sql += " ORDER BY %s" % (order)
        return

    def sqlInsert(self):
        if self.value is None:
            return ''
        sql_values = []
        sql_columns = []
        for column_name in self.columns:
            if column_name != self.id_column:
                value = self.value[column_name]
                value = self.sqlValue(value)

                sql_values.append(value)
                sql_columns.append(column_name)

        value = ', '.join(sql_values)
        column_name = ', '.join(sql_columns)

        self.sql = "INSERT INTO %s (%s) VALUES (%s) RETURNING id" % (
            self.table_name, column_name, value)
        self.sql += ";"
        return self.sql

    def sqlUpdate(self, values):
        sql_values = []
        for column_name in values:
            if column_name != self.id_column:
                value = values[column_name]
                value = self.sqlValue(value)
                value = "%s = %s" % (column_name, value)
                sql_values.append(value)

        value = ', '.join(sql_values)

        self.sql = "UPDATE %s SET %s;\n" % (self.table_name, value)
        return self.sql

    def sqlDelete(self):
        self.sql = "DELETE FROM %s" % (self.table_name)
        self.sqlWhere()
        return self.sql

    def sqlValue(self, value):
        if type(value) is bool:
            if value:
                value = True
            else:
                value = False
        if value is None:
            value = 'NULL'
        else:
            value = "'%s'" % (value)
        return value

    def initWhere(self):
        self.conditions = []
        return self

    def initOrder(self):
        self.orders = []
        return self

    def where(self, column, value, inequality='='):
        condition = "%s %s '%s'" % (column, inequality, value)
        self.conditions.append(condition)
        return self

    def order(self, column, option='DESC'):
        order = "%s %s" % (column, option)
        self.orders.append(order)
        return self

    def createTable(self):
        sql = self.createTableSql()
        self.query(sql)

        sql = self.constraintSql()
        self.query(sql)
        return

    def createTableSql(self):
        if self.columns is None:
            return ''

        column_sql = ''
        column_type = ''
        option = ''
        column_sqls = []
        for column_name in self.columns:
            column = self.columns[column_name]
            if column_name == self.id_column:
                column_sql = 'id SERIAL PRIMARY KEY NOT NULL'
            elif column['type']:
                column_type = self.columnTypeSql(column)
                option = self.columnOptionSql(column)
                column_sql = "%s %s" % (column_name, column_type)
                if option:
                    column_sql += option
            column_sqls.append(column_sql)

        column_sql = ",\n".join(column_sqls)
        table_name = self.table_name
        self.sql = "CREATE TABLE IF NOT EXISTS \"%s\" (\n%s\n);\n" % (table_name, column_sql)
        return self.sql

    def dropTable(self):
        sql = self.dropTableSql()
        self.query(sql)
        return

    def dropTableSql(self):
        table_name = self.table_name
        self.sql = "DROP TABLE \"%s\";\n" % (table_name)
        return self.sql

    def columnTypeSql(self, column):
        if 'length' in column:
            column_type = "%s(%s)" % (column['type'], column['length'])
        else:
            column_type = column['type']
        column_type = column_type.upper()
        return column_type

    def columnOptionSql(self, column):
        option = ''
        if 'is_required' in column:
            option += ' NOT NULL'
        if 'is_default_null' in column:
            option += ' DEFAULT NULL'
        return option

    def constraintSql(self):
        sql = ''
        if self.foreigns:
            for conname in self.foreigns:
                foreign = self.foreigns[conname]
                sql += "ALTER TABLE %s\n" % self.table_name
                sql += "      ADD CONSTRAINT %s FOREIGN KEY (%s)\n" % (conname, foreign['column'])
                sql += "      REFERENCES %s (%s)\n" % (foreign['foreign_table_name'], foreign['foreign_column'])

                update_type = foreign['cascade_update_type'];
                delete_type = foreign['cascade_delete_type'];

                if update_type: sql+= "      ON UPDATE %s\n" % (update_type)
                if delete_type: sql+= "      ON DELETE %s\n" % (delete_type)
                sql+= ";\n"

        if self.unique:
            for unique_key in self.unique:
                unique_columns = self.unique[unique_key]
                unique_name = ', '.join(unique_columns)
                sql += "ALTER TABLE %s\n" % self.table_name;
                sql += "      ADD CONSTRAINT %s\n" % unique_key;
                sql += "      UNIQUE (%s);\n" % unique_name;

        return sql
