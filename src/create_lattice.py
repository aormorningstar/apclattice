import numpy as np

class LatticeParam:
    def __init__(self, dof, sites_per_cell, n_cell, site_period):
        self.dof = dof
        self.sites_per_cell = sites_per_cell
        self.n_cell = n_cell
        self.site_period = site_period


class LatticeFactory:
    def CreateLattice(self, LatticeParam, ltype):
        Lattice = self._GetLattice(ltype)
        return Lattice(LatticeParam)
    
    def _GetLattice(self, ltype):
        if format == '1d':
            return self._Create1DLattice
        elif format == '2ds':
            return self._Create2DSquareLattice
        elif format == '2dh':
            return self._Create2DHoneycomb
        else:
            raise ValueError(ltype)

    def _Create1DLattice(self,LatticeParam):
        gra = Graph()
        gra.nsites = LatticeParam.sites_per_cell*LatticeParam.n_cell
        ones = np.ones(gra.nsites)
        eye = np.identity(gra.nsites)
        gra.adj = np.roll(eye,1,axis=1)+np.roll(eye,-1,axis=1)
        gra.val = ones #could be another class
        gra.dof = LatticeParam.dof

        lat = gra.Lattice()

        uc = lat.UnitCell
        lat.uc.dim = 1
        max_size = (uc.dim-1)*LatticeParam.site_period
        uc.a = np.linspace(0,max_size,LatticeParam.sites_per_cell)
        uc.b = np.arange(LatticeParam.sites_per_cell)
        #lat.L = 
        return gra

# below not ready yet

    def _Create2DSquareLattice(self,LatticeParam):
        gra = Graph()
        gra.nsites = LatticeParam.sites_per_cell*LatticeParam.n_cell
        ones = np.ones(gra.nsites)
        eye = np.identity(gra.nsites)
        gra.adj = np.roll(eye,1,axis=1)+np.roll(eye,-1,axis=1)
        gra.val = ones #could be another class
        gra.dof = LatticeParam.dof

        lat = gra.Lattice()

        uc = lat.UnitCell
        lat.uc.dim = 2
        max_size = (uc.dim-1)*LatticeParam.site_period
        uc.a = np.linspace(0,max_size,LatticeParam.sites_per_cell)
        uc.b = np.arange(LatticeParam.sites_per_cell)
        #lat.L = 
        return gra


    def _Create2DHoneycomb(self,LatticeParam):
        gra = Graph()
        gra.nsites = LatticeParam.sites_per_cell*LatticeParam.n_cell
        ones = np.ones(gra.nsites)
        eye = np.identity(gra.nsites)
        gra.adj = np.roll(eye,1,axis=1)+np.roll(eye,-1,axis=1)
        gra.val = ones #could be another class
        gra.dof = LatticeParam.dof

        lat = gra.Lattice()

        uc = lat.UnitCell
        lat.uc.dim = 2
        max_size = (uc.dim-1)*LatticeParam.site_period
        uc.a = np.linspace(0,max_size,LatticeParam.sites_per_cell)
        uc.b = np.arange(LatticeParam.sites_per_cell)
        #lat.L = 
        return gra
