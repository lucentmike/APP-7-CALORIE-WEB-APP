#Creates a temperature class that takes a country and city
#Has a get method that gets temperature information from web (webscrape)
import requests
from pprint import pprint
from selectorlib import Extractor

class Temp:
    def __init__(self, country, city):
        self.country = country
        self.city = city
    
    def get(self):

        #replaces spaces with dash for url
        self.city = self.city.replace(" ", "-")

        #runs a request method to site, grab contents, converts it into text
        r = requests.get(f"https://www.timeanddate.com/worldclock/{self.country}/{self.city}")
        c = r.content 
        c = r.text 

        #Use yaml file to identify the x-path of the data you want
        extractor = Extractor.from_yaml_file('files/temperature.yaml')
        #extracts the content into variable
        raw_result = extractor.extract(c)
        #extracts the number value from dictonary key
        result = float(raw_result["temp"].replace("\xa0°F", ""))

        return result