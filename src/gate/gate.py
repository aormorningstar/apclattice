from abc import ABC, abstractmethod

class Gate(ABC):
    """Gates enact local dynamics on lattices."""

    @abstractmethod
    def __call__(self, lat, i):
        """Apply the gate to a lattice near a specified site.

        Parameters:
            lat (Lattice): Lattice to enact local dynamics on.
            i (int): Index of site of lattice around which gate is applied.
        """
        pass
