from src.unitcell import UnitCell, HoneycombUnitCell, SquareUnitCell, LineUnitCell
import numpy as np
from unittest import TestCase

class TestUnitCell(TestCase):

    def setUp(self):
        self.uchc = HoneycombUnitCell((0,2))
        self.ucsq = SquareUnitCell((2,))
        self.ucln = LineUnitCell((2,))

    def test_honeycomb_unit_cell(self):
        self.assertTrue(np.array_equal(self.uchc.a, [np.array([1., 0.]),
                                                     np.array([0.5, np.sqrt(3.)/2.])]))
        self.assertTrue(np.array_equal(self.uchc.b, [np.array([0.5, np.sqrt(3.)/6.]),
                                                      np.array([1., np.sqrt(3.)/3.])]))

    def test_square_unit_cell(self):
        self.assertTrue(np.array_equal(self.ucsq.a, [np.array([1.,0.]),
                                                      np.array([0.,1.])]))
        self.assertTrue(np.array_equal(self.ucsq.b, [np.array([0.5,0.5])]))

    def test_line_unit_cell(self):
        self.assertTrue(np.array_equal(self.ucln.a, [np.array([1.])]))
        self.assertTrue(np.array_equal(self.ucln.b, [np.array([0.5])]))

