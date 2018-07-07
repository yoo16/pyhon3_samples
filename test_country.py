import autoloader
from country import Country

country = Country()
country.all()

print(country.sql)
print(country.values)