import numpy as np
import unitcell

class Lattice(Graph):
    
    # graph_attr is placeholder for parent init method 
    def __init__(self, graph_attr, unit_cell, L, periodic = False):
        super().__init__(graph_attr)
        self.unit_cell = unit_cell
        self.L = L # size of lattice, i.e. number of unit cells
                   # along each dimension
        self.periodic = periodic

        # TODO: initailize & store coords-index relationship
        # as tuple : int dictionary, i.e.:
        # { (n_0, n_1, ..., n_dim, m) : site_index }

    # returns True if valid index for a site in Lattice
    def __contains__(self, index):
        return 0 <= index and index < self.nsites

    @property
    def dof(self):
        return self.vv

    # return coordinates (n_0, n_1, ..., n_dim, m) for site with index
    def ind_to_coords(self, index):

        # TODO

        return (0, 0)
    
    # return coordinates (n_0, n_1, ..., n_dim, m) for site with index
    def coords_to_ind(self, coords):

        # check valid site within cell
        if coords[-1] >= self.unit_cell.sites_per_cell:
            return None

        # check coords are within boundaries
        if np.count_nonzero(np.greater_equal(coords[:-1], self.L)) > 0:

            # take modulo if periodic
            if self.periodic:
                coords = np.mod(coords[:-1], self.L)
            else:
                return None

        # TODO: determine index using { (tuple) : int } dict?
        index = 0

        return index

    # for site at index, return type of site (within unit cell)
    def ind_to_type(self, index):

        # convert index to coords
        coords = self.ind_to_coords(index)

        # last coordinate is site type
        return coords[-1]

    # for setting & getting node values,
    # site can either be an index or coordinates
    def get_val(self, site):

        # convert to index if given coordinates
        if not isinstance(site, int):
            site = self.coords_to_ind(site)
        
        return Graph.get_val(self, site)
            

    def set_val(self, site, new_value):

        # convert to index if given coordinates
        if not isinstance(site, int):
            site = self.coords_to_ind(site)

        Graph.set_val(self, site, new_value)