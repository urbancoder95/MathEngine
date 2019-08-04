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
    def __init__(self, value):
        '''Defines a node to store a data. This can be a constant or a variable. 
        '''
        super().__init__(value = value)
        self.value = value

    def __repr__(self):
        #s = super().__repr__()
        return "DataNode: " + str(self.value)
    def __str__(self):
        return "DataNode: " + str(self.value)

class OpNode(Node):
    def __init__(self, left: DataNode, right: DataNode, op: str):
        '''Defines a node to store the type of operation. This is an unbiased type operation 
        which can take on any mathematical operation.
        '''
        super().__init__(op = op)
        self.op = op
    
    def __repr__(self):
        return "OpNode: " + self.op
    
    def __str__(self):
        return "OpNode: " + self.op


# class ErroneousNode(Node):
#     def __init__(self, value, op):
#         super().__init__(value = value, op = op)
#         print("Exiting as error occurred")

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


class BinaryOp(OpNode):
    def __init__(self, left: DataNode, right: DataNode, op: OpNode):
        super().__init__(op == op)
        self.left = left
        self.right = right
    
    def __repr__(self):
        return self.left.name + self.op.symbol + self.right.name

    def __str__(self):
        return self.__repr__()

class UnbiasedNodeException(Exception):
    def __init__(self, message):
        self.message = message

# if __name__ == '__main__':
#     obj = DataNode(3)
#     print(obj)
#     obj = ErroneousNode(obj.value, '+')