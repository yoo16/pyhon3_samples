import pgsql

class Area(pgsql.Pgsql):
    table_name = 'areas'
    dbname = 'sample'
    host = '192.168.11.56'
    columns = {
        'id': {
            'type': 'int4',
            'is_primary': True,
        },
        'name' : {
            'type': 'varchar',
            'length': 256,
            'is_required': True
        },
        'code' : {
            'type': 'varchar',
            'length': 16,
            'is_required': True
        },
    }
    primary_key = 'areas_pkey'