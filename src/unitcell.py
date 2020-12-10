"""Unit cells which make up the translated tile of a regular lattice.

Various unit cells are implemented
    - 2D honeycomb lattice cell
    - 2D square lattice cell
    - 1D square lattice cell.
"""

import numpy as np

class UnitCell:
    """A unit cell of a lattice."""

    def __init__(self, a, b, dof):
        """Initialize the unit cell.

        :param a: List of lattice vectors (numpy arrays).
        :param b: List of basis vectors (numpy arrays).
        :param dof: List of degrees of freedom (:class:`DOF`).
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
        assert dim_check, "Inconsistent dimension."
        dof_check = len(b) == len(dof)
        assert dof_check, "Must specify one degree of freedom per site."

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
            a_check = a_check and np.all(a1 == a2)
        # basis vectors
        b_check = True
        for b1, b2 in zip(self.b, other.b):
            b_check = b_check and np.all(b1 == b2)
        # degrees of freedom
        dof_check = True
        for dof1, dof2 in zip(self.dof, other.dof):
            dof_check = dof_check and dof1 == dof2
        return dim_check and spc_check and a_check and b_check and dof_check

    def __ne__(self, other):
        """Check non-equivalency."""
        return not self == other

# Layout of Vectors:
#
#        ________
#       ^    . b[1]
# a[1] /  . b[0]
#     /_______>
#       a[0]
#
# where a[0] is defined to be [1,0]

class HoneycombUnitCell(UnitCell):
    """The unit cell of a honeycomb lattice in two dimensions."""

    def __init__(self, dof):
        """Initialize the honeycomb lattice.

        :param dof: List of two degrees of freedom (:class:`DOF`). One for each
            site of the honeycomb unit cell.
        """
        a = [np.array([1., 0.]),
             np.array([0.5, np.sqrt(3.)/2.])]
        b = [np.array([0.5, np.sqrt(3.)/6.]),
             np.array([1., np.sqrt(3.)/3.])]
        super().__init__(a, b, dof)

# Layout of Vectors:
#
#        _______
#       ^       |
#  a[1] |   . b[0]
#       |_______>
#       a[0]
#
# where a[0] is defined to be [1,0]

class SquareUnitCell(UnitCell):
    """The unit cell of a square lattice in two dimensions."""

    def __init__(self, dof):
        """Initialize a square 2D lattice.

        :param dof: List of one degree of freedom (:class:`DOF`).
        """
        a = [np.array([1.,0.]),
             np.array([0.,1.])]
        b = [np.array([0.5,0.5])]
        super().__init__(a, b, dof)

# Layout of Vectors:
#
#       ____. b[0]
#       _________>
#          a[0]
#
# where a[0] is defined to be [1,0]

class LineUnitCell(UnitCell):
    """The unit cell of a square lattice in one dimension."""

    def __init__(self, dof):
        """Initialize a square 1D lattice.

        :param dof: List of one degree of freedom (:class:`DOF`).
        """
        a = [np.array([1.])]
        b = [np.array([0.5])]
        super().__init__(a, b, dof)
