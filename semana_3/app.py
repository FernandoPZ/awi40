import web

urls = (
    '/(.*)', 'tax.controlles.visitas.Visitas'
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()