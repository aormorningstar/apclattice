# updated: 11-16-2020
# Honeycomb Unit Cell Class
# Input:  dof
# Output: an instance of UnitCell with all the properties filled

import numpy as np
from .unitcell import UnitCell

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
    def __init__(self, dof):
        a = [np.array([1., 0.]),
             np.array([0.5,np.sqrt(3.)/2.])]
        b = [np.array([0.5,np.sqrt(3.)/6.]),
             np.array([1., np.sqrt(3.)/3.])]
        dim = len(a)
        spc = len(b)
        super().__init__(dim, a, spc, b, dof)

# The following are the rest of the unit cell constructions we discussed, including
# a factory class that turns itself into one type depending on its input.
# We can 

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
    def __init__(self, dof):
        a = [np.array([1.,0.]),
             np.array([0.,1.])]
        b = [np.array([0.5,0.5])]
        dim = len(a)
        spc = len(b)
        super().__init__(dim, a, spc, b, dof)

# Layout of Vectors:
#
#       ____. b[0]
#       _________>
#          a[0]
# 
# where a[0] is defined to be [1,0]

class LineUnitCell(UnitCell): # 1D unit cell
    def __init__(self, dof):
        a = [np.array([1.])]
        b = [np.array([0.5])]
        dim = len(a)
        spc = len(b)
        super().__init__(dim, a, spc, b, dof)

class UnitCellFactory(UnitCell):
    def __init__(self, uctype, dof):
        if   uctype == '1d':  self = LineUnitCell(dof)
        elif uctype == '2ds': self = SquareUnitCell(dof)
        elif uctype == '2dh': self = HoneycombUnitCell(dof)
        else:                 raise ValueError(uctype)
