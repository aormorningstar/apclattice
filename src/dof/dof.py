from abc import ABC, abstractmethod

class DOF(ABC):
    """Abstract degree of freedom on a site."""

    @abstractmethod
    def isvalid(self, val):
        """Is this value valid?

        :param val: Can the degree of freedom take on this value?
        :return: True if val is a valid value. False otherwise.
        """
        pass

    @abstractmethod
    def __eq__(self, oth):
        """Compare two DOFs for equivalence.

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
