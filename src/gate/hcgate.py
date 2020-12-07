import numpy as np
import itertools as it
from .gate import Gate
from ..unitcell import HoneycombUnitCell
from ..dof import DiscreteDOF

class HoneycombGate(Gate):
    """A gate that conserves charge and acts on a honeycomb lattice of discrete degrees of freedom.

    Allows charge-conserving transitions on a site and its three neighbors. All possible transitions happen with equal probability. The gate can only act on lattices with a unit cell that matches the one used to construct the gate.
    """

    def __init__(self, uc):
        """Construct the gate.

        :param uc: A honeycomb unit cell with discrete degrees of freedom.
        """
        assert isinstance(uc, HoneycombUnitCell), "Expected a HoneycombUnitCell."
        assert np.all([isinstance(dof, DiscreteDOF)  for dof in uc.dof]), "All degrees of freedom must be discrete."
        # the unit cell
        self.__uc = uc
        # the change in coords to get to nearby sites (two cases)
        self.__deltas = np.asarray([
            [ # case 0: central site is a type 0 site
                [0, 0, 0],
                [-1, 0, 1],
                [0, -1, 1],
                [0, 0, 1],
            ],
            [ # case 1: central site is a type 1 site
                [0, 0, 0],
                [1, 0, -1],
                [0, 1, -1],
                [0, 0, -1],
            ],
        ])
        # the types of nearby sites (two cases)
        self.__types = [
            [0, 1, 1, 1,], # case 0
            [1, 0, 0, 0,], # case 1
        ]
        # collect all possible local states and organize by total charge
        self.__secs = [
            {}, # case 0
            {}, # case 1
        ]
        # loop over cases
        for case, types in enumerate(self.__types):
            # valid values of the included sites
            vals = [range(uc.dof[t].min, uc.dof[t].max + 1) for t in types]
            # all valid states
            states = np.asarray(list(it.product(*vals)))
            # total charge of states
            totalcharges = states.sum(axis=1)
            # the unique values of total charge
            utotalcharges = np.unique(totalcharges)
            # collect states with common total charge
            for utc in utotalcharges:
                self.__secs[case][utc] = states[totalcharges == utc, :]

    @property
    def uc(self):
        """The unit cell that the gate assumes."""
        return self.__uc

    def iscompatible(self, lat):
        """Check if the gate is compatible with a lattice."""
        return self.uc == lat.uc

    def __randstate(self, case, charge):
        """Randomly choose a state with the same charge.

        :param case: The case 0 or 1 specifies whether the central site is type 0 or 1
        :param charge: Total charge of the sites involved.
        """
        states = self.__secs[case][charge]
        return states[np.random.choice(len(states)), :]

    def __call__(self, lat, i):
        """Apply the gate to a lattice around a specified site."""
        # the coords of the central site
        coords = np.asarray(lat.ind_to_coords(i))
        # what case are we dealing with?
        case = coords[-1]
        deltas = self.__deltas[case]
        # indices of all sites involved
        inds = np.asarray([lat.coords_to_ind(tuple(coords + delta)) for delta in deltas])
        # total charge of local state
        totalcharge = np.sum(lat.vals[inds])
        # randomly transition to a state with the same charge
        lat.vals[inds] = self.__randstate(case, totalcharge)
