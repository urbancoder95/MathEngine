from variable import Variable
from graph.nodes import OpNode
class add(OpNode):
    def __init__(self, left, right, op):
        super().__init__(op == op)
        self.op = op
        self.left = left
        self.right = right
    