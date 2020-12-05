from .dof import DOF
import numpy.random as rd

class DiscreteDOF(DOF):
    """A degree of freedom that takes on contiguous integer values. A concrete subclass of the abstract class DOF."""

    def __init__(self, min, max):
        """Create a degree of freedom with all integers in [min, max].

        :param min: The minimum valid value.
        :type min: int
        :param max: The maximum valid value.
        :type max: int
        """
        iimin = isinstance(min, int)
        iimax = isinstance(max, int)
        assert iimin and iimax and min < max, "Must be integers with min < max."
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
        return isinstance(val, int) and self.min <= val and val <= self.max

    def __eq__(self, oth):
        """Compare two DOFs for equivalence."""
        return isinstance(oth, DiscreteDOF) and self.min == oth.min and self.max == oth.max

    def rand(self, size=None):
        """Sample random valid value(s)."""
        return rd.choice(range(self.min, self.max+1), size=size)
