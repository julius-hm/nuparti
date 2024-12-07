import sys
import os
sys.path.append(os.path.abspath("/workspaces/nuparti/nupartilib")) # Directorio raiz (codespaces)

from four_vector import *
from lorentz_transformation import *

import unittest
import numpy as np

# Creamos un 4-vector particular y verificamos que cumple las multiplicación con la matriz de la
# La transformación de Lorentz con la Identidad (4x4)
# Tiene que ser él mismo en este caso

class TestFourVector(unittest.TestCase):

    def test_multiplication_with_lorentz_transform(self):
        t, x, y, z = 1, 2, 3, 4
        four_vector = FourVector(t, x, y, z)
        
        lorentz_matrix = np.identity(4)
        lorentz_transform = LorentzTransformation(lorentz_matrix)
        transformed_vector = four_vector * lorentz_transform
        
        np.testing.assert_almost_equal(transformed_vector.vector, four_vector.vector)


if __name__ == '__main__':
    unittest.main()