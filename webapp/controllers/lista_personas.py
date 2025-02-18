import web
from models.personas import Personas

render = web.template.render("webapp/views", base = "master")

class ListaPersonas:

    def GET(self):
      try:
        personas = Personas()
        print(f"{personas.lista_personas()}")
        return render.lista_personas()
      except Exception as error:
        print(error)

