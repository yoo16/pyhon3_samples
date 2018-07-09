from lib.pgsql import Pgsql

class Area(Pgsql):
    table_name = 'areas'
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
    unique = {
        'areas_name_key': ['name'],
        'areas_code_key': ['code'],
    }

    # def __init__(self):
    #     super().__init__()
    #     return