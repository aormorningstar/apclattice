class UnitCell:

    # unit cell attributes are private
    def __init__(self, dim, a, spc, b, dof):

        # check for internal compatibility
        assert len(a[0]) == dim, "dimension error: does not match a"
        assert len(b) == spc, "sites per cell error: does not match b"

        self.__a = a # list of unit vectors
        self.__dim = dim
        self.__b = b # array of site location(s) within cell
        self.__spc = spc # sites per unit cell
        self.__dof = dof # list of DOF objects, one per site

    # getter methods
    @property
    def a(self):
        return self.__a

    @property
    def dim(self):
        return self.__dim

    @property
    def b(self):
        return self.__b

    @property
    def spc(self):
        return self.__spc

    @property
    def dof(self):
        return self.__dof

    # check equivalency of two unit cells
    def __eq__(self, other):
        return (
            self.dim == other.dim and
            self.a == other.a and
            self.spc == other.spc and
            self.b == other.b and
            self.dof == other.dof
        )

    # check non-equivalency
    def __ne__(self, other):
        return not self.__eq__(other)
