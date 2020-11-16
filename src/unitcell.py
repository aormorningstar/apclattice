class UnitCell:

    # unit cell attributes are private
    def __init__(self, dim, a, sites_per_cell, b):
        self.dim = dim
        self.a = a # array of unit vectors
        self.sites_per_cell = sites_per_cell
        self.b = b # array of site location(s) within cell

    # check equivalency of two unit cells
    def __eq__(self, other):
        return (
            self.dim == other.dim and
            self.a == other.a and
            self.sites_per_cell == other.sites_per_cell and
            self.b == other.b
        )

    # check non-equivalency
    def __ne__(self, other):
        return not self.__eq__(other)
