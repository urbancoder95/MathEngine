from graph.nodes import DataNode
class Variable(DataNode):
    def __init__(self, name = None):
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