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
    
    def Lista_personas(self):
        try:
            personas = db.child("personas").get()
            response =(
                "status":200,
                "message":"Todo bien",
                "personas":dict(personas.val())
            )
            return response
        except Exception as error:
            response =(
                "status":400,
                "message":"Algo fallo con el servidor",
                "personas":dict(personas.val())
            )

