
class MustMeetMinimumLenghtRequirement:
    
    def check(self, password):
            return len(password) >= 8
    
    def message(self):
        return 'The password must contain at least 8 characters.'