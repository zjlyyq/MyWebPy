import web
from handler import Handle
urls = (
    #'/(.*)', 'Handle'
    '/(wx)', 'Handle'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        data = web.input()
        if not data:
            return "hello " + name
        return data.id