from re import search

class MustContainSpecialCharacterRequirement:
    
    def check(self, password):
        return bool(search(r"[^\w\s]", password))
    
    def message(self):
        return 'The password must contain at least one special character.'