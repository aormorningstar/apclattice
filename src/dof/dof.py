from abc import ABC, abstractmethod

class DOF(ABC):
    """Degree of freedom on a site."""

    @property
    @abstractmethod
    def min(self):
        """Minimum allowed value."""
        pass

    @property
    @abstractmethod
    def max(self):
        """Maximum allowed value."""
        pass

    @abstractmethod
    def isvalid(self, val):
        """Is this a valid value?"""
        pass
