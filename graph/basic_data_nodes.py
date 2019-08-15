
from nodes import DataNode, OpNode
class Constant(DataNode):
    def __init__(self, value, name: str = None):
        self.value = value
        self.name = name
        super().__init__(value = value, name = name)
    
    def __repr__(self):
        return self.value
    def __str__(self):
        return self.name + ": " + str(self.value)
class Variable(DataNode):
    def __init__(self, name: str = None):
        if(name == None):
            self.name = 'x'
        else:
            self.name = name
        super().__init__(value = self.name)
        self.value = self.name

    def __repr__(self):
        return "Variable: " + self.value
    
    def __str__(self):
        return "Variable: " + self.value