

class PassWordChecker:
    def __init__(self, requirements):
        self.requirements = requirements
    
    def check(self, password):
        self.final_message = []
        self.final_result = True
        for req in self.requirements:
            if not req.check(password):
                self.final_message.append(req.message())
                self.final_result = False

    def return_check(self):
        return self.final_result
    
    def message(self):
        return self.final_message