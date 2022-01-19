from files.calories import Calorie
from files.temperature import Temp
import requests
from pprint import pprint
from selectorlib import Extractor


r = requests.get()
c = r.content 
c = r.text 

#Use yaml file to identify the x-path of the data you want
extractor = Extractor.from_yaml_file('files/temperature.yaml')

extractor.extract(c)

raw_result = extractor.extract(c)
raw_result["temp"].replace("", "")

result = float(raw_result["temp"].replace("", ""))

