from clases.Album import Album
from clases.Musico import Musico
from clases.Oyente import Oyente
from clases.Playlist import Playlist


class Gestion_Indicadores():
    def __init__(self, musicos: list[Musico], oyentes: list[Oyente], 
                 albums: list[Album], playlists: list[Playlist]) -> None:
        self.musicos = musicos
        self.oyentes = oyentes

        self.albums = albums
        self.playlists = playlists

    def menu(self):
        while True:
            try:
                opcion = int(input("""1. Mostrar top 5 de músicos
2. Mostrar top 5 de álbumes
3. Mostrar top 5 de canciones
4. Mostrar top 5 de oyentes
5. Salir
"""))

                if opcion == 1:
                    self.top5_musicos()
                elif opcion == 2:
                    self.top5_albumes()
                elif opcion == 3:
                    self.top5_canciones()
                elif opcion == 4:
                    self.top5_oyentes()

                elif opcion == 5:
                    print("Ha salido de la Gestión de Indicadores")
                    break  
                else:
                    raise Exception

            except:
                print("Ingrese una opción válida")

    def top5_musicos(self):
        musicos_top = []
        musicos_Ids = []

        for album in self.albums:
            artista = self.buscarUsuarioConId(album.artista)
            if artista == None:
                print("El artista del usuario, ya no se encuentra el sistema")
                continue
            
            try:
                indexUsuario = musicos_Ids.index(artista.id)
            except ValueError:
                musicos_Ids.append(artista.id)
                musicos_top.append({
                    "nombre": artista.name,
                    "reproducciones": 0
                })
                indexUsuario = -1
                
            for cancion in album.tracklist:
                musicos_top[indexUsuario]["reproducciones"] += cancion.reproducciones

        self.mostrar_top5(musicos_top)

            
    def buscarUsuarioConId(self, id):
        for usuario in self.musicos + self.oyentes:
            if usuario.id == id:
                return usuario

    def top5_albumes(self):
        albumes_Top = []
        for album in self.albums:
            albumes_Top.append({
                "nombre": album.nombre,
                "reproducciones": 0
            })

            for cancion in album.tracklist:
                albumes_Top[-1]["reproducciones"] += cancion.reproducciones
        
        self.mostrar_top5(albumes_Top)

    def top5_canciones(self):
        canciones_Top = []

        for album in self.albums:
            for cancion in album.tracklist:
                  canciones_Top.append({
                        "nombre": cancion.nombre,
                        "reproducciones": cancion.reproducciones
                    })

        self.mostrar_top5(canciones_Top)

    def mostrar_top5(self, items_Top):
        items_Top.sort(reverse=True, key= lambda item: item["reproducciones"])

        
        for index, item_Top in enumerate(items_Top):
            nombre = item_Top["nombre"]
            reproducciones = item_Top["reproducciones"]

            print(f"Top {index +1}: {nombre} ({reproducciones} reproducciones)")
            if index == 4:
                break


    def top5_oyentes(self):
        usuarios_Top = []

        for usuario in self.musicos + self.oyentes:
            usuarios_Top.append({
                    "nombre": usuario.name,
                    "reproducciones": len(usuario.canciones_Escuchadas)
                })
        
        self.mostrar_top5(usuarios_Top)
