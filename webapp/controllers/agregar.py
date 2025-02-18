import web

render = web.template.render("webapp/views", base = "master")

class Agregar:
    def GET(self):
        return render.agregar()