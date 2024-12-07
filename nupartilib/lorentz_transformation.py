"""Clase LorentzTransformation del paquete"""
import numpy as np

class LorentzTransformation:
    """
    Transformación de Lorentz en 4 dimensiones con matrices (complejas)
    """
    def __init__(self, matrix):
        # Matriz de Lorentz 4x4 (cambios en las 4 direcciones)
        self.matrix = np.array(matrix, dtype=complex)
        if self.matrix.shape != (4, 4):
            raise ValueError("La matriz debe 4x4")

    def get_matrix(self):
        return self.matrix

    def rep1(self, param):
        # rep1 devuelve la representación de Lorentz
        return self.matrix

    def rep2(self, param):
        # rep2 devuelve la otra representación de Lorentz
        return self.matrix

    def __repr__(self):
        return f"LorentzTransformation(matrix={self.matrix})"
