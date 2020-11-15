import numpy as np
from .gate import Gate

class HoneycombGate(Gate):
    """A gate that conserves charge and acts on a honeycomb lattice.

    Allows charge-conserving transitions on a site and its neighbors. All possible transitions happen with equal probability.
    """

    def __init__(self, lat):
        """Construct the gate."""
        pass

    def iscompatible(self, lat):
        """Check if the gate is compatible with a lattice."""
        pass

    def __call__(self, gr, i):
        """Apply the gate to a lattice at a specified location."""

        # BELOW WAS COPIED FROM ANOTHER GATE, NEEDS TO BE REDONE

        assert self.uc == lat.uc, "Unit cells must match."

        # difference in coords to other site
        dc = np.asarray([1, 0])

        # coords and values of sites
        c0 = lat.ind_to_coords(i)
        c1 = c0 + dc
        q0 = lat.get_val(c0)
        q1 = lat.get_val(c1)

        # split the total charge between the sites randomly
        qtot = q0 + q1
        qmin, qmax = self.dof.min(), self.dof.max()
        q0min = max(qmin, qtot - qmax)
        q0max = min(qmax, qtot - qmin)
        newq0 = np.random.randint(q0min, q0max+1)
        newq1 = qtot - newq0

        # set the new values
        lat.set_val(c0, newq0)
        lat.set_val(c1, newq1)
