class LengthError(Exception):
    """
    This is called when there is a length error.
    """
    def __init__(self, length1, length2):
        message = "LENGTH MISMATCHED.\nCertain values are of length " + str(length1) + " and " + str(length2) + ".\n"
        super.message = message


class DimensionMismatchError(Exception):
    """
    This is called when there is dimension mismatch in the defined tensor.
    """
    def __init__(self):
        self.message = "DIMENSION MISMATCHED.\nCertain values do not conform to the required shape " + ".\n"
        super().__init__(self.message)
