from graph.nodes import DataNode
from ops import *
from tools import name
class Variable(DataNode):
    def __init__(self, name = None):
        if(name == None):
            self.name = name.assign_name()
        else:
            self.name = name
        super().__init__(value = self.name)
        self.value = self.name

    def __repr__(self):
        return "Variable: " + self.value
    
    def __str__(self):
        return "Variable: " + self.value

    def __add__(self, o):
        return add(self, o)
    def __sub__(self, o):
        return sub(self, o)
    def __mul__(self, o):
        return mul(self, o)
    def __truediv__(self, o):
        return div(self, o)
    def __pow__(self):
        return 