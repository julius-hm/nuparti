import sys
import os
sys.path.append(os.path.abspath("/workspaces/nuparti/nupartilib")) # Directorio raiz (codespaces)

from particles import *
import unittest

# Importamos las clases y a cada una se le hace test 

class TestParticleClasses(unittest.TestCase):
    def setUp(self):
        """Instancia de las clases Particle y Lepton para las pruebas"""
        self.particle = Particle(charge=1, mass=1, position={"x": 0, "y": 0, "z": 0})

        # Configuraciones (propiedades) de los leptones, bosones y quarks
        # Y creamos una lista de leptones/bosones/quarks a partir de las configuraciones

        self.lepton_configs = [
            {'charge': -1, 'mass': 0.511, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'generation': 'first', 'mean_life': '>6.6e28 yr'},
            {'charge': -1, 'mass': 105.65, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'generation': 'second', 'mean_life': 2.19e-6},
            {'charge': -1, 'mass': 1776.93, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'generation': 'third', 'mean_life': 290.3e-15},
            {'charge': 0, 'mass': 0, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'magnetic_moment': '<0.064e-10', 'generation': 'first'},
            {'charge': 0, 'mass': 0, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'magnetic_moment': '<0.064e-10', 'generation': 'second'},
            {'charge': 0, 'mass': 0, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'magnetic_moment': '<0.064e-10', 'generation': 'third'}
        ]
        

        self.leptons = [Lepton(**config) for config in self.lepton_configs]

        self.boson_configs = [
            {'charge': 0, 'mass': 0, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 1, 'interaction': "electromagnetic"},
            {'charge': 0, 'mass': 0, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 1, 'interaction': "strong"},
            {'charge': 0, 'mass': 0, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 2, 'interaction': "gravity"},
            {'charge': 1, 'mass': 80369.2, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 1, 'interaction': "weak"},
            {'charge': 0, 'mass': 91188, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 1, 'interaction': "weak"},
            {'charge': 0, 'mass': 125.2, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0, 'interaction': None}
        ]
        
        self.bosons = [Boson(**config) for config in self.boson_configs]

        self.quark_configs = [
            {'charge': 2/3, 'mass': 0, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'generation': "first"},
            {'charge': -1/3, 'mass': 4.70, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'generation': "first"},
            {'charge': -1/3, 'mass': 93.5, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'generation': "second"},
            {'charge': 2/3, 'mass': 1273, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'generation': "second"},
            {'charge': -1/3, 'mass': 4183, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'generation': "third"},
            {'charge': 2/3, 'mass': 4183, 'position': {'x': 0, 'y': 0, 'z': 0}, 'spin': 0.5, 'generation': "third"}
        ]
        
        self.quarks = [Quark(**config) for config in self.quark_configs]
    
    def test_particle_properties(self):
        """Prueba de las propiedades básicas de la superclase Particle"""
        self.assertEqual(self.particle.c, 1)
        self.assertEqual(self.particle.m, 1)
        self.assertEqual(self.particle.r, {"x": 0, "y": 0, "z": 0})
    
    def test_lepton_properties(self):
        """Prueba de las propiedades de los leptones (subclase)"""
        for lepton in self.leptons:
            # Verificar que leptones tienen los atributos esperados
            self.assertIn('Subtype: Fermion', lepton.properties())
            self.assertIn(f'Spin: {lepton.s} ħ', lepton.properties())
            self.assertIn(f'Generation: {lepton.g}', lepton.properties())

    def test_boson_properties(self):
        """Prueba de las propiedades de los bosones (subclase)"""
        for boson in self.bosons:
            # Verificar que bosones tienen los atributos esperados
            self.assertIn('Subtype: Boson', boson.properties())
            self.assertIn(f'Spin: {boson.s} ħ', boson.properties())
            self.assertIn(f'Interaction: {boson.i}', boson.properties())

    def test_quark_properties(self):
        """Prueba de las propiedades de los quarks (subclase)"""
        for quark in self.quarks:
            # Verificar que el quark tiene los atributos esperados
            self.assertIn('Subtype: Fermion', quark.properties())
            self.assertIn(f'Spin: {quark.s} ħ', quark.properties())
            self.assertIn(f'Generation: {quark.g}', quark.properties())
    
    def test_lepton_specific_properties(self):
        """Prueba de propiedades para cada lepton"""
        for i, lepton in enumerate(self.leptons):
            config = self.lepton_configs[i]
            
            self.assertEqual(lepton.c, config['charge'])
            self.assertEqual(lepton.m, config['mass'])
            self.assertEqual(lepton.s, config['spin'])
            self.assertEqual(lepton.g, config['generation'])
            
            # # Verificar las propiedades adicionales
            if 'mean_life' in config:
                self.assertEqual(lepton.l, config['mean_life'])
            else:
                self.assertIsNone(lepton.l)  # En caso de no tener vida media
            
            
            if 'magnetic_moment' in config:
                self.assertEqual(lepton.mm, config['magnetic_moment'])

    def test_boson_specific_properties(self):
        """Prueba de propiedades para cada bosón"""
        for i, boson in enumerate(self.bosons):
            config = self.boson_configs[i]
            
            self.assertEqual(boson.c, config['charge'])
            self.assertEqual(boson.m, config['mass'])
            self.assertEqual(boson.s, config['spin'])
            self.assertEqual(boson.i, config['interaction'])

    def test_quark_specific_properties(self):
        """Prueba de propiedades para cada quark"""
        for i, quark in enumerate(self.quarks):
            config = self.quark_configs[i]
            
            self.assertEqual(quark.c, config['charge'])
            self.assertEqual(quark.m, config['mass'])
            self.assertEqual(quark.s, config['spin'])
            self.assertEqual(quark.g, config['generation'])
    
    def test_properties_return_type(self):
        """Verifica que la propiedad 'properties' retorne una cadena"""
        for lepton in self.leptons:
            self.assertIsInstance(lepton.properties(), str)

if __name__ == "__main__":
    unittest.main()