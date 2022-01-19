from files.temperature import Temp


#Creates a calorie class that takes in weight, height, age and temperature
#Has a calculate method that calculates calories needed

class Calorie:
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height - self.temperature * 10
        return result
    
if __name__ == "__main__":
    temperature = Temp(country="usa", city="San Marcos").get()
    calorie = Calorie(weight=185, height=68, age=27, temperature=temperature)
    print (calorie.calculate())

