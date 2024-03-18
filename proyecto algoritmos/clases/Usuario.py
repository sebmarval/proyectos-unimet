import uuid
from clases.Cancion import Cancion
from clases.Playlist import Playlist
from clases.Album import Album


class Usuario:
    def __init__(self, id: str, name: str, username:str, correo:str, type:str,
                 likes_musico, likes_album, likes_playlist, likes_canciones, canciones_Escuchadas: list) -> None:
        if id == None:
            id = uuid.uuid4() 
        self.id = id
        self.name = name.strip().title()
        self.username = username
        self.correo = correo 
        self.type = type

        self.likes_album = set(likes_album)
        self.likes_musico = set(likes_musico)
        self.likes_playlist = set(likes_playlist)
        self.likes_canciones = set(likes_canciones)
        
        self.canciones_Escuchadas = canciones_Escuchadas.copy()


    def __str__(self) -> str:
        return f"""Usuario {self.id}
Nombre: {self.name}
Username: {self.username}
Correo: {self.correo}"""

    def linea_TXT(self):
        # REVIEW - Guardar listas
        return f"{self.id}; {self.name}; {self.correo}; {self.username}; {self.likes_musico}; {self.likes_album}; {self.playlists_creadas}; {self.likes_canciones}; {self.playlists_creadas}"
    
    def likear_Album(self, album: Album):
        if self.id in album.likes:
            album.likes.remove(self.id)
            self.likes_album.remove(album.id)

            print(f"Se ha eliminado el like al album {album.nombre}: ({len(album.likes)})")
        else:
            album.likes.add(self.id)
            self.likes_album.add(album.id)

            print(f"Se ha agregado el like al album {album.nombre}: ({len(album.likes)})")

    def likear_Musico(self, musico):
        if self.id in musico.likes_recibidos:
            musico.likes_recibidos.remove(self.id)
            self.likes_musico.remove(musico.id)

            print(f"Se ha eliminado el like al músico {musico.name}: ({len(musico.likes_recibidos)})")
        else:
            musico.likes_recibidos.add(self.id)
            self.likes_musico.add(musico.id)

            print(f"Se ha agregado el like al músico {musico.name}: ({len(musico.likes_recibidos)})")

    def likear_Playlist(self, playlist: Playlist):
        if self.id in playlist.likes:
            playlist.likes.remove(self.id)
            self.likes_playlist.remove(playlist)

            print(f"Se ha eliminado el like a la playlist {playlist.titulo}: ({len(playlist.likes)})")
        else:
            playlist.likes.add(self.id)
            self.likes_playlist.add(playlist.id)

            print(f"Se ha agregado el like a la playlist {playlist.titulo}: ({len(playlist.likes)})")

    def likear_Cancion(self, cancion: Cancion ):
        if self.id in cancion.likes:
            cancion.likes.remove(self.id)
            self.likes_canciones.remove(cancion.id)

            print(f"Se ha eliminado el like a la canción {cancion.nombre}: ({len(cancion.likes)})")
        else:
            cancion.likes.add(self.id)
            self.likes_canciones.add(cancion.id)

            print(f"Se ha agregado el like a la canción {cancion.nombre}: ({len(cancion.likes)})")
        