from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from wtforms.fields.core import Label
from files.temperature import Temp

#Creates the Flask app
app = Flask(__name__)

#Creates the pages, using get method to call page
class HomePage(MethodView):
    
    def get(self):
        return render_template('index.html')

class CaloriesFormPage(MethodView):
    def get(self):
        calorie_form = CalorieForm()
        return render_template('calories_form_page.html', caloriesform=calorie_form)

#Creates the calorie form that inherits from the wtforms, forms. 
class CalorieForm(Form):
    weight = StringField(label = 'Weight: ' , default = 175)
    height = StringField(label= 'Height: ' , default = 68 )
    age = StringField(label = 'Age: ', default = 21)

    city= StringField(label = 'City: ' , default = "San Diego")
    country= StringField(label = 'Country: ' , default = "USA")

    button = SubmitField('Calculate Calories')




#Creates a calorie class that takes in weight, height, age and temperature
#Has a calculate method that calculates calories needed

class Calorie:
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        calories = 10 * self.weight + 6.5 * self.height - self.temperature * 10
        return calories


if __name__ == "__main__":
    temperature = Temp(country="usa", city="San Marcos").get()
    calorie = Calorie(weight=185, height=68, age=27, temperature=temperature)
    print (calorie.calculate())

#Adds URL rules, when the URL is called, load the page and page name
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form_page', view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)