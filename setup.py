from setuptools import setup, find_packages

setup(
    name="nuparti",  
    version="0.01",  
    packages=find_packages(),  
    description="Librería de Python para obtener datos y cálculos para partículas elementales",
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown", 
    author="Manuel Julius Hernández Martínez",  
    author_email="juliushm@ciencias.unam.mx",
    url="  ",
    classifiers=[
        "Programming Language: 3",
        "License: MIT License",
    ],
    python_requires=">=3.6",
    install_requires=[],  # Por el momento, no se necesitan dependencias externas para ejecutar.
)
