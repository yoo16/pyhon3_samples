import pgsql

class Sensor(pgsql.Pgsql):
    table_name = 'sensors'
    dbname = 'sample'
    host = 'localhost'
