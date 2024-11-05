# Creamos una superclase Particles, cuyos atributos son comúnes para las partículas del ME
class Particle():
  '''Las partículas elementales son las piezas más fundamentales del universo.
  Atributos

  c: carga en unidades de [e]
  m: masa en unidades de [MeV]
  r: posición en unidades de [u]
  '''

  type = 'Particle'

  def __init__(self, charge, mass, position):
    self.c = charge
    self.m = mass
    self.r = position
    
    # Se definen las propiedades asociadas self
  def properties(self):
    r = self.r  
    str_properties = f'Type: {self.type}\n' + (
      f'Charge: {self.c} e\n' +  # Unidades de carga del electrón
      f'Mass: {self.m} MeV\n' +  # Unidades de masa en reposo (MeV)
      f'Position: x={r["x"]} , y={r["y"]} , z={r["z"]} '  # Unidades de posición [u]
      )
    return str_properties # Importante: Le decimos que regrese tipo, carga, masa y position



# Creamos una subclase Elemntary Particle para Leptones, Bosones y Quarks

class ElementaryParticle(Particle):        # Definimos que va heredar de la origiinal Particle
  def __init__(self, charge, mass, position, spin, generation=None, mean_life=None):  # Le damos las instancias, Mean Life y Generación son opcionales
    Particle.__init__(self, charge, mass, position)    # Llamamos a la clase original
    self.s = spin                                      
    self.is_fermion = bool(spin % 1.0)                 # Evalúa si spin es número entero, bool semientero
    self.is_boson = not self.is_fermion                # fermión si no es bosón                                       
    self.g = generation
    self.l = mean_life

# Damos las atributos llamando a las de la clase original y se le agerga la de spin, generación y vida promedio
  def properties(self):
    properties_particle = super().properties()  # Usamos super() para llamar al método de la clase base
    properties_particle = properties_particle + f'\nSpin: {self.s} ħ'   # Agregamos los demás atributos a la cadena 
    properties_particle = properties_particle + f'\nGeneration: {self.g}'  
    properties_particle = properties_particle + f'\nMean Life: {self.l} s' 
    return properties_particle

### Leptones ###

# Definición del electrón
electron = ElementaryParticle(
    charge=-1,
    mass=0.511,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "first",              # Le damos valor de cadena de texto a la propiedad
    mean_life= ">6.6e28 yr"
)

# Definición del muón
muon = ElementaryParticle(
    charge=-1,
    mass=105.65,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "second",
    mean_life= 2.19e-6
)

# Definición de tau
muon = ElementaryParticle(
    charge=-1,
    mass=1776.93,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "second",
    mean_life= 290.3e-15  
) 

# Definición de electrón neutrino
electron_neutrino = ElementaryParticle(
    charge=0,
    mass=0,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "first"
) 

# Definición de muón neutrino
muon_neutrino = ElementaryParticle(
    charge=0,
    mass=0,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "second"
) 

# Definición de tau neutrino
tau_neutrino = ElementaryParticle(
    charge=0,
    mass=0,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "third"
) 

### Bosones ###

# Definición del Fotón
photon = ElementaryParticle(
    charge= 0,
    mass= 0,
    position={'x':0, 'y':0, 'z':0},
    spin= 1
)

# Definición del Gluón
gluon = ElementaryParticle(
    charge= 0,
    mass= 0,
    position={'x':0, 'y':0, 'z':0},
    spin= 1
)

# Definición del Gravitón
graviton = ElementaryParticle(
    charge= 0,
    mass= 0,
    position={'x':0, 'y':0, 'z':0},
    spin= 2
)

# Definición del Bosón W
w_boson = ElementaryParticle(
    charge= +-1,
    mass= 80369.2,
    position={'x':0, 'y':0, 'z':0},
    spin= 1
)

# Definición del Bosón Z
z_boson = ElementaryParticle(
    charge= 0,
    mass= 91188,
    position={'x':0, 'y':0, 'z':0},
    spin= 1
)

# Definición del Bosón de Higgs
higgs = ElementaryParticle(
    charge= 0,
    mass= 125.2,
    position={'x':0, 'y':0, 'z':0},
    spin= 0
)

### Quarks ###

# Definición del Quark Up
quark_up = ElementaryParticle(
    charge=2/3,
    mass=0,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation="first"
)

# Definición del Quark Down
quark_down = ElementaryParticle(
    charge=2/3,
    mass=4.70,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "first"
)

# Definición del Quark Strange
quark_strange = ElementaryParticle(
    charge= -1/3,
    mass= 93.5,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "second"
)

# Definición del Quark Charm
quark_charm = ElementaryParticle(
    charge= 2/3,
    mass= 1273,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "second"
)

# Definición del Quark Bottom
quark_bottom = ElementaryParticle(
    charge= -1/3,
    mass= 4183,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "third"
)

# Definición del Quark Up
quark_up = ElementaryParticle(
    charge= -1/3,
    mass= 4183,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "third"
)
