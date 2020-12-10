from src.unitcell import UnitCell, HoneycombUnitCell, SquareUnitCell, LineUnitCell
from src.dof import DiscreteDOF
import numpy as np
from unittest import TestCase

# cosine of angle between vectors
def cosangle(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

class TestHoneycombUnitCell(TestCase):

    def setUp(self):
        dof = [DiscreteDOF(0, 1), DiscreteDOF(0, 1)]
        self.uc = HoneycombUnitCell(dof)

    def test_honeycomb_unit_cell(self):
        self.assertAlmostEqual(0.5, cosangle(*self.uc.a))
        self.assertAlmostEqual(1.0, cosangle(*self.uc.b))
        self.assertAlmostEqual(
            cosangle(self.uc.a[0], self.uc.b[0]),
            cosangle(self.uc.a[1], self.uc.b[1])
        )
        self.assertEqual(2, self.uc.spc)
        self.assertEqual(2, self.uc.dim)
        self.assertTrue(self.uc == self.uc)

class TestSquareUnitCell(TestCase):

    def setUp(self):
        dof = [DiscreteDOF(0, 1)]
        self.uc = SquareUnitCell(dof)

    def test_square_unit_cell(self):
        self.assertAlmostEqual(0.0, cosangle(*self.uc.a))
        self.assertEqual(1, self.uc.spc)
        self.assertEqual(2, self.uc.dim)
        self.assertTrue(self.uc == self.uc)

class TestLineUnitCell(TestCase):

    def setUp(self):
        dof = [DiscreteDOF(0, 1)]
        self.uc = LineUnitCell(dof)

    def test_line_unit_cell(self):
        self.assertAlmostEqual(1.0, cosangle(self.uc.a[0], self.uc.b[0]))
