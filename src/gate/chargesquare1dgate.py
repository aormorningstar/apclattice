import numpy as np
from .gate import Gate

class ChargeSquare1DGate(Gate):
    """A gate that conserves charge and acts on a 1D square lattice.

    Allows charge-conserving transitions on two contiguous sites to happen. All possible transitions happen with equal probability. Assumes a discrete degree of freedom.
    """

    def __init__(self, uc, dof):
        """Construct the gate.

        Parameters:
            uc (UnitCell): Unit cell indicating lattices this gate can act on.
            dof (DOF): Degree of freedom of the sites.

        Returns:
            ChargeSquare1DGate: The new gate.
        """

        # unit cell and degree of freedom
        self.uc = uc
        self.dof = dof

    def __call__(self, lat, i):
        """See abstract Gate."""

        # TODO: More efficient way of checking these. Maybe store ID of lattice that has already been verified?
        assert self.uc == lat.uc "Unit cells must match."
        assert self.dof == lat.dof "Degree of freedom must match."

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
