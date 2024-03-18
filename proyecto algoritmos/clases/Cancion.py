
class Cancion:
    def __init__(self, id:str, nombre:str, duracion:str, link:str, 
                 likes:list[str] = [], reproducciones = 0) -> None:
        self.id = id
        self.nombre = nombre.strip().title()
        self.duracion = duracion
        self.link = link
        # Cosas ajenas al API
        self.likes = set(likes)
        self.reproducciones = reproducciones

    def escuchar(self, usuario):
        self.reproducciones += 1
        print(f"Escuchando canción {self.nombre} ({self.link}) ({self.reproducciones} reproducciones)")
        usuario.canciones_Escuchadas.append(self.id)