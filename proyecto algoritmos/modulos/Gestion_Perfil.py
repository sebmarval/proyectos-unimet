import pickle
from clases.Album import Album
from clases.Musico import Musico
from clases.Oyente import Oyente
from clases.Playlist import Playlist


class Gestion_Perfil:
    def __init__(self, musicos: list[Musico], oyentes: list[Oyente], 
                 albums: list[Album], playlists: list[Playlist]) -> None:
        self.musicos = musicos
        self.oyentes = oyentes

        self.albums = albums
        self.playlists = playlists

        self.usuario_Sesion: Musico | Oyente | None = None

    def menu(self):
        while True:
            try:
                opcion = int(input("""1. Registar nuevos usuarios
2. Iniciar sesión
3. Buscar perfiles
4. Cambiar información personal de la cuenta
5. Borrar los datos de la cuenta
6. Salir
"""))

                if opcion == 1:
                    self.registar_Usuarios()
                elif opcion == 2:
                    self.iniciar_Sesion()
                elif opcion == 3:
                    usuario = self.buscar_Usuario()
                    if usuario == None:
                        print("El usuario que busca no se encuntra registrado")
                        return
                    
                    if isinstance(usuario, Oyente):
                        usuario.mostrar_Informacion(self.albums, self.playlists)
                    else:
                        usuario.mostrar_Informacion(self.albums)

                elif opcion == 4:
                    self.cambiar_Infomracion()
                elif opcion == 5:
                    self.eliminar_Usuario()
                elif opcion == 6:
                    print("Ha salido de la Gestión de Perfil")
                    break  
                else:
                    raise Exception

            except:
                print("Ingrese una opción válida")

    def registar_Usuarios(self):
        nombre = input("Ingrese su nombre, recuerde no usar caracteres especiales ni espacios: ")
        email = self.pedir_Email()
        username = input("Ingrese el username por el cual le gustaría ser llamado: ")
        tipo = self.pedir_Tipo_Usuario()

        if tipo == "Oyente":
            oyente = Oyente(None, nombre, email, username)
            self.oyentes.append(oyente)
        elif tipo == "Musico":
            musico = Musico(None, nombre, email, username)
            self.musicos.append(musico)
        
        self.actualizar_Usuarios()
        return

    def pedir_Email(self):
        repetido = True
        while repetido:
            correo = input("Ingrese un email: " )
            repetido = False

            for usuario in self.oyentes + self.musicos:
                if usuario.correo == correo:
                    print("Ya existe una cuenta asignada a ese correo, por favor ingrese uno distinto")
                    repetido = True
                    break
        
        return correo


    def pedir_Tipo_Usuario(self):
        while True:
            tipo = input("Les gustaría ser musico u oyente?: ").strip().title()

            if tipo != "Oyente" and tipo != "Musico":
                print("Ingrese un tipo válido, por favor")
                continue
            return tipo

    def iniciar_Sesion(self):
        nombre = input("Coloca el nombre de tu usario para ingresar a la cuenta: ")
        usuario = self.buscar_Usuario(nombre)
        if usuario == None:
            print("No se encontró ningún usuario con ese nombre")
            return
        self.usuario_Sesion = usuario
        print("Se ha iniciado sesión con el siguiente usuario: ")
        print(usuario)

    def buscar_Usuario(self, nombre = "", exclusivamenteMusicos = False):
        if nombre == "":
            nombre = input("Coloque el nombre del usuario que desea buscar: ")

        if exclusivamenteMusicos == True:
            usuarios = self.musicos
        else:
            usuarios = self.oyentes + self.musicos

        for usuario in usuarios:
            if usuario.name == nombre:
                return usuario
        
    def cambiar_Infomracion(self):
        if self.usuario_Sesion == None:
            print("Debes estar en tu sesión para poder editar tu información")
            return
        
        while True:
            try:
                opcion = int(input("""Escoja que información desea cambiar 
1. Modificar nombre
2. Modifcar correo
3. Modificar username
4. Salir
"""))

                if opcion == 1:
                    nombre_Cambio = input("Ingrese su nuevo nombre: ")

                    print(f"Usuario ha cambiado su nombre de {self.usuario_Sesion.name} a {nombre_Cambio}")
                    self.usuario_Sesion.name = nombre_Cambio
                    self.actualizar_Usuarios()

                elif opcion == 2:
                    correo_Cambio = self.pedir_Email()

                    print(f"Usuario ha cambiado su corrreo de {self.usuario_Sesion.correo} a {correo_Cambio}")
                    self.usuario_Sesion.correo = correo_Cambio
                    self.actualizar_Usuarios()
                elif opcion == 3:
                    username_Cambio = input("Ingrese su nuevo username: ")
                    
                    print(f"Usuario ha cambiado su username de {self.usuario_Sesion.username} a {username_Cambio}")
                    self.usuario_Sesion.username = username_Cambio
                    self.actualizar_Usuarios()

                elif opcion == 4:
                    print("Ha salido de la modificación de su cuenta")
                    break
                else:
                    raise Exception

            except:
                print("Ingrese una opción válida")

    def eliminar_Usuario(self):
        if self.usuario_Sesion == None:
            print("Debes estar en tu sesión para poder editar tu información")
            return
        
        for index, oyente in enumerate(self.oyentes):
            if self.usuario_Sesion.id == oyente.id:
                self.oyentes.pop(index)
                print(f"Se ha eliminado el oyente: {self.usuario_Sesion.name}")
                self.usuario_Sesion = None
                self.actualizar_Usuarios()
                return

        for index, musico in enumerate(self.musicos):
            if self.usuario_Sesion.id == musico.id:
                self.musicos.pop(index)
                print(f"Se ha eliminado el musico: {self.usuario_Sesion.name}")
                self.usuario_Sesion = None
                self.actualizar_Usuarios()
                return

        print("El usuario no se encuentra en la base de datos")
        
    def actualizar_Usuarios(self):
        try:
          print("Actualianzado datos en los archivos de usuarios")

          with open("pickle/musicos.pkl", "wb") as musicoFile:
            pickle.dump(self.musicos, musicoFile)
          
          with open("pickle/oyentes.pkl", "wb") as oyentesFile:
            pickle.dump(self.oyentes, oyentesFile)          

        except:
          print("Error actualizando los archivos de usuarios")
