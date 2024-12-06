"""Clase FourVector del paquete"""

import numpy as np

class FourVector:
    """
    Es un elemento del espacio vectorial espaciotemporal
    """
    def __init__(self, t, x, y, z):
        self.vector = np.array([t, x, y, z], dtype=complex)  #Arreglo del FourVector

    def __mul__(self, lorentz_transform):
        """
        Transformación de Lorentz al FourVector usando una matriz 4x4
        
        :param lorentz_transform es instancia de la clase LorentzTransform
        :return: Nuevo FourVector con los componentes transformadas
        """
        # Matriz de Lorentz en general
        
        transformed_vector = lorentz_transform.get_matrix() @ self.vector
        return FourVector(
            t=np.real(transformed_vector[0]),
            x=np.real(transformed_vector[1]),
            y=np.real(transformed_vector[2]),
            z=np.real(transformed_vector[3])
        )

    def __repr__(self):
        return f"FourVector(t={self.vector[0]}, x={self.vector[1]}, y={self.vector[2]}, z={self.vector[3]})"
