"""Clase FourVector del paquete"""

import numpy as np

class FourVector:
    """
    Es un elemento del espacio vectorial espaciotemporal
    """
    def __init__(self, t, x, y, z):
        self.vector = np.array([t, x, y, z], dtype=complex)  # Arreglo del FourVector

    def __mul__(self, lorentz_transform):
        """
        Transformación de Lorentz al FourVector usando una matriz 4x4
        
        :param lorentz_transform es instancia del módulo LorentzTransform
        :return: Nuevo FourVector con los componentes transformadas
        """
        I = 1j 
        AR = lorentz_transform.rep1(2) # Representaciones para la transformación
        AL = lorentz_transform.rep2(2)

        # Matriz V para la transformación de Lorentz para los FourVectors
        V = np.array([[-self.vector[1] + I * self.vector[2], self.vector[3] + self.vector[0]],
                      [self.vector[3] - self.vector[0], self.vector[1] + I * self.vector[2]]], dtype=complex)

        # Aplicar la transformación utilizando las representaciones
        VP = AR @ V @ AL.T

        # Regresa un nuevo FourVector transformado
        return FourVector(
            t=np.real(VP[0, 1] - VP[1, 0]) / 2.0,
            x=np.real(VP[1, 1] - VP[0, 0]) / 2.0,
            y=np.imag(VP[0, 0] + VP[1, 1]) / 2.0,
            z=np.real(VP[0, 1] + VP[1, 0]) / 2.0
        )

    def __repr__(self):
        return f"FourVector(t={self.vector[0]}, x={self.vector[1]}, y={self.vector[2]}, z={self.vector[3]})"
