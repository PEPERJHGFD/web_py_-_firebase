import web

render = web.template.render("views", base = "master")

class Agregar:
    def GET(self):
        return render.agregar()