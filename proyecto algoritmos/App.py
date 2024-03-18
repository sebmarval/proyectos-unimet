from io import TextIOWrapper
import pickle
import requests
from clases.Album import Album
from clases.Cancion import Cancion
from clases.Musico import Musico
from clases.Oyente import Oyente
from clases.Playlist import Playlist
from modulos.Gestion_Indicadores import Gestion_Indicadores
from modulos.Gestion_Interaccion import Gestion_Interaccion
from modulos.Gestion_Perfil import Gestion_Perfil
from modulos.Gestion_musical import Gestion_Musical

class App:
    def __init__(self) -> None:
        self.oyentes, self.musicos = self.leer_Usuarios()
        self.albumes = self.leer_Albums()
        self.playlists = self.leer_Playlists()

        self.gestion_Perfil = Gestion_Perfil(self.musicos, self.oyentes, self.albumes, self.playlists)
        self.gestion_musical = Gestion_Musical(self.albumes, self.playlists, self.gestion_Perfil)
        self.gestion_Interacciones = Gestion_Interaccion(self.gestion_Perfil,  self.gestion_musical)
        self.gestion_Indicadores = Gestion_Indicadores(self.musicos, self.oyentes, self.albumes, self.playlists)

    def leer_Usuarios(self):
      try:
        with open("pickle/musicos.pkl", "rb") as musicoFile:
          musicos = pickle.load(musicoFile)

        with open("pickle/oyentes.pkl", "rb") as oyentesFile:
          oyentes = pickle.load(oyentesFile)

        return musicos, oyentes
      except FileNotFoundError:
        return self.escribir_Usuarios()
         
    def escribir_Usuarios(self):
        try:
          print("Escirbiendo datos en los archivos de usuarios")
          oyentes, musicos = self.leer_Usuarios_API()
          with open("pickle/musicos.pkl", "wb") as musicoFile:
            pickle.dump(musicos, musicoFile)
          
          with open("pickle/oyentes.pkl", "wb") as oyentesFile:
            pickle.dump(oyentes, oyentesFile)          

          return oyentes, musicos
        except:
          print("Error escribiendo en los archivos de usuarios")
          return [], []      

    def leer_Usuarios_API(self):
      response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json")
      usuarios_JSON = response.json()

      oyentes_registro = []
      musicos_registro = []

      for usuario in usuarios_JSON:
          id = usuario["id"]
          name = usuario["name"]
          username = usuario["username"]
          email = usuario["email"]
          type = usuario["type"]

          if type == "listener":
              oyente = Oyente(id, name, username, email)
              oyentes_registro.append(oyente)
          elif type == "musician":
              usuario_musico = Musico(id, name, username, email)
              musicos_registro.append(usuario_musico)
          else:
              raise Exception("Tipo no valido")
      
      return oyentes_registro, musicos_registro

    def leer_Albums(self):
      try:
        print("Escirbiendo datos en los archivos de albums")

        with open("pickle/albums.pkl", "rb") as albumsFile:
          albums = pickle.load(albumsFile)

        return albums
      except FileNotFoundError:
        return self.escribir_Albums()
     
    def escribir_Albums(self):
      try:
        albums = self.leer_Albums_API()

        with open("pickle/albums.pkl", "wb") as albumsFile:
          pickle.dump(albums, albumsFile)          

        return albums
      except:
        print("Error escribiendo en los archivos de albumes")
        return []

    def leer_Albums_API(self):
      response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json")
      albums_JSON = response.json()

      albums = []

      for album in albums_JSON:
          id = album["id"]
          name = album["name"]
          description = album["description"]
          cover = album["cover"]
          published = album["published"]
          genre = album["genre"]
          artist = album["artist"]
          tracklist = album["tracklist"]

          canciones = []
          for track in tracklist:
            idCancion = track["id"]
            nameCancion = track["name"]
            durationCancion = track["duration"]
            linkCancion = track["link"]

            cancion  = Cancion(idCancion, nameCancion, durationCancion, linkCancion)
            canciones.append(cancion)

          albumClass = Album(id, name, description, cover, published, genre, artist, canciones)
          albums.append(albumClass)
      
      return albums

    def leer_Playlists(self):
      try:
        with open("pickle/playlists.pkl", "rb") as playlistFile:
          playlist = pickle.load(playlistFile)

        return playlist
      except FileNotFoundError:
        return self.escribir_Playlist()
    
    def escribir_Playlist(self):
      try:
        playlists = self.leer_Playlists_API()

        with open("pickle/playlists.pkl", "wb") as playlistFile:
          pickle.dump(playlists, playlistFile)   
      except:
        print("Error escribiendo en los archivos de playlists")
        return []

    def leer_Playlists_API(self):
      response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json")
      playlists_JSON = response.json()

      playlists = []

      for album in playlists_JSON:
          id = album["id"]
          name = album["name"]
          description = album["description"]
          creator = album["creator"]
          tracks = album["tracks"]

          playlistClass = Playlist(id, name, description, creator, tracks)
          playlists.append(playlistClass)
      
      return playlists

    def start(self):
      print("bienvenido a Metrotify")
      while True:
        try:
          opcion = int(input("""1. Gestión Perfil
2. Gestión de musica
3. Gestión de interacciones
4. Gestion de estadisticas
5. Salir
"""))

          if opcion == 1:
            self.gestion_Perfil.menu()
          elif opcion == 2:
            self.gestion_musical.menu()
          elif opcion == 3:
            self.gestion_Interacciones.menu()
          elif opcion ==4:
             self.gestion_Indicadores.menu()
          elif opcion == 5:
            print("Ha salido de la aplicación")
            break  
          else:
            raise Exception

        except:
          print("Ingrese una opción válida")


