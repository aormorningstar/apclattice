from src.unitcell import UnitCell, HoneycombUnitCell, SquareUnitCell, LineUnitCell
import numpy as np
from unittest import TestCase

class TestUnitCell(TestCase):

    def setUp(self):
        self.uchc = HoneycombUnitCell(1)
        self.ucsq = SquareUnitCell(1)
        self.ucln = LineUnitCell(1)

    def test_honeycomb_unit_cell(self):
        self.assertEqual(self.uchc.a, [np.array([1., 0.]),
                                       np.array([0.5, np.sqrt(3.)/2.])])
        self.assertEqual(self.uchc.b, [np.array([0.5, np.sqrt(3.)/6.]),
                                       np.array([1., np.sqrt(3.)/3.])])

    def test_square_unit_cell(self):
        self.assertEqual(self.ucsq.a, [np.array([1.,0.]),
                                       np.array([0.,1.])])
        self.assertEqual(self.ucsq.b, [np.array([0.5,0.5])])

    def test_line_unit_cell(self):
        self.assertEqual(self.ucln.a, [np.array([1.])])
        self.assertEqual(self.ucln.b, [np.array([0.5])])

