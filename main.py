
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from Personas import Persona
from Canciones import Cancion
from Comentarios import Comentario
from Listas import PlayList
from Solicitudes import Solicitud

app = Flask(__name__)
CORS(app)

Usuarios = []
Usuarios.append(Persona(0,'Usuario','Maestro','admin','admin','admin'))
contarUsuarios = 0
Canciones = []
Comentarios = []
Playlists = []
SolicitudesL = []
cont_canciones = 0
con_usuarios = 1
contSoli = 0
contarSoli = 0

@app.route('/', methods=['GET'])
def rutaInicial():
    print("Hola si salio")
    return("Hola salio")

@app.route('/Personas', methods=['GET'])
def obtenerPersonas():
    global Usuarios
    Datos = []
    for usuario in Usuarios:
        Dato = {
            'nombre': usuario.getNombre(), 
            'apellido': usuario.getApellido(),
            'username' : usuario.getUser(),
            'id' : usuario.getId()
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Personas2/<string:username>', methods=['GET'])
def ObtenerPersona(username):
    global Usuarios
    for usuario in Usuarios:
        if usuario.getUser() == username:
            Dato = {
                'nombre': usuario.getNombre(), 
                'apellido': usuario.getApellido(),
                'username' : usuario.getUser(),
                'password' : usuario.getContra(),
                'id': usuario.getId()               
                }
            break
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/Login', methods=['POST'])
def Login1():
     global Usuarios
     username = request.json['username']
     password = request.json['password']
     for usuario in Usuarios: 
        if usuario.getUser() == username and usuario.getContra() == password: 
            Dato = {
                 'message' : 'Succes',
                 'username' : usuario.getUser(),
                 'tipo' : usuario.getTipo()

             }
            break 

        else:
             Dato = {
             'message' : 'Failed',
             'username' : ""
             }
     respuesta = jsonify(Dato)
     return (respuesta)
    
@app.route('/Registrar', methods=['POST'])
def Registrar():
    global Usuarios
    global contarUsuarios
    global con_usuarios
    username = request.json['username']
    password = request.json['password']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    tipo = 'cliente'
    id = con_usuarios
    encontrado = False

    for usuario in Usuarios: 
        if usuario.getUser() == username : 
            encontrado = True
            break 

    if encontrado:
        return jsonify({
            'message' : 'Failed',
            'reason' :'Usuario registrado' 

            })
            
    else:
        nuevo = Persona(id,nombre,apellido,password,username,tipo)
        Usuarios.append(nuevo)
        con_usuarios += 1
        return jsonify({
            'message' : 'Succes',
            'reason' : 'Se agrego'

        }) 

@app.route('/RecuperarPassword/<string:username>', methods=['GET'])
def RecuperarPassword(username): 
     global Usuarios
     encontrado = False
     password = " "
     for usuario in Usuarios: 
          if usuario.getUser() == username : 
            encontrado = True
            password = usuario.getContra()
            break 
     if encontrado:
        return jsonify({
            'message' : 'Success',
            'reason' :'Usuario encontrado',
            'password' : password 

            })   
     else: 
         return jsonify({
            'message' : 'Failed',
            'reason' :'Usuario no encontrado' 
            })           
      

@app.route('/Personas1/<string:username>', methods=['DELETE'])
def EliminarPersona(username):
    global Usuarios
    for i in range(len(Usuarios)):
        if username == Usuarios[i].getUser():
            del Usuarios[i]
            break
    return jsonify({'message':'Se elimino el dato exitosamente'})

@app.route('/Editar/<string:username>', methods=['PUT'])
def Editar(username):
    global Usuarios
    for i in range(len(Usuarios)):
        if username == Usuarios[i].getUser():
           Usuarios[i].setNombre(request.json['nombre'])
           Usuarios[i].setApellido(request.json['apellido'])
           Usuarios[i].setContraseña(request.json['password'])
        break
        
    return jsonify({'message':'Se actualizo el dato exitosamente'})

@app.route('/EditarU/<string:usernameN>/<string:usernameOld>', methods=['PUT'])
def EditarU(usernameN,usernameOld):
    global Usuarios
    encontrado = False
    for usuario in Usuarios: 
        if usernameN== usuario.getUser():
            encontrado = True
            break

    if encontrado:
       return jsonify({
           'message' : 'Failed',
           'rason' : 'Usuario ya registrado',
            'usuario' : usernameOld
 
       }) 
    else: 
        for i in range(len(Usuarios)):
         if usernameOld == Usuarios[i].getUser():
           Usuarios[i].setUser(usernameN)
           break
        return jsonify({
           'message' : 'Success',
           'rason' : 'Usuario acutalizado'
 
       }) 
        
@app.route('/Cancion', methods=['POST'])
def SCancion(): 
    global Canciones,cont_canciones
    id = cont_canciones
    nombre = request.json['nombre']
    artista = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spoti = request.json['spoti']
    you = request.json['youtube']
    #(self,id,nombre,artista,album,imagen,fecha,spoti,youtube):
    nuevo = Cancion(id,nombre,artista,album,imagen,fecha,spoti,you)
    Canciones.append(nuevo)
    cont_canciones += 1
    return jsonify({
        'message' : 'Success',
        'reason' : 'Se agrego la Cancion'
    }) 
@app.route('/CancionesM', methods=['GET'])
def obtenerCanciones():
    global Canciones,cont_canciones
    Datos = []
    for cancion in Canciones:
        Dato = {
            'id' : cancion.getID(),
            'nombre': cancion.getNombre(),
            'artista': cancion.getArtista(),
            'album' : cancion.getAlbum(),
            'fecha':  cancion.getFecha(), 
            'spoti' : cancion.getLS(), 
            'youtube': cancion.getLY(),
            'imagen' : cancion.getImage()

            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/CancionesG/<int:cancionB>', methods=['GET'])
def obtenerCancion(cancionB):
    global Canciones
    for cancion in Canciones:
        if cancionB== cancion.getID():
            Dato = {
            'id' : cancion.getID(),
            'nombre': cancion.getNombre(),
            'artista': cancion.getArtista(),
            'album' : cancion.getAlbum(),
            'fecha':  cancion.getFecha(), 
            'spoti' : cancion.getLS(), 
            'youtube': cancion.getLY(),
            'imagen' : cancion.getImage()
            }
            break
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/EditaCr/<int:cancion>', methods=['PUT'])
def EditarC(cancion):
    global Canciones
    for i in range(len(Canciones)):
        if cancion == Canciones[i].getID():
           Canciones[i].setNombre(request.json['nombre'])
           Canciones[i].setAlbum(request.json['album'])
           Canciones[i].setArtista(request.json['artista'])
           Canciones[i].setFecha(request.json['fecha'])
           Canciones[i].setImagen(request.json['imagen'])
           Canciones[i].setLS(request.json['spoti'])
           Canciones[i].setLY(request.json['youtube'])
        break
        
    return jsonify({'message':'Se actualizo el dato exitosamente'})

@app.route('/CancionD/<int:cancion>', methods=['DELETE'])
def DelCancion(cancion):
    global Canciones
    for i in range(len(Canciones)):
        if cancion == Canciones[i].getID():
            del Canciones[i]
            break
    return jsonify({'message':'Se elimino el dato exitosamente'})   
        
@app.route('/Comentar', methods=['POST'])
def Comentar(): 
    global Comentarios
    user = request.json['username']
    com = request.json['comentario']
    idC = request.json['id']
    nuevo = Comentario(user,com,idC)
    Comentarios.append(nuevo)
    return jsonify({
        'message' : 'Success',
        'reason' : 'Se agrego el comentario'
    }) 
@app.route('/ComentariosG', methods=['GET'])
def obtenerComentario():
    global Comentarios
    Datos = []
    for comentario in Comentarios:
        Dato = {
            'nombre': comentario.getUser(), 
            'id': comentario.getIdC(),
            'comentario' : comentario.getComentario()
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Comentarios/<string:idC>', methods=['GET'])
def obComentarios(idC):
    global Comentarios
    Datos = []
    for i in range(len(Comentarios)):
        print("id",idC)
        print("ComId",Comentarios[i].getIdC())
        if Comentarios[i].getIdC() == idC:
            Dato = {
               'username' : Comentarios[i].getUser(),
               'comentario': Comentarios[i].getComentario()
              }  
            Datos.append(Dato)            
    respuesta = jsonify(Datos)
    return(respuesta)
@app.route('/PlayList', methods=['POST'])
def Playlist(): 
    global Playlists
    encontrado = False
    id = request.json['id']
    nombre = request.json['nombre']
    artista = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spoti = request.json['spoti']
    you = request.json['youtube']
    username = request.json['username']
    for play in Playlists:
        if username == play.getUser() and id == play.getID():
         encontrado = True

    if encontrado: 
        return jsonify({ 
            'message' : 'Failed',
            'reason' : 'Ya esta en la PlayList'
         })
    else: 
        nuevo = PlayList(id,nombre,artista,album,imagen,fecha,spoti,you,username)
        Playlists.append(nuevo)
        return jsonify ({
         'message' : 'Success',
          'reason' : 'Se agrego a tu PlayList'
        
        })
        
@app.route('/Play/<int:user>', methods=['GET'])
def ObtenerPlay(user):
    global Playlists
    Datos = []
    for i in range(len(Playlists)):
        if user == Playlists[i].getUser():
            Dato = {
             'id' : Playlists[i].getID(),
             'nombre': Playlists[i].getNombre(),
             'artista': Playlists[i].getArtista(),
             'album' : Playlists[i].getAlbum(),
             'fecha':  Playlists[i].getFecha(), 
             'spoti' : Playlists[i].getLS(), 
             'youtube': Playlists[i].getLY(),
             'imagen' : Playlists[i].getImage(),
             'username' : Playlists[i].getUser()
             }
            Datos.append(Dato) 
            
    respuesta = jsonify(Datos)  
    return(respuesta)
@app.route('/PlayM', methods=['GET'])
def obPlay():
    global Playlists
    Datos = []
    for play in Playlists:
        Dato = {
             'id' : play.getID(),
             'nombre': play.getNombre(),
             'artista': play.getArtista(),
             'album' : play.getAlbum(),
             'fecha':  play.getFecha(), 
             'spoti' : play.getLS(), 
             'youtube': play.getLY(),
             'imagen' : play.getImage(),
             'username' : play.getUser()

            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)
@app.route('/PlayD/<int:user>/<string:idC>', methods=['DELETE'])
def DelPlay(user,idC):
    global Playlists
    for i in range(len(Playlists)):
        if user == Playlists[i].getUser() and idC == Playlists[i].getID():
            del Playlists[i]
            break
    return jsonify({'message':'Se elimino el dato exitosamente'}) 

@app.route('/Solicitud', methods=['POST'])
def NSoli(): 
    global SolicitudesL,contSoli,contarSoli
    id = contSoli
    total = contarSoli
    print(total)
    nombre = request.json['nombre']
    print(nombre)
    artista = request.json['artista']
    print(artista)
    album = request.json['album']
    print(album)
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spoti = request.json['spoti']
    you = request.json['youtube']
    #(self,id,nombre,artista,album,imagen,fecha,spoti,youtube,total)#
    nuevo = Solicitud(id,nombre,artista,album,imagen,fecha,spoti,you,total)
    SolicitudesL.append(nuevo)
    contSoli += 1
    contarSoli += 1
    return jsonify({
        'message' : 'Success',
        'reason' : 'Se agrego la Cancion'
    }) 

@app.route('/SolicitudM', methods=['GET'])
def obSoli():
    global SolicitudesL,contSoli,contarSoli
    Datos = []
    for soli in SolicitudesL:
        Dato = {
            'id' : soli.getID(),
            'nombre': soli.getNombre(),
            'artista': soli.getArtista(),
            'album' : soli.getAlbum(),
            'fecha':  soli.getFecha(), 
            'spoti' : soli.getLS(), 
            'youtube': soli.getLY(),
            'imagen' : soli.getImage(),
            'total' : soli.getTotal()

            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/SolictudG/<int:soli>', methods=['GET'])
def obUSoli(soli):
    global SolicitudesL
    for solit in SolicitudesL:
        if soli== solit.getID():
            Dato = {
            'id' : solit.getID(),
            'nombre': solit.getNombre(),
            'artista': solit.getArtista(),
            'album' : solit.getAlbum(),
            'fecha':  solit.getFecha(), 
            'spoti' : solit.getLS(), 
            'youtube': solit.getLY(),
            'imagen' : solit.getImage()
            }
            break
    respuesta = jsonify(Dato)
    return(respuesta)
      
if __name__ == "__main__":
     app.run(threade=True, host="0.0.0.0", port=5000, debug=True)