from Mascota import Mascota

class Gato(Mascota):
    def __init__(self, name, tipo, golosinas):
        super().__init__(name, tipo, golosinas)
        self.patrón = "Calicó"
        self.ruido = "MIAU"
    
    def maullar(self):
        print(f"{self.ruido}")
        return self