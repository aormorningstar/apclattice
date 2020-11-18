from src.dof import DiscreteDOF, ContinuousDOF
from unittest import TestCase

class TestDiscreteDOF(TestCase):

    def setUp(self):
        self.min = -1
        self.max = 1
        self.dof = DiscreteDOF(self.min, self.max)

    def test_discrete_dof_min_max(self):
        self.assertEquals(self.dof.min, self.min)
        self.assertEquals(self.dof.max, self.max)

    def test_discrete_dof_isvalid(self):
        self.assertTrue(self.dof.isvalid(self.max - 1))
        self.assertFalse(self.dof.isvalid(self.min - 1))
        self.assertFalse(self.dof.isvalid(self.max - 0.5))

    def test_discrete_dof_eq(self):
        oth = DiscreteDOF(self.min, self.max)
        self.assertTrue(self.dof == oth)

class TestContinuousDOF(TestCase):

    def setUp(self):
        self.min = -1
        self.max = 1
        self.dof = ContinuousDOF(self.min, self.max)

    def test_continuous_dof_min_max(self):
        self.assertEquals(self.dof.min, self.min)
        self.assertEquals(self.dof.max, self.max)

    def test_continuous_dof_isvalid(self):
        self.assertTrue(self.dof.isvalid(self.max - 0.5))
        self.assertFalse(self.dof.isvalid(self.min - 0.5))

    def test_continuous_dof_eq(self):
        oth = ContinuousDOF(self.min, self.max)
        self.assertTrue(self.dof == oth)
