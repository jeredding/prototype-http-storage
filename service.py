import web

urls = (
    '[fF]ile[s]?/(.*)', 'Files',
    '[fF]ile[s]?/(.*)/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})', 'File',
)

app = web.application(urls, globals())


class Files(object):
    def GET(self):
        raise NotImplementedError()


class File(object):
    def GET(self, id):
        raise NotImplementedError()

if __name__ == "__main__":
    app.run()
