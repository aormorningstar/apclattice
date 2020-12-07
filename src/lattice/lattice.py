import numpy as np
import itertools as it

class Lattice:
    """A Bravais lattice in arbitrary dimensions.

    Stretches over some number of unit cells in each direction. Holds values associated to each site. Can have periodic or open boundaries.
    """

    def __init__(self, uc, L, vals, periodic=False):
        """Construct the lattice.

        :param uc: The unit cell.
        :param L: The number of unit cells in each direction of the lattice.
        :param vals: A list of values for the sites of the lattice. Must be consistent with the degrees of freedom in the unit cell. Number of values given must also be consistent with number of sites implied by L and uc.
        :param periodic: Whether to use periodic boundaries or not.
        """
        # unit cell of lattice
        self.uc = uc
        # number of unit cells in each direction
        self.L = L
        # check for consistency of spatial dimension
        assert len(L) == uc.dim, 'Inconsistent spatial dimension. Check L and uc.'
        # number of sites
        self.__nsites = np.prod(L)*uc.spc
        # value at each site
        self.vals = vals
        # check consistency
        assert len(vals) == self.nsites, 'Inconsistent number of sites.'
        # periodic boundaries
        self.__periodic = periodic
        # build data for translating between index and coords
        shape = np.append(L, uc.spc)
        inds = np.arange(self.nsites)
        self.__c_to_i = np.reshape(inds, shape)
        self.__i_to_c = list(it.product(*map(range, shape)))
        # check the two maps are inverses
        assert np.all([i == self.__c_to_i[self.__i_to_c[i]] for i in inds]), 'Conversion between ind and coords failed.'

    @property
    def periodic(self):
        """Are boundaries periodic?"""
        return self.__periodic

    @property
    def nsites(self):
        """Number of sites in the lattice."""
        return self.__nsites

    def __contains__(self, site):
        """Returns True if valid site in Lattice.

        :param site: Index or coords specifying a site.
        """
        # site is an index
        if isinstance(site, int):
            i = site
            return 0 <= i < self.nsites
        # site is a coords
        elif isinstance(site, tuple) and len(site) == len(self.L) + 1:
            c = site
            valid_type = c[-1] < self.uc.spc
            # periodic boundaries
            if self.periodic:
                return valid_type
            # open boundaries
            else:
                return np.all(np.less(c[:-1], self.L)) and valid_type
        # invalid argument
        else:
            raise ValueError('Invalid site specification.')

    def ind_to_coords(self, ind):
        """Cartesian coordinates corresponding to a linear index.

        :param ind: The linear index. Must be in [0, nsites-1].
        """
        return self.__i_to_c[ind]

    def coords_to_ind(self, coords):
        """Linear index corresponding to cartesian coords.

        :param coords: The coordinates.
        """
        # coords in the lattice
        if coords in self:
            # wrap around boundary if periodic
            if self.periodic:
                coords = tuple(np.mod(coords[:-1], self.L))
            return self.__c_to_i[coords]
        # coords not in the lattice or invalid
        else:
            return None

    def ind_to_type(self, index):
        """For site at index, return type of site (within unit cell).

        :param index: The index of the site.
        """
        # convert index to coords
        coords = self.ind_to_coords(index)
        # last coordinate is site type
        return coords[-1]

    def val(self, site, new_val=None):
        """Get or set the value at a site.

        :param site: Index or coords specifying a site.
        :param new_val: New value at that site.
        """
        # convert to index if given coordinates
        ind = site if isinstance(site, int) else self.coords_to_ind(site)
        # getter
        if new_val is None:
            return self.vals[ind]
        # setter
        else:
            type = self.ind_to_type(ind)
            if self.uc.dof[type].isvalid(new_val):
                self.vals[ind] = new_val
            else:
                raise ValueError("Can't set that site to that value.")

    def position(self, site):
        """The absolute position of the site.

        :param site: Index or coords specifying a site.
        """
        assert site in self, 'Invalid site.'
        # coords
        c = self.ind_to_coords(site) if isinstance(site, int) else site
        # position
        r = np.zeros(self.uc.dim)
        # add lattice vectors
        for i, ai in enumerate(self.uc.a):
            r += c[i]*ai
        # add basis vector
        r += self.uc.b[c[-1]]
        return r
