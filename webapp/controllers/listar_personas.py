import web

import pyrebase

config = {
  "apiKey": "AIzaSyBy0ouvCBeUrUPtsWcaMQuHrqOuu4Maps0",
  "authDomain": "bd-nube-d853b.firebaseapp.com",
  "databaseURL": "https://bd-nube-d853b-default-rtdb.firebaseio.com",
  "storageBucket": "bd-nube-d853b.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)

print(f"Configuration: {firebase}")
db = firebase.database()

render = web.template.render("views", base = "master")

class Listar_personas:
    def GET(self):
        return render.listar_personas()

