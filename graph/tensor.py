from .nodes import DataNode
from utils.errors import *


# from collections import UserList


class Tensor(DataNode):
    """
    Defines a tensor of an arbitrary shape.
    @param value: list or scalar.
    @param name: Assign a name to the node.
    """

    def __init__(self, value, name: str = None):

        super(Tensor, self).__init__(value, name=name)
        self.data = value
        self.name = name
        self.shape = []
        self.__shapenew__()

    def __getitem__(self, item):
        """
        Overriden __getitem__ method aiding in accessing elements in the Tensor.
        :param item: int or slice. The index of a/group of element(s).
        :return: element(s) of
        """
        if type(item) == int:
            return Tensor(self.data[item])
        elif type(item) == slice:
            return Tensor(self.data[item])
        elif type(item) == tuple:
            # print(item)
            temp = self.data
            # print(temp)
            for i in item:
                if type(i) == slice:
                    temp = temp[i]
                elif type(i) == int:
                    temp2 = []
                    for j in temp:
                        try:
                            temp2.append(j[i])
                        except TypeError:
                            raise IndexError("Too many indices for Tensor.")
                    temp = temp2
                    del temp2
                else:
                    raise TypeError("Expected integer or slices.")
                # print(temp)
            return Tensor(temp)
        else:
            raise TypeError("Expected integer or slices.")
        # return item

    def __len__(self):
        """
        Overriden __len__ method.
        :return: shape of the Tensor.
        """
        return self.shape

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
            length = len(self.data)
        except TypeError:
            length = 0
        # Now we check if value is None, which means it is empty. None itself is a scalar value.
        if self.data is None:
            return ()
        # We check weather the value is not None but still scalar of types int or float. 
        elif length == 0 and (type(self.data) == int or type(self.data) == float):
            return ()
        # Then we check for the entire shape of the value
        elif len(self.data) > 0:
            length = len(self.data)
            shape = list()
            index = 0
            next_val = self.data
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
                            type(self.data).__name__ + "\'")

    def __shapenew__(self):
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
            length = len(self.data)
            self.__findList__(self.data)
            # print("No Dimension mismatch error")
        except TypeError:
            length = 0
        # Now we check if value is None, which means it is empty. None itself is a scalar value.
        '''if self.data is None:
            return ()
        # We check weather the value is not None but still scalar of types int or float.
        elif length == 0 and (type(self.data) == int or type(self.data) == float):
            return ()
        # Then we check for the entire shape of the value
        elif len(self.value) > 0:
            length = len(self.data)
            shape = list()
            index = 0
            next_val = self.data
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
                            type(self.__data).__name__ + "\'")'''

    def __findList__(self, listVal):
        flag, tempList = self.__checkLengthOfElements__(listVal)
        if len(tempList) == 0 and tempList[0] <= 1:
            return
        if flag:
            if not self.shape.__contains__(len(tempList)):
                self.shape.append(len(tempList))
            for elem in listVal:
                self.__findList__(elem)
        else:
            raise DimensionMismatchError
            # print("Dimension mismatch of vector components {}".format(listVal))

    def __checkLengthOfElements__(self, value):
        temp = []
        for item in value:
            try:
                val = len(item)
                temp.append(val)
            except TypeError:
                temp.append(1)
        return all(i == temp[0] for i in temp), temp

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
        return "<class:{} value:{} name:\"{}\">".format("Tensor", self.data, self.name)

    def __str__(self):
        return "<class:{} value:{} name:\"{}\">".format("Tensor", self.data, self.name)
