from .nodes import DataNode
from utils.errors import LengthError

class Tensor(DataNode, list):
    """
    Defines a tensor of an arbitrary shape.
    @param value: list or scalar.
    @param name: Assign a name to the node.
    """
    def __init__(self, value, name: str = None):

        super(DataNode, Tensor).__init__()
        self.value = value
        self.shape = self.__shape__()

    def __shape__(self):
        """
        METHOD DOC PENDING.

        Scalar values will have the shape of ().
        Vector values will have shapes of (n,).
        Matrices will have shapes of (m, n)
        . . .
        .
        .
        """
        # Initially check for scalar values. 
        # To do this we check the length of the whole value. 
        # If it throws a TypeError 
        # (which is because it is not a list), then it's a list.
        try:
            length = len(self.value)
        except TypeError:
            length = 0
        # Now we check if value is None, which means it is empty. None itself is a scalar value.
        if self.value is None:
            return ()
        # We check weather the value is not None but still scalar of types int or float. 
        elif length == 0 and (type(self.value) == int or type(self.value) == float):
            return ()
        # Then we check for the entire shape of the value
        elif len(self.value) > 0:
            length = len(self.value)
            shape = list()
            index = 0
            next_val = self.value
            while length > 0:
                # Keep on adding values to the shape
                # attribute until a scalar is encountered
                shape.append(length)
                length = self.__check_len__(next_val)
                next_val = next_val[index]
            return tuple(shape)
        else:
            raise TypeError("Can only work with values of type " +
                            "\'int\' or \'float\' not \'" +
                            type(self.value).__name__ + "\'")

    def __check_len__(self, next_val):
        # Checks the length of the inner elements of next_val. 
        # NEEDS IMPROVEMENT AS IT DOES NOT NEST FOR ALL THE INNER VALUES
        # TILL NOW JUST THE FIRST ELEMENT OF EVERY NESTED INNER TENSOR.
        try:
            length = len(next_val[0])
        except TypeError:
            length = 0
        try:
            for i in next_val[1:]:
                try:
                    length2 = len(i)
                except TypeError:
                    length2 = 0
                if not (length2 == length):
                    raise LengthError(length, length2)
        except TypeError:
            return ()
        return length

    def __repr__(self):
        return
