class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise Exception("Name")
