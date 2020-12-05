import numpy as np

class UnitCell:
    """A unit cell class."""

    def __init__(self, a, b, dof):
        """Initialize the unit cell.

        :param a: List of lattice vectors (numpy arrays).
        :param b: List of basis vectors (numpy arrays).
        :param dof: List of degrees of freedom (DOFs).
        """
        self.__a = a # lattice vectors
        self.__b = b # basis vectors
        self.__dof = dof # degrees of freedom
        self.__dim = len(a) # spatial dimensions
        self.__spc = len(b) # sites per unit cell
        # check for consistency
        a_dims = np.asarray(list(map(len, a)))
        b_dims = np.asarray(list(map(len, b)))
        dim_check = np.all(a_dims == self.dim) and np.all(b_dims == self.dim)
        assert dim_check, "error: inconsistent dimension"
        assert len(b) == len(dof), "error: must specify one degree of freedom per site"

    # getter methods
    @property
    def a(self):
        """List of attice vectors."""
        return self.__a

    @property
    def dim(self):
        """Spatial dimension."""
        return self.__dim

    @property
    def b(self):
        """List of basis vectors."""
        return self.__b

    @property
    def spc(self):
        """Number of sites in the unit cell."""
        return self.__spc

    @property
    def dof(self):
        """List of degrees of freedom (one per site)."""
        return self.__dof

    def __eq__(self, other):
        """Check equivalency of two unit cells."""
        dim_check = self.dim == other.dim
        spc_check = self.spc == other.spc
        # lattice vectors
        a_check = True
        for a1, a2 in zip(self.a, other.a):
            a_check *= np.all(a1 == a2)
        # basis vectors
        b_check = True
        for b1, b2 in zip(self.b, other.b):
            b_check *= np.all(b1 == b2)
        # degrees of freedom
        dof_check = True
        for dof1, dof2 in zip(self.dof, other.dof):
            dof_check *= dof1 == dof2
        return dim_check and spc_check and a_check and b_check and dof_check

    def __ne__(self, other):
        """Check non-equivalency."""
        return not self == other
