"""Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value
Call your function for three different cities, at least one of which is not in the default country."""

def describe_city(city, country='UAE'):
    msg = city.title() + " is a city in " + country.title() + "."
    print(msg)
describe_city('Ajman')
describe_city('New Delhi', 'India')
describe_city('Ras al Khaimah')
