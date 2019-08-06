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


# class ErroneousNode(Node):
#     def __init__(self, value, op):
#         super().__init__(value = value, op = op)
#         print("Exiting as error occurred")

# Define some types of data nodes

class Tensor(DataNode, list):
    def __init__(self, value, name: str = None):
        '''
        Defines a tensor of an arbitrary shape. 
        @param value: list or scalar.
        @param name: Assign a name to the node.
        '''
        self.value = value
        self.shape = self.__shape__()

    def __shape__(self):
        try:
            length = len(self.value)
        except TypeError:
            length = 0
        if(self.value == None):
            return ()
        elif(length == 0 and (type(self.value) == int or type(self.value) == float)):
            return ()
        elif(len(self.value) > 0):
            check_len = 0
            while(check_len > 0):
                pass #START FROM HERE
    def __check_len__(iter):
        try:
            length = len(iter[0])
        except TypeError:
            length = 0
        for i in iter[1:]:
            try:
                length2 = len(i)
            except TypeError:
                length2 = 0
            if(not(length2 == length)):
                raise LengthError('Multiple dimensions detected.')
            elif(length2 == 0):
                return 0
            else:
                pass
        return length
    def __repr__(self):
        return 

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


class BinaryOp(OpNode):
    def __init__(self, left: DataNode, right: DataNode, op: OpNode, name: str = None):
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