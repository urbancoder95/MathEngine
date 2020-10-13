"""
An abstract definition of the various nodes that are going to be involved in the whole engine. There is a basic
Node class which consists of the basic definitions required by any node. The rest are self explanatory.

@Author: Jeet Dutta
"""
# from tools import name


class Node:
    """
    Defines a basic node inside the graph. This is the base class for all subsequent
    to-be built nodes. It defines the name
    """
    def __init__(self, name: str = None):
        if name is None:
            self.name = "Node" + str(1)
        else:
            self.name = name

    def __repr__(self):
        return "<class:{} name:\"{}\">".format("Node", self.name)

    def __str__(self):
        return "<class:{} name:\"{}\">".format("Node", self.name)


class DataNode(Node):
    """
    Defines a node to store a data. This can be a constant or a variable.
    """
    def __init__(self, value, name: str = None):
        super().__init__(name=name)
        self.value = value

    def __repr__(self):
        # name = super().__repr__()
        return "<class:{} value:{} name:\"{}\">".format("DataNode", self.value, self.name)

    def __str__(self):
        return "<class:{} value:{} name:\"{}\">".format("DataNode", self.value, self.name)


class OpNode(Node):
    """
    Defines a node to store the type of operation. This is an unbiased type operation
    which can take on any mathematical operation.
    """
    def __init__(self, op, name: str = None):
        super().__init__(name=name)
        self.op = op

    def __repr__(self):
        # name = super().__repr__()
        return "<class:{} opname:{} name:\"{}\">".format("OpNode", self.op, self.name)

    def __str__(self):
        return "<class:{} opname:{} name:\"{}\">".format("OpNode", self.op, self.name)
