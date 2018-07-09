from models.area import Area
from models.country import Country

country = Country()
country_values = []
country_values.append({'name': "Italy", 'area_code': 'EU'})

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
