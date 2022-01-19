#Creates a temperature class that takes a country and city
#Has a get method that gets temperature information from web (webscrape)

class Temp:
    def __init__(self, country, city):
        self.county = country
        self.city = city
    
    def get(self):
        pass