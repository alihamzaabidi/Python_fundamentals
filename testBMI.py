class body_mass_index:
    def __init__(self):
        self.weight = 0.0
        self.height = 0.0
    def set_weight(self, weight):
        self.weight = weight
    def set_height(self,height):
        self.height = height
    def calculate_bmi(self):
        self.res = self.weight / ((self.height/100)*2)
        return self.res
    def get_bmi(self):
        if self.res < 18.5:
            print("The persone is {} and underweight".format(self.res))
        elif self.res>=18.5 and self.res<25:
            print("The BMI of persone is {} and Normal".format(self.res))
        elif self.res>=25 and self.res<30:
            print("The BMI of person is {} and Overweight".formate(self.res))
        else:
            print("The person is Obesity")

def main():
    obj = body_mass_index()
    obj.set_weight(72.5)
    obj.set_height(165)
    obj.calculate_bmi()
    obj.get_bmi()
main()
    
