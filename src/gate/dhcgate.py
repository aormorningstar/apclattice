import numpy as np
import itertools as it

from .gate import Gate
from ..unitcell import HoneycombUnitCell
from ..dof import DiscreteDOF

class DiscreteHoneycombChargeGate(Gate):
    """A gate that conserves charge and acts on a honeycomb lattice of discrete degrees of freedom.

    Allows charge-conserving transitions on a site and its three neighbors. All possible transitions happen with equal probability.
    """

    def __init__(self, uc):
        """Construct the gate."""

        assert isinstance(uc, HoneycombUnitCell), "Expected a HoneycombUnitCell."
        assert np.all([isinstance(dof, DiscreteDOF)  for dof in uc.dof]), "All degrees of freedom must be discrete."

        # the unit cell
        self.__uc = uc

        # number of sites involved in an update
        self.__n = 4

        # the change in coords to nearby sites
        self.__deltas = np.asarray([
            [ # type 0 site
                [-1, 0, 1], # down and to the left
                [0, -1, 1], # down and to the right
                [0, 0, 1], # up
            ],
            [ # type 1 site
                [1, 0, 0], # up and to the right
                [0, 1, 0], # up and to the left
                [0, 0, 0], # down
            ],
        ])

        # the types of nearby sites
        self.__types = [
            [1, 1, 1,],
            [0, 0, 0,],
        ]

        # generate all possible local states
        rs = [range(dof.min, dof.max + 1) for dof in uc.dof]
        states = list(it.product(*rs))


    @property
    def uc(self):
        """The unit cell that the gate assumes."""

        return self.__uc

    def iscompatible(self, lat):
        """Check if the gate is compatible with a lattice."""

        return self.uc == lat.uc

    def __call__(self, lat, ind):
        """Apply the gate to a lattice around a specified site."""

        # index, coords, type, val of central site
        i0 = ind
        c0 = lat.ind_to_coords(i0)
        t0 = c0[-1]
        v0 = lat.val[i0]

        # indices, coords, types, vals of sites
        c = [c0] + [c0 + d for d in self.__deltas[t0]]
        i = [i0] + [lat.coords_to_ind(_c) for _c in c]
        t = [t0] + self.__types[t0]
        v = [lat.val[_i] for _i in i]

        # excess charge
        dq = [lat.val[_i] - self.uc.dof[_t].min for _i, _t in zip(i, t)]

        # randomly distribute the excess charge
        full = self.__n * [False]
        dqtot = np.sum(dq)
        while dqtot > 0:
