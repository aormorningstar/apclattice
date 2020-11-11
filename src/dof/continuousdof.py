from .dof import DOF

class ContinuousDOF(DOF):
    """A degree of freedom that takes values in a real interval."""

    def __init__(self, min, max):
        """Create a degree of freedom with all reals in [min, max]."""

        assert min < max "Must have min < max."

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
        return self.__min <= val and val <= self.__max
