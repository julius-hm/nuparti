from setuptools import setup, find_packages

setup(
    name="nuparti",  
    version="0.02",  
    packages=find_packages(),  
    description="Librería de Python para obtener datos y cálculos de partículas elementales",
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown", 
    author="Manuel Julius Hernández Martínez",  
    author_email="juliushm@ciencias.unam.mx",
    url="https://github.com/tu_usuario/nuparti",  # Añadir URL de tu proyecto o repositorio
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",  # Especifica la versión de Python
        "License :: OSI Approved :: MIT License",  # Licencia MIT
    ],
    python_requires=">=3.6",
    install_requires=[
        'numpy',
        'PyQt5'
    ],
    entry_points={
        'console_scripts': [
            'nupartilib_gui = nupartilib.gui:main',
        ],
    },
)