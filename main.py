from vehiculos.coche import Coche
from vehiculos.moto import Moto
from utilidades.catalogo import catalogar


vehiculos = [
    Coche("Rojo", 4, 180, 2000),
    Moto("Negra", 2, "Deportiva")
]

catalogar(vehiculos) 
catalogar(vehiculos, 2) 
