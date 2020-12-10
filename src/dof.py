"""Degrees of freedom of lattice sites.

Contains various degrees of freedom. Currently implemented are degrees of
freedom that take on
    - integer values in a finite contiguous interval
    - real values in a finite contiguous interval.
"""

from abc import ABC, abstractmethod
import numpy.random as rd

class DOF(ABC):
    """Abstract degree of freedom on a site.

    Meant to be subclassed by concrete degrees of freedom.
    """

    @abstractmethod
    def isvalid(self, val):
        """Is this value valid?

        :param val: Can the degree of freedom take on this value?
        :return: True if val is a valid value. False otherwise.
        """
        pass

    @abstractmethod
    def __eq__(self, oth):
        """Compare two degrees of freedom for equivalence.

        :param oth: The other degree of freedom to compare to.
        :return: True if degrees of freedom are equivalent.
        """
        pass

    @abstractmethod
    def rand(self, size=None):
        """Sample random valid value(s).

        :param size: Number of samples. If None then return scalar not an array.
        :return: Scalar or array of samples.
        """
        pass

class DiscreteDOF(DOF):
    """A discrete degree of freedom.

    Takes on contiguous integer values. A concrete subclass of the abstract
    class :class:`DOF`.
    """

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
        """Minimum valid value."""
        return self.__min

    @property
    def max(self):
        """Maximum valid value."""
        return self.__max

    def isvalid(self, val):
        """Checks if the argument is a valid value."""
        return isinstance(val, int) and self.min <= val and val <= self.max

    def __eq__(self, oth):
        """Compare two degrees of freedom for equivalence."""
        return isinstance(oth, DiscreteDOF) and self.min == oth.min and self.max == oth.max

    def rand(self, size=None):
        """Sample random valid value(s)."""
        return rd.choice(range(self.min, self.max+1), size=size)

class ContinuousDOF(DOF):
    """A continuous degree of freedom.

    Takes on values in a real interval. A concrete subclass of the abstract
    class :class:`DOF`.
    """

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
        """Minimum valid value."""
        return self.__min

    @property
    def max(self):
        """Maximum valid value."""
        return self.__max

    def isvalid(self, val):
        """Checks if the argument is a valid value."""
        return self.min <= val and val <= self.max

    def __eq__(self, oth):
        """Compare two degrees of freedom for equivalence."""
        return isinstance(oth, ContinuousDOF) and self.min == oth.min and self.max == oth.max

    def rand(self, size=None):
        """Sample random valid value(s)."""
        return rd.uniform(self.min, self.max, size=size)
