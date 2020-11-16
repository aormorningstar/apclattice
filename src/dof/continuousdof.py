from .dof import DOF

class ContinuousDOF(DOF):
    """A degree of freedom that takes on values in a real interval. A concrete subclass of the abstract class DOF."""

    def __init__(self, min, max):
        """Create a degree of freedom with all reals in [min, max].

        :param min: The minimum valid value.
        :type min: float
        :param max: The maximum valid value.
        :type max: float
        """

        assert min < max, "Must have min < max."

        self.__min = min
        self.__max = max

    @property
    def min(self):
        """Min value.

        :return: Minimum valid value.
        """

        return self.__min

    @property
    def max(self):
        """Max value.

        :return: Maximum valid value.
        """

        return self.__max

    def isvalid(self, val):
        """Is this value valid?"""

        return self.min <= val and val <= self.max

    def __eq__(self, oth):
        """Compare two DOFs for equivalence."""

        return isinstance(oth, ContinuousDOF) and self.min == oth.min and self.max == oth.max
