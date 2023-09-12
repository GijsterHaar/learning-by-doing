'''
Get the mean average temperature from various temperature units

Class Celcius
    to_celcius
    from_celcius
    __add__
    __div__
    __eq__
    __str__


Class Kelvin
    to_celcius
    from_celcius
    __add__
    __div__
    __eq__
    __str__

'''

class Kelvin:
    def __init__(self, temp): # self == Kelvin. temp == int
        self.temp = temp
        #return None

    def __eq__(self, other): # self == Kelvin, other == Kelvin
        return self.temp == other.to_kelvin().temp # self.temp == int, other.temp == int
        # return a boolean
    
    def __add__(self, other): # self == Kelvin, other == Kelvin
        return Kelvin(self.temp + other.temp) # self.temp == int, other.temp == int
        # returns an int -> int(50) -> Kelvin(50)
    
    def __floordiv__(self, divisor):
        return Kelvin(self.temp // divisor)
    
    def to_kelvin(self):
        return self

class Celcius:
    def __init__(self, temp):
        self.temp = temp
    
    def __eq__(self, other):
        return self.to_kelvin() == other.to_kelvin()
    
    def to_kelvin(self):
        return Kelvin(self.temp + 273)
    





    # def __add__(self, other):
    #     return Celcius(self.temp + other.temp)
    
    # def __floordiv__(self, divisor):
    #     return Celcius(self.temp // divisor)