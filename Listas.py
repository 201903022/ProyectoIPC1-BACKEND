
class PlayList:


    def __init__(self,id,nombre,artista,album,imagen,fecha,spoti,youtube,user):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.imagen = imagen
        self.fecha = fecha
        self.spoti = spoti
        self.youtube = youtube
        self.user = user

    def getID(self):
        return self.id

    def getNombre(self):
        return self.nombre 

    def getArtista(self):
        return self.artista
    

    def getAlbum(self):
        return self.album

    def getImage(self): 
        return self.imagen

    def getFecha(self): 
        return self.fecha   

    def getLS(self): 
        return self.spoti
    def getLY(self): 
        return self.youtube
    def getUser(self): 
        return self.user


    def setId(self, id):
        self.id = id
    
    def setNombre(self, nombre): 
        self.nombre = nombre
    
    def setArtista(self, artista):
        self.artista = artista
    
   
    def setAlbum(self,album):
        self.album = album

    def setImagen(self,imagen):
        self.imagen = imagen
    def setFecha (self,fecha): 
        self.fecha = fecha
    def setLS(self, spoti):
        self.spoti = spoti
    def setLY(self, youtube): 
         self.youtube = youtube

    def setUser(self, user): 
         self.user = user