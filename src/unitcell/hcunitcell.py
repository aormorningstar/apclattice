# updated: 11-16-2020

import numpy as np
from .unitcell import UnitCell

# HELP NEEDED

class HoneycombUnitCell:
    def __init__(self,uc):      # Is there a way for me to just return a UnitCell object with out passing it in first?
        self.__a = [np.array([1.,0.]),np.array([0.5,np.sqrt(3.)/2.])]
        self.__b = [np.array([0.5,np.sqrt(3.)/6.]), np.array([1.,np.sqrt(3.)/3.])]
        self.__dim = len(self.__a)
        self.__spc = len(self.__b)
        self.__uc = uc(self.__dim, self.__a, self.__spc, self.__b) # Not sure how to create a UnitCell object in this class

    def create(self):           # I'm not sure hot to initialize and directly return an object
        return self.__uc

'''
class UnitCellFactory:
    def CreateUnitCell(self, Utype):
        uc = self._GetUnitCell(Utype)
        return uc()
    
    def _GetUnitCell(self, Utype):
        if format == '1d':
            return self._Create1DUnitCell
        elif format == '2ds':
            return self._Create2DSquareUnitCell
        elif format == '2dh':
            return self._Create2DHoneycomb
        else:
            raise ValueError(Utype)

    def _Create2DHoneycomb(self, UnitCell):
        s = UnitCellParam.cell_scaling
        a = s*[np.array([1.,0.]),np.array([0.5,np.sqrt(3.)/2.])]
        b = s*[np.array([0.5,np.sqrt(3.)/6.]), np.array([1.,np.sqrt(3.)/3.])]
        dim = len(a)
        sites_per_cell = len(b)
        return UnitCell(dim, a, sites_per_cell, b)

    def _Create1DUnitCell(self, UnitCell):
        s = UnitCellParam.cell_scaling
        a = s*[np.array([1.])]
        b = s*[np.array([0.5])]
        dim = len(a)
        sites_per_cell = len(b)
        return UnitCell(dim, a, sites_per_cell, b)

    def _Create2DSquareUnitCell(self, UnitCell):
        s = UnitCellParam.cell_scaling
        a = s*[np.array([1.,0.]),np.array([0.,1.])]
        b = s*[np.array([0.5,0.5])]
        dim = len(a)
        sites_per_cell = len(b)
        return UnitCell(dim, a, sites_per_cell, b)
'''