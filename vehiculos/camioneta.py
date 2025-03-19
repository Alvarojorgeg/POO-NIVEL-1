from .vehiculo import Vehiculo

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga
    
    def __str__(self):
        return super().__str__() + f", carga {self.carga}"