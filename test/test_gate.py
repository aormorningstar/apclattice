from src.dof import DiscreteDOF
from src.unitcell import HoneycombUnitCell
from src.lattice import Lattice
from src.gate import HoneycombGate
import numpy as np
from unittest import TestCase

class TestHoneycombGate(TestCase):

    def setUp(self):
        dof = DiscreteDOF(0, 1)
        uc = HoneycombUnitCell(2*[dof])
        L = [4, 4]
        vals = np.random.choice(range(dof.max), uc.spc*np.prod(L))
        self.lat = Lattice(uc, L, vals, periodic=True)
        self.gate = HoneycombGate(uc)

    def test_call(self):
        charge = np.sum(self.lat.vals)
        charge_conserved = True
        for i in range(self.lat.nsites):
            self.gate(self.lat, i)
            if np.sum(self.lat.vals) != charge:
                charge_conserved = False
        self.assertTrue(charge_conserved)
