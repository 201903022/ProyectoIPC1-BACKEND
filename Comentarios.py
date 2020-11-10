
class Comentario:
    def __init__(self,usuario,comentario,idC):
        self.usuario = usuario
        self.comentario = comentario
        self.idC = idC
    
    def getUser(self):
        return self.usuario

    def getIdC(self):
        return self.idC   

    def getComentario(self):
        return self.comentario
    #MEtodos SETS
    def setUser(self, usuario):
        self.usuario = usuario
    
    def setCom(self, apellido):
        self.apellido = apellido
    

    def setContraseña(self,comentario):
        self.comentario = comentario
    def setIdC(self,id):
        self.idC = id