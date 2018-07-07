import pgsql

class Country(pgsql.Pgsql):
    table_name = 'countries'
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
        'area_id' : {
            'type' : 'int4',
            'foreign': {
                'class_name': 'Area',
                'table': 'areas',
                'column': 'id',
            }
        },
    }
    primary_key = 'countries_pkey'
    foreign = {
            'countries_area_id_fkey': {
                                  'column':  'area_id',
                                  'class_name': 'Area',
                                  'foreign_table_name': 'areas',
                                  'foreign_column': 'id',
                                  },
    }