import re

class MustContainCapital:
    
    def __init__(self, password):
        self.password = password
    
    def check(self):
        capital = [char for char in self.password if char.isupper()]
        return len(capital) > 0
    
    def __str__(self):
        return 'The password must contain at least one capital.'