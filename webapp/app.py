import web
from controllers.index import Index as Index
from controllers.listar_personas import Listar_personas as Listar_personas
from controllers.agregar import Agregar as Agregar

urls = (
    '/', 'Index',
    '/agregar', 'Agregar',
    '/listar_personas', 'Listar_personas'
)

app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()
