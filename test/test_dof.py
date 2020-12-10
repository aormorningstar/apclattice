from src.dof import DiscreteDOF, ContinuousDOF
from unittest import TestCase
import numpy as np

class TestDiscreteDOF(TestCase):

    def setUp(self):
        self.min = 0
        self.max = 2
        self.dof = DiscreteDOF(self.min, self.max)

    def test_discrete_dof_min_max(self):
        self.assertEqual(self.dof.min, self.min)
        self.assertEqual(self.dof.max, self.max)

    def test_discrete_dof_isvalid(self):
        self.assertTrue(self.dof.isvalid(self.max - 1))
        self.assertFalse(self.dof.isvalid(self.min - 1))
        self.assertFalse(self.dof.isvalid(self.max - 0.5))

    def test_discrete_dof_eq(self):
        oth = DiscreteDOF(self.min, self.max)
        self.assertTrue(self.dof == oth)

    def test_discrete_dof_rand(self):
        self.assertTrue(self.min <= self.dof.rand() <= self.max)
        nrand = 10
        samples = self.dof.rand(nrand)
        self.assertTrue(
            np.all(samples <= self.max) and np.all(self.min <= samples)
        )

class TestContinuousDOF(TestCase):

    def setUp(self):
        self.min = 0
        self.max = 2
        self.dof = ContinuousDOF(self.min, self.max)

    def test_continuous_dof_min_max(self):
        self.assertEqual(self.dof.min, self.min)
        self.assertEqual(self.dof.max, self.max)

    def test_continuous_dof_isvalid(self):
        self.assertTrue(self.dof.isvalid(self.max - 0.5))
        self.assertFalse(self.dof.isvalid(self.min - 0.5))

    def test_continuous_dof_eq(self):
        oth = ContinuousDOF(self.min, self.max)
        self.assertTrue(self.dof == oth)

    def test_continuous_dof_rand(self):
        self.assertTrue(self.min <= self.dof.rand() <= self.max)
        nrand = 10
        samples = self.dof.rand(nrand)
        self.assertTrue(
            np.all(samples <= self.max) and np.all(self.min <= samples)
        )
