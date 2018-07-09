from lib.pgsql import Pgsql

class Country(Pgsql):
    table_name = 'countries'

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
    foreigns = {
            'countries_area_id_fkey': {
                                  'column':  'area_id',
                                  'class_name': 'Area',
                                  'foreign_table_name': 'areas',
                                  'foreign_column': 'id',
                                  'cascade_update_type': 'NO ACTION',
                                  'cascade_delete_type': 'CASCADE',
                                  },
    }
    unique = {
        'countries_name_key': {
                    'name',
                    },
    }

    # def __init__(self):
    #     super().__init__()
    #     return