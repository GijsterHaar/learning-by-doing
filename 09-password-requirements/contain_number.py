from re import search

class MustContainNumberRequirement:

    def check(self, password):
        return bool(search(r'[0-9]', password))
    
    def message(self):
        return 'The password must contain at least one number.'