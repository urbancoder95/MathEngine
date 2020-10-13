from .nodes import DataNode, OpNode


class BinaryOp(OpNode):
    def __init__(self, left: DataNode, right: DataNode, op: OpNode, name: str = None):
        super().__init__(op == op)
        self.left = left
        self.right = right

    def __repr__(self):
        return self.left.name + self.op.symbol + self.right.name

    def __str__(self):
        return self.__repr__()
