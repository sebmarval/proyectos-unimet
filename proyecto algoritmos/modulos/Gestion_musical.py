import datetime
import pickle
from clases.Cancion import Cancion
from clases.Album import Album
from clases.Playlist import Playlist
from modulos.Gestion_Perfil import Gestion_Perfil

class Gestion_Musical:
    def __init__(self, albumes: list[Album], playlists: list[Playlist],
                 gestion_Perfil: Gestion_Perfil) -> None:
        self.albumes = albumes
        self.playlists = playlists
        self.gestion_Perfil = gestion_Perfil
        
    def menu(self):
        while True:
            try:
                opcion = int(input("""1. Crear un álbum musical
2. Escuchar música de un músico
3. Crear playlist
4. Busquedas
5. Reproducir musicas
6. Salir
"""))

                if opcion == 1:
                    self.crear_Album()
                elif opcion == 2:
                    self.escuchar_Musica()
                elif opcion == 3:
                    self.crear_Playlist()
                elif opcion == 6:
                    print("Ha salido de la Gestión Musical")
                    break  
                else:
                    raise Exception

            except:
                print("Ingrese una opción válida")

    def crear_Album(self): 
        nombre_Album = input("Ingrese el nombre que desea agregar a su Album: ")
        descripcion_Album = input("Coloque una descripción para dar a conocer su tema")
        portada_Album = input("Indique una portda para identificar su album")
        fecha_Album = datetime.datetime.today().strftime('%Y-%m-%dT%H:%M:%SZ')
        genero_Album = input("Coloque aqui el genero musical del album")
        canciones = []

        artista = self.gestion_Perfil.buscar_Usuario(exclusivamenteMusicos=True)
        if artista == None:
            print("No existe un músico con ese nombre")
            return

        while True: 
            cancion = self.crear_Cancion()
            canciones.append(cancion)
            opcion = input("desea seguir agregando canciones indique (Si o No): ").strip().title()
            if opcion == "Si":
                continue
            elif opcion == "No":
                break
            else:
                print("Entrada inválida, consideramos que continua deseando agregar más canciones")

        album = Album(None, nombre_Album, descripcion_Album, portada_Album, fecha_Album, genero_Album, artista.id, canciones)
        self.albumes.append(album)
        self.actualizar_Todos()

    def crear_Cancion(self): 
        id = None
        nombre = input("Ingrese el nombre de la canción que desea añadir: ")
        link = input("Ingrese el link de su canción: ")
        duracion = self.pedir_Duracion_Cancion()

        cancion = Cancion(id, nombre, duracion, link)
        return cancion

    def pedir_Duracion_Cancion(self):
        while True:
            try:
                duracion_Cancion_Minutos = int(input("Indique los minutos que dura su canción, recuerde que debe ser menor a 60 y mayor a 0: "))
                duracion_Cancion_Segundos = int(input("Indique los segundos que dura la canción, recuerde que debe ser menor a 60 y mayor a 0: "))

                if duracion_Cancion_Minutos < 0 and duracion_Cancion_Minutos > 59:
                    input("Recuerde que los minutos deben ser menor a 60 y mayor a 0: ")
                elif duracion_Cancion_Segundos < 0 and duracion_Cancion_Segundos > 59:
                    input("Recuerde que los segundos deben ser menor a 60 y mayor a 0: ")
                
                break
            except:
                print("Ingrese un número válido")

        return f"{duracion_Cancion_Minutos}: {duracion_Cancion_Segundos}"

    def escuchar_Musica(self):
        usuario = self.gestion_Perfil.usuario_Sesion
        if usuario == None:
            print("Necesita iniciar una sesión primero antes de escuchar")
            return
        while True:
            try:
                opcion = int(input("""1. Buscar Albums o Canciones
2. Buscar canciones por musico
3. Buscar canciones por playlist
4. Salir
"""))

                if opcion == 1:
                    resultado_Busqueda = self.buscar_Album_Canciones()
                    if resultado_Busqueda == None:
                        print("No existe una canción o álbum con este nombre")
                        return
                    
                    resultado_Busqueda.escuchar(usuario)
                elif opcion == 2:
                    musico = self.gestion_Perfil.buscar_Usuario(exclusivamenteMusicos=True)
                    if musico == None:
                        print("No existe un músico con ese nombre")
                        return

                    cancion = musico.buscarCanciones(self.albumes)
                    cancion.escuchar(usuario)
                elif opcion == 3:
                    playlist = self.buscar_Playlist()
                    if playlist == None:
                        print("No existe una playlist con ese nombre")
                        return
                    
                    cancion = playlist.buscarCanciones(self.albumes)
                    cancion.escuchar(usuario)

                elif opcion == 4:
                    print("Ha salido del buscador")
                    break  
                else:
                    raise Exception

            except:
                print("Ingrese un número válido")

    def buscar_Album_Canciones(self):
        nombre_buscado = input("Ingrese el nombre de la canción o el álbum: ").strip().title()
        for album in self.albumes:
            if album.nombre == nombre_buscado:
                return album
            
            for cancion in album.tracklist:
                if cancion.nombre == nombre_buscado:
                    return cancion
    
    def buscar_Playlist(self):
        nombre_buscado = input("Ingrese el nombre de la playlist a buscar: ").strip().title()

        for playlist in self.playlists:
            if playlist.titulo == nombre_buscado:
                return playlist

    def crear_Playlist(self): 
        id = None
        titulo_playlist = input("Indique el nombre que desea colocar a su playlist: ").strip().title()
        descripción_playlist = input("descríbanos sobre lo que trata tu playlist: ")
        creador = self.gestion_Perfil.usuario_Sesion
        if creador == None:
            print("Necesita iniciar sesión primero")

        canciones = []
        while True:
            cancionId = self.buscar_Cancion().id
            canciones.append(cancionId)

            opcion = input("Desea seguir agregando canciones indique (Si o No): ").strip().title()
            if opcion == "Si":
                continue
            elif opcion == "No":
                break
            else:
                print("Entrada inválida, consideramos que continua deseando agregar más canciones")
        playlist = Playlist(id, titulo_playlist, descripción_playlist, creador.id, canciones)
        self.playlists.append(playlist)
        self.actualizar_Todos()

    def buscar_Cancion(self):
          while True:
            try:
                opcion = int(input("""1. Buscar Albums o Canciones
2. Buscar canciones por musico"""))

                if opcion == 1:
                    resultado_Busqueda = self.buscar_Album_Canciones()
                    if resultado_Busqueda == None:
                        print("No existe una canción o álbum con este nombre")
                        continue
                    
                    if isinstance(resultado_Busqueda, Cancion):
                        return resultado_Busqueda
                    else:
                        cancion = resultado_Busqueda.buscarCanciones()
                        return cancion
                    
                elif opcion == 2:
                    musico = self.gestion_Perfil.buscar_Usuario(exclusivamenteMusicos=True)
                    if musico == None:
                        print("No existe un músico con ese nombre")
                        continue

                    cancion = musico.buscarCanciones(self.albumes)
                    return cancion
                else:
                    raise Exception

            except:
                print("Ingrese un número válido")

    def buscar_Album(self):
        nombre_buscado = input("Ingrese el nombre del álbum a buscar: ").strip().title()
        for album in self.albumes:
            if album.nombre == nombre_buscado:
                return album

    def actualizar_Todos(self):
        try:
            print("Actualianzado datos en todos los archivos")

            with open("pickle/musicos.pkl", "wb") as musicoFile:
                pickle.dump(self.gestion_Perfil.musicos,  musicoFile)
          
            with open("pickle/oyentes.pkl", "wb") as oyentesFile:
                pickle.dump(self.gestion_Perfil.oyentes, oyentesFile)   
        
            with open("pickle/palylists.pkl", "wb") as playlisstFile:
                pickle.dump(self.playlists, playlisstFile)

            with open("pickle/albums.pkl", "wb") as albumsFile:
                pickle.dump(self.albumes, albumsFile)         

        except:
          print("Error actualizando todos los archivos")
