import pyrebase

config = {
  "apiKey": "AIzaSyBnMWgOtB2XVRUZgPlZVG64Tl14EHFacgc",
  "authDomain": "perla-10493.firebaseapp.com",
  "databaseURL": "https://perla-10493-default-rtdb.firebaseio.com",
  "storageBucket": "perla-10493.firebasestorage.app"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

class Personas:
    def __init__(self):
        pass
    
    def lista_personas(self):
        try:
            personas = db.child("personas").get()
            response ={
                "status":200,
                "message":"Todo bien",
                "personas":dict(personas.val())
            }
            return response
        except Exception as error:
            print(f"{error.args[0]}")
            response ={
                "status":400,
                "message":"Error en el servidor",
                "personas":{}
                }
            return response
persona = Personas()
print(f"{persona.lista_personas()}")

            
