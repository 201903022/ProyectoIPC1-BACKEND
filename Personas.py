#Para definir una clase, es recomendable usar otro archivo
#Para tener todo mas ordenado

#class nombre_clase para definir una clase
class Persona:

    #__init__ es lo que nosotros conocemos como metodo constructor
    #Es el primer metodo a ejecutarse en la clase persona
    #Hay muchos mas metodos pero este es el importante
    #Usamos self para hacer referencia a este objeto
    #Es como si usaramos el this en java
    def __init__(self,id,nombre,apellido,contraseña,username,tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
        self.username = username
        self.tipo = tipo
        self.id = id

    #En este caso no existe el encapsulamiento, asi que
    #Creamos nuestros metodos get y set

    #Los metodos get tienen como parametro el self, es decir
    #Que hace referencia a si mismo, pero este no se envia.
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    

    def getContra(self):
        return self.contraseña
    
    def getUser(self):
        return self.username
    def getTipo(self): 
        return self.tipo
    def getId (self): 
        return self.id


    #Los metodos set tambien llevan el parametro self, para saber
    #En que variable se guardara el valor que estamos mandandao
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    

    def setContraseña(self,contraseña):
        self.contraseña = contraseña

    def setUser(self,username):
        self.username = username