from clases.Album import Album
from clases.Playlist import Playlist
from clases.Usuario import Usuario

class Oyente(Usuario):
    def __init__(self, id: str, name: str, username: str, correo: str,
                likes_musico: list[str] = [], likes_album = [], likes_playlist = [], likes_canciones = [], canciones_Escuchada = [],) -> None:
        super().__init__(id, name, username, correo, "listener", likes_musico, likes_album, likes_playlist, likes_canciones, canciones_Escuchada)

    def mostrar_Informacion(self, albums: list[Album], playlists: list[Playlist]):
        print(f"Oyente: {self.name}")

        print("Álbumes gustados:")
        count = 0
        for idAlbum in self.likes_album:
            for album in albums:
                if idAlbum == album.id:
                    count += 1
                    print(f"{count}. {album.nombre}")

        print("Canciones gustadas:")
        count = 0
        for idCancion in self.likes_canciones:
            for album in albums:
                for cancion in album.tracklist:
                    if idCancion == cancion.id:
                        count += 1
                        print(f"{count}. {cancion.nombre}")

        print("Playlist creadas:")
        count = 0
        for playlist in playlists:
            if playlist.creador == self.id:
                count += 1
                print(f"{count}. {playlist.titulo}")