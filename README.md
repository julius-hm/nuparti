# nuparti
Esta librería proporciona datos básicos de las partículas elementales del Modelo Estándar y pretende servir para hacer cálculos.

Se pueden consultar información sobre fermiones y bosones.

Se han agregado los módulos:
Three_vector: Opreaciones con vectores 3D
Rotation: Girar un vector (3D) respecto a un eje
Four_Vector: Vector espaciotemporal para una una transofrmación de Lorentz
Lorentz_transformation: Para cálculos con 4-vectores

Se incluye un demo en un jupyternotebook

## Requisitos
Python 3.6 o superior

## Instalación (GitHub) desde terminal

git clone https://github.com/julius-hm/nuparti.git

cd nuparti

pip install .

###

## Ejemplos de uso:

# Definimos un par de ThreeVectors y generamos uno nuevo para rotarlo

from three_vector import *
from rotation import *
import numpy

v1 = ThreeVector(1, 2, 3)
v2 = ThreeVector(4, 5, 6)

v3 = v1 + v2

axis = ThreeVector(0, 0, 1)
rotation = Rotation(np.pi / 2, axis)

rotated_vector = rotation.apply(v3)

# Crear una transformación de Lorentz y la aplicamos a un Four_Vector

from particle import *
from lorentz_transform import *

lt = LorentzTransformation([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

fv = FourVector(1, 0, 0, 0)

transformed_fv = fv * lt

##

