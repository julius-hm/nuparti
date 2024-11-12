# Creamos una superclase, Particles, cuyos atributos son comúnes para las partículas del ME
class Particle():
  '''Una particula es un constituyente fundamental del universo.
  Atributos
  ----------

  c: carga en unidades de [e]
  m: masa en unidades de [MeV]
  r: posición en unidades de [metros] (por definir)
  '''

  type = 'Particle'

  def __init__(self, charge, mass, position):
    self.c = charge
    self.m = mass
    self.r = position
    
    # Se definen las propiedades asociadas (self) con una cadena
  def properties(self): 
    r = self.r
    str_properties = f'Type: {self.type}\n' + (
      f'Charge: {self.c} e\n' +  # Unidades de carga del electrón
      f'Mass: {self.m} MeV\n' +  # Unidades de masa en reposo (MeV)
      f'Position: x={r["x"]} , y={r["y"]} , z={r["z"]} '  # Unidades de posición
      )
    return str_properties # Importante: Le decimos que regrese tipo, carga, masa y position


### Leptones ###

# Creamos una subclase para Leptones

class Lepton(Particle):        # Definimos que va heredar de la origiinal Particle
  def __init__(self, charge, mass, position, spin, generation, mean_life=None):  # Le damos las instancias, donde Mean Life es opcional
    Particle.__init__(self, charge, mass, position)    # Llamamos a la clase original
    self.s = spin                                      
    self.is_fermion = bool(spin % 1.0)                 # Evalúa si spin es número entero, bool semientero
    self.is_boson = not self.is_fermion                # fermión si no es bosón                                       
    self.g = generation
    self.l = mean_life

# Damos las atributos llamando a las de la clase original y se le agerga la de spin, generación y vida media
  def properties(self):
    properties_particle = super().properties()  # Usamos super() para llamar al método de la clase base/superclase
    properties_particle = properties_particle + f'\nSpin: {self.s} ħ'   # Agregamos los demás atributos a la cadena 
    properties_particle = properties_particle + f'\nGeneration: {self.g}'  
    properties_particle = properties_particle + f'\nMean Life: {self.l} s' 
    return properties_particle


# Definición del electrón
electron = Lepton(
    charge=-1,
    mass=0.511,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "first",              # Le damos valor de cadena de texto a las propiedades que lo requieren
    mean_life= ">6.6e28 yr"
)

# Definición del muón
muon = Lepton(
    charge=-1,
    mass=105.65,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "second",
    mean_life= 2.19e-6
)

# Definición de tau
muon = Lepton(
    charge=-1,
    mass=1776.93,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "second",
    mean_life= 290.3e-15  
) 

# Definición de electrón neutrino
electron_neutrino = Lepton(
    charge=0,
    mass=0,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "first"
) 

# Definición de muón neutrino
muon_neutrino = Lepton(
    charge=0,
    mass=0,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "second"
) 

# Definición de tau neutrino
tau_neutrino = Lepton(
    charge=0,
    mass=0,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "third"
) 

### Bosones ###

# De forma similar, cremoas una subclase para Bosones

class Boson(Particle):        # Definimos que va heredar de la origiinal Particle
  def __init__(self, charge, mass, position, spin, interaction=None):  # Le damos las instancias, donde Interaction es opcional
    Particle.__init__(self, charge, mass, position)    # Llamamos a la clase original
    self.s = spin                                      
    self.is_fermion = bool(spin % 1.0)                 # Evalúa si spin es número entero, bool semientero
    self.is_boson = not self.is_fermion                # fermión si no es bosón                                       
    self.i = interaction

# Damos las atributos llamando a las de la clase original y se le agerga la de spin, generación y vida media
  def properties(self):
    properties_particle = super().properties()  # Usamos super() para llamar al método de la clase base/superclase
    properties_particle = properties_particle + f'\nInteraction: {self.i}'   # Agregamos los demás atributos a la cadena  
    return properties_particle

# Definición del Fotón
photon = Boson(
    charge= 0,
    mass= 0,
    position={'x':0, 'y':0, 'z':0},
    spin= 1,
    interaction= "electromagnetic"
)

# Definición del Gluón
gluon = Boson(
    charge= 0,
    mass= 0,
    position={'x':0, 'y':0, 'z':0},
    spin= 1,
    interaction= "strong"
)

# Definición del Gravitón
graviton = Boson(
    charge= 0,
    mass= 0,
    position={'x':0, 'y':0, 'z':0},
    spin= 2,
    interaction= "gravity"
)

# Definición del Bosón W
w_boson = Boson(
    charge= +-1,
    mass= 80369.2,
    position={'x':0, 'y':0, 'z':0},
    spin= 1,
    interaction= "weak"
)

# Definición del Bosón Z
z_boson = Boson(
    charge= 0,
    mass= 91188,
    position={'x':0, 'y':0, 'z':0},
    spin= 1,
    interaction= "weak"
)

# Definición del Bosón de Higgs
higgs = Boson(
    charge= 0,
    mass= 125.2,
    position={'x':0, 'y':0, 'z':0},
    spin= 0
)

### Quarks ###

# Creamos una subclase para Quarks

class Quark(Particle):        # Definimos que va heredar de la origiinal Particle
  def __init__(self, charge, mass, position, spin, generation):  # Le damos las instancias
    Particle.__init__(self, charge, mass, position)    # Llamamos a la clase original
    self.s = spin                                      
    self.is_fermion = bool(spin % 1.0)                 # Evalúa si spin es número entero, bool semientero
    self.is_boson = not self.is_fermion                # fermión si no es bosón                                       
    self.g = generation

# Damos las atributos llamando a las de la clase original y se le agerga la de spin, generación y vida media
  def properties(self):
    properties_particle = super().properties()  # Usamos super() para llamar al método de la clase base/superclase
    properties_particle = properties_particle + f'\nSpin: {self.s} ħ'   # Agregamos los demás atributos a la cadena 
    properties_particle = properties_particle + f'\nGeneration: {self.g}' 
    return properties_particle

# Definición del Quark Up
quark_up = Quark(
    charge=2/3,
    mass=0,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation="first"
)

# Definición del Quark Down
quark_down = Quark(
    charge=2/3,
    mass=4.70,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "first"
)

# Definición del Quark Strange
quark_strange = Quark(
    charge= -1/3,
    mass= 93.5,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "second"
)

# Definición del Quark Charm
quark_charm = Quark(
    charge= 2/3,
    mass= 1273,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "second"
)

# Definición del Quark Bottom
quark_bottom = Quark(
    charge= -1/3,
    mass= 4183,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "third"
)

# Definición del Quark Up
quark_up = Quark(
    charge= -1/3,
    mass= 4183,
    position={'x':0, 'y':0, 'z':0},
    spin= 0.5,
    generation= "third"
)

#######