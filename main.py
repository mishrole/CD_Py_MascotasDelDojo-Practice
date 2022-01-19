from Ninja import Ninja
from Mascota import Mascota

nina = Mascota("Nina", "Gato", 1)
ninja = Ninja("Mitchell", "Rodríguez", [], 1, nina)
ninja.alimentar().caminar().bañar().estadoMascota()