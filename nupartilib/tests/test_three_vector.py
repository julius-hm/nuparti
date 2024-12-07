import sys
import os
sys.path.append(os.path.abspath("/workspaces/nuparti/nupartilib")) # Directorio raiz (codespaces)

from three_vector import *

import unittest
import numpy as np

# Crearemos un vector 3D para ver que cumpla con las operaciones de
# Suma, resta, multiplicación por escalar, producto interno y externo

class TestThreeVector(unittest.TestCase):

    def setUp(self):
        self.v1 = ThreeVector(1, 2, 3)
        self.v2 = ThreeVector(1, 2, 3)

    def test_add(self):
        result = self.v1 + self.v2
        expected = np.array([2, 4, 6], dtype=complex)
        np.testing.assert_almost_equal(result.vector, expected)

    def test_sub(self):
        result = self.v1 - self.v2
        expected = np.array([0, 0, 0], dtype=complex)
        np.testing.assert_almost_equal(result.vector, expected)

    def test_mul(self):
        scalar = 2.0
        result = self.v1 * scalar
        expected = np.array([2, 4, 6], dtype=complex)
        np.testing.assert_almost_equal(result.vector, expected)

    def test_dot(self):
        result = self.v1.dot(self.v2)
        expected = 14 
        self.assertEqual(result, expected)

    def test_cross(self):   
        result = self.v1.cross(self.v2)
        expected = np.array([0, 0, 0], dtype=complex) 
        np.testing.assert_almost_equal(result.vector, expected)

    def test_init(self):
        expected_repr = "ThreeVector(x=(1+0j), y=(2+0j), z=(3+0j))"
        self.assertEqual(repr(self.v1), expected_repr)


if __name__ == '__main__':
    unittest.main()
