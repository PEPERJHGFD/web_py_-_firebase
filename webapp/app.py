import web
from controllers.index import Index as Index
from controllers.lista_personas import ListaPersonas as ListaPersonas
from controllers.agregar import Agregar as Agregar

urls = (
    '/', 'Index',
    '/agregar', 'Agregar',
    '/lista_personas', 'ListaPersonas'
)

app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()
