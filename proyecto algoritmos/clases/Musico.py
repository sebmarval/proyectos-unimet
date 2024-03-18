from clases.Album import Album
from clases.Cancion import Cancion
from clases.Usuario import Usuario


class Musico(Usuario):
    def __init__(self, id: str, name: str, username: str, correo: str,
                 likes_musico: list[str] = [], likes_album = [], likes_playlist = [], likes_canciones = [], canciones_Escuchadas = [], 
                 likes_recibidos = []) -> None:
        self.likes_recibidos = set(likes_recibidos)
        super().__init__(id, name, username, correo, "musician", likes_musico, likes_album, likes_playlist, likes_canciones,canciones_Escuchadas)

    def mostrar_Informacion(self, albums: list[Album]):
        reproduccionesTotales = 0
        canciones_Top = []

        print(f"Álbumes de música del músico {self.name}: ")
        for album in albums:
            if album.artista == self.id:
                print(f"Tracklist del album: {album.nombre}")
                for index, cancion in enumerate(album.tracklist):
                    print(f"{index +1}. {cancion.nombre}")
                    canciones_Top.append({
                        "nombre": cancion.nombre,
                        "reproducciones": cancion.reproducciones
                    })
                    reproduccionesTotales += cancion.reproducciones

        canciones_Top.sort(reverse=True, key= lambda item: item["reproducciones"])

        for index, cancion_Top in enumerate(canciones_Top):
            nombre = cancion_Top["nombre"]
            reproducciones = cancion_Top["reproducciones"]

            print(f"Top {index +1}: {nombre} ({reproducciones} reproducciones)")
            if index == 9:
                break

        print(f"Reproducciones totales: {reproduccionesTotales}")

    
    def buscarCanciones(self, albums: list[Album]):
        cancionesMusico: list[Cancion] = []

        for album in albums:
            if album.artista == self.id:
                cancionesMusico += album.tracklist

        for index, cancion in enumerate(cancionesMusico):
            print(f"{index +1},{cancion.nombre}")

        while True:
            try: 
                opcion = int(input("Ingrese el número de la canción que desee   ")) - 1

                if opcion < 0:
                    print("Ingrese solo números positivos")
                    continue

                return cancionesMusico[opcion]
            except:
                print("Ingrese un número válido")

