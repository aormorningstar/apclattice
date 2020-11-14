from .dof import DOF

class DiscreteDOF(DOF):
    """A degree of freedom that takes on contiguous integer values."""

    def __init__(self, min, max):
        """Create a degree of freedom with all integers in [min, max].

        :param min: The minimum valid value.
        :type min: int
        :param max: The maximum valid value.
        :type max: int
        """

        iimin = isinstance(min, int)
        iimax = isinstance(max, int)
        assert iimin and iimax and min < max "Must be integers with min < max."

        self.__min = min
        self.__max = max

    def min(self):
        """Min value.

        :return: Minimum valid value.
        :rtype: int
        """
        return self.__min

    def max(self):
        """Max value.

        :return: Maximum valid value.
        :rtype: int
        """
        return self.__max

    def isvalid(self, val):
        """Is this value valid?

        :param val: Can the degree of freedom take on this value?
        :return: True if val is a valid value. False otherwise.
        :rtype: bool
        """
        return isinstance(val, int) and self.__min <= val and val <= self.__max
