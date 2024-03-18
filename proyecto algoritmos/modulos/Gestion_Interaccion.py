from modulos.Gestion_Perfil import Gestion_Perfil
from modulos.Gestion_musical import Gestion_Musical


class Gestion_Interaccion():
    def __init__(self, gestion_Perfil: Gestion_Perfil, gestion_Musical: Gestion_Musical) -> None:
        self.gestion_Perfil = gestion_Perfil
        self.gestion_Musical = gestion_Musical

    def menu(self):
        while True:
            try:
                opcion = int(input("""1. Likear a un músico
2. Likear a un álbum
3. Likear a una canción
4. Likear a una playlist
5. Salir
"""))

                if opcion == 1:
                    self.like_A_Musico()
                elif opcion == 2:
                    self.like_A_Album()
                elif opcion == 3:
                    self.like_A_Cancion()
                elif opcion == 4:
                    self.like_A_Playlist()

                elif opcion == 5:
                    print("Ha salido de la Gestión de Interacciones")
                    break  
                else:
                    raise Exception

            except:
                print("Ingrese una opción válida")

    def like_A_Musico(self):
        usuario  = self.gestion_Perfil.usuario_Sesion

        if usuario == None:
            print("Necesita iniciar sesión antes de empezar a dar likes")

        musico = self.gestion_Perfil.buscar_Usuario(exclusivamenteMusicos=True)
        if musico == None:
            print("No existe un músico con ese nombre")   
        usuario.likear_Musico(musico) 
    
    def like_A_Album(self):
        usuario  = self.gestion_Perfil.usuario_Sesion

        if usuario == None:
            print("Necesita iniciar sesión antes de empezar a dar likes")

        album = self.gestion_Musical.buscar_Album()  
        if album == None:
            print("No existe un álbum con ese nombre")   
        usuario.likear_Album(album)

    def like_A_Cancion(self):
        usuario  = self.gestion_Perfil.usuario_Sesion

        if usuario == None:
            print("Necesita iniciar sesión antes de empezar a dar likes")

        cancion = self.gestion_Musical.buscar_Cancion()  
     
        usuario.likear_Cancion(cancion) 
    
    def like_A_Playlist(self):
        usuario  = self.gestion_Perfil.usuario_Sesion

        if usuario == None:
            print("Necesita iniciar sesión antes de empezar a dar likes")

        playlist = self.gestion_Musical.buscar_Playlist()  
        if playlist == None:
            print("No existe una playlist con ese nombre")  
        usuario.likear_Playlist(playlist) 
