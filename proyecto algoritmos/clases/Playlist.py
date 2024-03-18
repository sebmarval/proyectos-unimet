import uuid
from clases.Album import Album
from clases.Cancion import Cancion


class Playlist():
    def __init__(self, id:str, titulo: str, descripcion: str, creador:str, canciones:list[str], likes = []) -> None:
        if id == None:
            id = str(uuid.uuid4())
        self.id = id
        self.titulo = titulo.strip().title()
        self.descripcion = descripcion
        self.creador = creador
        self.canciones = canciones

        # Cosas ajenas a la api
        self.likes = set(likes)

    def buscarCanciones(self, albums: list[Album]):
        canciones_Playlist: list[Cancion] = []

        for cancionId in self.canciones:
            for album in albums:
                for cancion in album.tracklist:
                    if cancion.id == cancionId:
                        canciones_Playlist.append(cancion)

        for index, cancion in enumerate(canciones_Playlist):
            print(f"{index +1},{cancion.nombre}")

        while True:
            try: 
                opcion = int(input("Ingrese el número de la canción que desee")) - 1

                if opcion < 0:
                    print("Ingrese solo números positivos")
                    continue

                return canciones_Playlist[opcion]
            except:
                print("Ingrese un número válido")