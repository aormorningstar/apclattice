from abc import ABC, abstractmethod

class Gate(ABC):
    """Gates enact local dynamics on lattices."""

    @abstractmethod
    def __call__(self, lat, i):
        """Apply the gate to a lattice at a specified location.

        :param lat: Lattice to enact local dynamics on.
        :param i: Index of site of lattice around which gate is applied.
        """
        pass

    @abstractmethod
    def iscompatible(self, lat):
        """Check if the gate is compatible with a lattice.

        :param lat: The lattice with which to check compatibility.
        """
        pass
