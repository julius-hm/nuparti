import sys
import os
sys.path.append(os.path.abspath("/workspaces/nuparti/nupartilib")) # Directorio raiz (codespaces)

from lorentz_transformation import *
import unittest

# Importamos el módulo (en este caso, todo) y hacemos las prubeas para la dimensión  de alguna matriz
# Probaremos con la matriz identidad (se busca que cumpla al hacer la multiplicación)

class TestLorentzTransformation(unittest.TestCase):
    
    def setUp(self):
        """Matrices de prueba para las transformaciones de Lorentz"""
        self.valid_matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=complex) 

        self.invalid_matrix = np.array([
            [1, 0, 0], 
            [0, 1, 0], 
            [0, 0, 1]
        ], dtype=complex)  # Matriz 3x3, no válida (debe ser 4x4)

        # Damos la instancias para una transformación de Lorentz que sí sea válida
        self.lorentz_transformation = LorentzTransformation(self.valid_matrix)
    
    def test_matrix_size(self):
        """Prueba que la matriz de Lorentz tenga tamaño 4x4"""
        self.assertEqual(self.lorentz_transformation.get_matrix().shape, (4, 4))

    def test_invalid_matrix_size(self):
        """Error si la matriz no es 4x4"""
        with self.assertRaises(ValueError):
            LorentzTransformation(self.invalid_matrix)

    # Nota: rep1 y rep2 son también representaciones matriciales en el módulo original

    def test_rep1(self):
        """Prueba el método rep1 para la representación de Lorentz"""
        result = self.lorentz_transformation.rep1(None) 
        np.testing.assert_array_equal(result, self.valid_matrix)

    def test_rep2(self):
        """Prueba el método rep2 para la representación de Lorentz"""
        result = self.lorentz_transformation.rep2(None)
        np.testing.assert_array_equal(result, self.valid_matrix)

if __name__ == "__main__":
    unittest.main()