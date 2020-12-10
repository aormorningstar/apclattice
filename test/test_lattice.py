from src.dof import DiscreteDOF
from src.unitcell import HoneycombUnitCell
from src.lattice import Lattice
import numpy as np
from unittest import TestCase

class TestLattice(TestCase):

    def setUp(self):
        dof = DiscreteDOF(0, 1)
        uc = HoneycombUnitCell(2*[dof])
        L = [4, 4]
        vals = np.random.choice(range(dof.max), uc.spc*np.prod(L))
        self.lat = Lattice(uc, L, vals, periodic=True)

    def test_contains(self):
        self.assertTrue(np.all(
            [i in self.lat for i in range(self.lat.nsites)]
        ))
        self.assertFalse(self.lat.nsites in self.lat)
        self.assertFalse(-1 in self.lat)

    def test_ind_coords(self):
        check_inv = [
            i == self.lat.coords_to_ind(self.lat.ind_to_coords(i)) for i in range(self.lat.nsites)
        ]
        self.assertTrue(np.all(check_inv))
