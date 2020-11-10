#Para definir una clase, es recomendable usar otro archivo
#Para tener todo mas ordenado

#class nombre_clase para definir una clase
class Cancion:

    #__init__ es lo que nosotros conocemos como metodo constructor
    #Es el primer metodo a ejecutarse en la clase persona
    #Hay muchos mas metodos pero este es el importante
    #Usamos self para hacer referencia a este objeto
    #Es como si usaramos el this en java 
                 #Nombre, Artista, Album, Imagen, Fecha, LinkSpotify, LinkYoutube
    def __init__(self,id,nombre,artista,album,imagen,fecha,spoti,youtube):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.imagen = imagen
        self.fecha = fecha
        self.spoti = spoti
        self.youtube = youtube

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