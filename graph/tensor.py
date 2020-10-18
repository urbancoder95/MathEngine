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
<<<<<<< Updated upstream
            length = len(self.value)
        except TypeError:
            length = 0
        # Now we check if value is None, which means it is empty. None itself is a scalar value.
        if self.value is None:
=======
            length = len(self.__data)
            self.__findList__(self.__data)
            print("No Dimension mismatch error")
        except TypeError:
            length = 0
        '''# Now we check if value is None, which means it is empty. None itself is a scalar value.
        if self.__data is None:
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                            type(self.value).__name__ + "\'")

=======
                            type(self.__data).__name__ + "\'")'''
            
    def __findList__(self, listVal):
        print(listVal)
        flag, tempList = self.__checkLengthOfElements__(listVal)
        if(len(tempList) == 1 and tempList[0] <= 1):
            return 
        if(flag):
            for elem in listVal: 
                self.__findList__(elem)
                return 
        else:
            raise Exception("Dimension mismatch of vector components" + listVal)
                
    def __checkLengthOfElements__(value):
        temp = []
        for item in value:
            try:
                val = len(item)
                temp.append(val)
            except:
                temp.append(1)
        print(temp)
        return all(i == item[0] for i in temp), temp
            
    
>>>>>>> Stashed changes
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
