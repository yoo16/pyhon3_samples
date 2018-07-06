import pgsql

class Instrument(pgsql.Pgsql):
    table_name = 'instruments'
    dbname = 'sample'
    host = 'localhost'
