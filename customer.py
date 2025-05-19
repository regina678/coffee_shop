class Customer:
    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name
    
    def name(self, value):
        if isinstance(value,str) and 1 <= len(value) <=15:
            self._name = value
        else:
            raise Exception("Name must be between 1 and 15 and be a string")