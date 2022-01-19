#Creates a calorie class that takes in weight, height, age and temperature
#Has a calculate method that calculates calories needed

class Calorie:
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        pass 