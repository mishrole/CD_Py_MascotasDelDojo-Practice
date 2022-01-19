class Mascota:
    # implementa __init__( name , tipo , golosinas ):
    def __init__(self, name, tipo, golosinas):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.energía = 5
        self.salud = 20
        self.ruido = 'BEEP BEEP!'

    # implementa los siguientes métodos:
    # dormir() - incrementa la energía de la mascota en 25
    def dormir(self):
        self.energía += 25
        return self

    # comer() - incrementa la energía de la mascota en 5 y la salud en 10
    def comer(self):
        self.energía += 5
        self.salud += 10
        return self

    # jugar() - incrementa la salud de la mascota en 5
    def jugar(self):
        self.salud += 5
        return self

    # ruido() - imprime el sonido que produce la mascota
    def sonido(self):
        print(f'{self.ruido}')
        return self