import autoloader
from area import Area
from country import Country

country = Country()
country.deletes()

area = Area()
area.deletes()

area_values = []
area_values.append({'name': "Asia", 'code': 'AS'})
area_values.append({'name': "North America", 'code': 'NA'})
area_values.append({'name': "South America", 'code': 'SA'})
area_values.append({'name': "Europe", 'code': 'EU'})
area_values.append({'name': "Africa", 'code': 'AF'})

for area_value in area_values:
    value = {}
    value['name'] = area_value['name']
    value['code'] = area_value['code']
    area = Area()
    area.insert(value)

country_values = []
country_values.append({'name': "Japan", 'area_code': 'AS'})
country_values.append({'name': "USA", 'area_code': 'NA'})
country_values.append({'name': "France", 'area_code': 'EU'})
country_values.append({'name': "Great Britain", 'area_code': 'EU'})
country_values.append({'name': "Germany", 'area_code': 'EU'})
country_values.append({'name': "China", 'area_code': 'AS'})
country_values.append({'name': "Egypt", 'area_code': 'AF'})

for country_value in country_values:
    area = Area()
    area.where('code', country_value['area_code'])
    area.one()

    if area.value:
        value = {}
        value['name'] = country_value['name']
        value['area_id'] = area.value['id']
        country = Country()
        country.insert(value)
