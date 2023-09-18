from re import search

class MustContainCapitalRequirement:
    
    def check(self, password):
        return bool(search(r'[A-Z]', password))
    
    def message(self):
        return 'The password must contain at least one capital.'