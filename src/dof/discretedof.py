from .dof import DOF

class DiscreteDOF(DOF):
    """A degree of freedom that takes contiguous integer values."""

    def __init__(self, min, max):
        """Create a degree of freedom with all integers in [min, max]."""

        iimin = isinstance(min, int)
        iimax = isinstance(max, int)
        assert iimin and iimax and min < max "Must be integers with min < max."

        self.__min = min
        self.__max = max

    def min(self):
        """Min value."""
        return self.__min

    def max(self):
        """Max value."""
        return self.__max

    def isvalid(self, val):
        """Is this value valid?"""
        return isinstance(val, int) and self.__min <= val and val <= self.__max
