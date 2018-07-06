import pgsql

class Spot(pgsql.Pgsql):
    table_name = 'spots'
    dbname = 'sample'
    host = 'localhost'
