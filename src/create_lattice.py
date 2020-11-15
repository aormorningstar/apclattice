# updated: 11-15-2020

import numpy as np
import unitcell

class UnitCellParam:
    def __init__(self, cell_scaling):
        self.cell_scaling = cell_scaling

class UnitCellFactory:
    def CreateUnitCell(self, UnitCellParam, Utype):
        uc = self._GetUnitCell(Utype)
        return uc(UnitCellParam)
    
    def _GetUnitCell(self, Utype):
        if format == '1d':
            return self._Create1DUnitCell
        elif format == '2ds':
            return self._Create2DSquareUnitCell
        elif format == '2dh':
            return self._Create2DHoneycomb
        else:
            raise ValueError(Utype)

    def _Create2DHoneycomb(self, UnitCellParam, UnitCell):
        s = UnitCellParam.cell_scaling
        a = s*np.array([[1.,0.5],
                        [0.,np.sqrt(3)/2.]])
        b = s*np.array([[0.5,          1.],
                        [np.sqrt(3)/6.,np.sqrt(3)/3.]])
        dim = np.size(a,1)
        sites_per_cell = np.size(b,1)
        return UnitCell(dim, a, sites_per_cell, b)

    def _Create1DUnitCell(self, UnitCellParam, UnitCell):
        s = UnitCellParam.cell_scaling
        a = s*np.array([1.])
        b = s*np.array([0.5])
        dim = np.size(a,1)
        sites_per_cell = np.size(b,1)
        return UnitCell(dim, a, sites_per_cell, b)

    def _Create2DSquareUnitCell(self, UnitCellParam, UnitCell):
        s = UnitCellParam.cell_scaling
        a = s*np.array([[1.,0.],
                        [0.,1.]])
        b = s*np.array([0.5,0.5])
        dim = np.size(a,1)
        sites_per_cell = np.size(b,1)
        return UnitCell(dim, a, sites_per_cell, b)
