from .dof import DOF

class ContinuousDOF(DOF):
    """A degree of freedom that takes on values in a real interval."""

    def __init__(self, min, max):
        """Create a degree of freedom with all reals in [min, max].

        :param min: The minimum valid value.
        :type min: float
        :param max: The maximum valid value.
        :type max: float
        """

        assert min < max "Must have min < max."

        self.__min = min
        self.__max = max

    def min(self):
        """Min value.

        :return: Minimum valid value.
        :rtype: float
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
        return self.__min <= val and val <= self.__max
