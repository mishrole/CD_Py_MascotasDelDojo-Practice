class Ninja:
    # implementar __init__( nombre, apellido, premios, comida_mascota, mascota )
    def __init__(self, nombre, apellido, premios, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    # implementa los siguientes métodos:
    # caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    def caminar(self):
        self.mascota.jugar()
        return self

    # alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    def alimentar(self):
        self.mascota.comer()
        return self

    # bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
    def bañar(self):
        self.mascota.sonido()
        return self

    def estadoMascota(self):
        print(f'Nombre: {self.mascota.name}')
        print(f'Tipo: {self.mascota.tipo}')
        print(f'Salud: {self.mascota.salud}')
        print(f'Energía: {self.mascota.energía}')
        return self