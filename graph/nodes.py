class Node():
    def __init__(self, value = None, op = None):
        '''
        Defines a basic node inside the graph. This is the base class for all subsequent 
        to-be built nodes.
        '''
        if(not value == None and not op == None):
            raise UnbiasedNodeException("A node cannot be both data and operational type.")
        self.value = value
        self.op = op
    def __repr__(self):
        if(self.value):
            return str(self.value)
        else:
            return str(self.op)
    def __str__(self):
        if(self.value):
            return str(self.value)
        else:
            return str(self.op)

class DataNode(Node):
    def __init__(self, value):
        '''Defines a node to store a data. This can be a constant or a variable. 
        '''
        super().__init__(value = value)
        self.value = value

    def __repr__(self):
        return "DataNode: " + str(self.value)
    def __str__(self):
        return "DataNode: " + str(self.value)

class OpNode(Node):
    def __init__(self, left, right, op):
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

class UnbiasedNodeException(Exception):
    def __init__(self, message):
        self.message = message

# if __name__ == '__main__':
#     obj = DataNode(3)
#     print(obj)
#     obj = ErroneousNode(obj.value, '+')