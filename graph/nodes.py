'''
An abstract definition of the various nodes that are going to be involved in the whole engine. There is a basic 
Node class which consists of the basic definitions required by any node. The rest are self explanatory.

@Author: Jeet Dutta
'''
from tools import name

class Node():
    def __init__(self, name: str = None):
        '''
        Defines a basic node inside the graph. This is the base class for all subsequent 
        to-be built nodes. It defines the name
        '''
        if(name == None):
            self.name = "Node" + str(1)
        else:
            self.name = name
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.__repr__()

class DataNode(Node):
    def __init__(self, value, name: str = None):
        '''Defines a node to store a data. This can be a constant or a variable. 
        '''
        super().__init__(name = name)
        self.value = value

    def __repr__(self):
        name = super().__repr__()
        return name + ": " + str(self.value)
    def __str__(self):
        return self.__repr__()

class OpNode(Node):
    def __init__(self, op: str, name: str = None):
        '''Defines a node to store the type of operation. This is an unbiased type operation 
        which can take on any mathematical operation.
        '''
        super().__init__(name = name)
        self.op = op
    
    def __repr__(self):
        name = super().__repr__()
        return name + ": " + self.op
    
    def __str__(self):
        return self.__repr__()