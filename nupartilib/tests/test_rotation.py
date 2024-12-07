import sys
import os
sys.path.append(os.path.abspath("/workspaces/nuparti/nupartilib")) # Directorio raiz (codespaces)

from three_vector import *
from rotation import *

import unittest
import numpy as np

# Probaremos que un vector en la dirección x sea rotado (pi/2) alrededor de un eje z

class TestRotation(unittest.TestCase):
    
    def setUp(self):
        """Prepara las instancias necesarias para las pruebas"""
        self.vector = ThreeVector(1, 0, 0)  # Vector canónico (dirección x)
        self.axis = ThreeVector(0, 0, 1)  # Eje de rotación (z)
        self.angle = np.pi / 2 
        self.rotation = Rotation(self.angle, self.axis)
    
    # Previamente, conocemos la matriz que debe resultar y la incluimos como referencia a esperar
    def test_matrix(self):
        """Verifica que la matriz de rotación sea calculada correctamente"""
        expected_matrix = np.array([
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ], dtype=complex)

        np.testing.assert_array_almost_equal(self.rotation.rotation_matrix, expected_matrix, decimal=5)

    def test_rotation(self):
        """Prueba que la rotación se aplique correctamente a un ThreeVector"""
        rotated_vector = self.rotation.apply(self.vector)
        expected_rotated_vector = ThreeVector(0, 1, 0)  # Después de rotar el vector (1, 0, 0) 90 grados alrededor del eje z

        self.assertEqual(rotated_vector, expected_rotated_vector)

    def test_axis(self):
        """Error si el eje de rotación no es un ThreeVector"""
        with self.assertRaises(ValueError):
            Rotation(self.angle, [0, 0, 1])  # Pasar una lista en lugar de un ThreeVector

    def test_zero(self):
        """Error si el eje de rotación es el vector cero"""
        with self.assertRaises(ValueError):
            Rotation(self.angle, ThreeVector(0, 0, 0))  # El eje de rotación no puede ser el vector cero

if __name__ == "__main__":
    unittest.main()
