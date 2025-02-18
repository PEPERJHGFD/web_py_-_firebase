import web

render = web.template.render("webapp/views", base = "master")

class Index:
    def GET(self):
        return render.index()