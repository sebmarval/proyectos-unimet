import uuid
from clases.Cancion import Cancion


class Album:
    def __init__(self, id:str, nombre:str, descripcion:str, portada:str, fecha:str, genero:str, 
                 artista: str, tracklist:list[Cancion], likes = []) -> None:
        if id == None:
            id = uuid.uuid4() 
        self.id = id
        self.nombre = nombre.strip().title()
        self.descricpcion = descripcion
        self.portada = portada
        self.fecha = fecha
        self.genero = genero 
        self.artista = artista
        self.tracklist = tracklist
        # Cosas ajenas a la APi
        self.likes = set(likes)

    def escuchar(self, usuario):
        for cancion in self.tracklist:
            cancion.escuchar(usuario)

    def buscarCanciones(self):
        for index, cancion in enumerate(self.tracklist):
            print(f"{index +1},{cancion.nombre}")

        while True:
            try: 
                opcion = int(input("Ingrese el número de la canción que desea")) - 1

                if opcion < 0:
                    print("Ingrese solo números positivos")
                    continue

                return self.tracklist[opcion]
            except:
                print("Ingrese un número válido")