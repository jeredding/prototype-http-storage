import web

urls = (
    '[fF]ile[s]?/', 'Files',
    '[fF]ile[s]?/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})', 'File',
)

app = web.application(urls, globals())


class Files(object):
    """This object manages collections of files.

    If a client sends a request to /Files then this object will manage that
    request.
    """

    def GET(self):
        raise NotImplementedError()


class File(object):
    """This object manages instances of files.

    If a client sends a request to /Files/<UUID> then this object will manage
    that request.
    """

    def GET(self, id):
        raise NotImplementedError()

if __name__ == "__main__":
    app.run()
