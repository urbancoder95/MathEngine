from .nodes import OpNode
from .tensor import Tensor


class BinaryOpNode(OpNode):
    """
    Base class for binary operations
    :param left: Tensor. Left operand.
    :param right: Tensor. Right operand.
    :param op: OpNode. Placeholder for operation type. Maybe deleted.
    :param name: str. Name of the operation.
    """
    def __init__(self, op: OpNode, name: str = None):
        super(BinaryOpNode, self).__init__(op=op)
        self.name = name
        self.__left = "left_operand"
        self.__right = "right_operand"

    def __call__(self, left: Tensor, right: Tensor, *args, **kwargs):
        self.__left = left
        self.__right = right
        return self.__repr__()

    def __repr__(self):
        return "<class:{} left_operand:{} right_operand:{} name:\"{}\">".format("BinaryOpNode",
                                                                                self.__left,
                                                                                self.__right,
                                                                                self.name)

    def __str__(self):
        return "<class:{} left_operand:{} right_operand:{} name:\"{}\">".format("BinaryOpNode",
                                                                                self.__left,
                                                                                self.__right,
                                                                                self.name)


class Add(BinaryOpNode):
    """
    Adds 2 tensors.
    """
    def __init__(self, name: str = None):
        super(Add, self).__init__(OpNode('add'), name)
        self.name = name

    def __call__(self, left: Tensor, right: Tensor, *args, **kwargs):
        temp = None
        if len(left.shape) == 0 and len(right.shape) == 0:
            return Tensor(left.data + right.data)
        else:
            print("Add does not support multi-dimensional lists yet.")
            # if len(left.shape) > len(right.shape):
