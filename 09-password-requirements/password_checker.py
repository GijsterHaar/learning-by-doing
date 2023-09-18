

class PassWordChecker:
    def __init__(self, requirements):
        self.requirements = requirements
    
    def check(self, password):
        self.final_message = []
        final_result = True
        for req in self.requirements:
            if not req.check(password):
                self.final_message.append(req.message())
                final_result = False
        return final_result
    
    def message(self):
        return self.final_message