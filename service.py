import web

urls = (
    '[fF]ile[s]?/?', 'Files',
    '[fF]ile[s]?/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})/?', 'File',
)

app = web.application(urls, globals())


class Files(object):
    """This object manages collections of files.

    If a client sends a request to /Files then this object will manage that
    request.
    """

    def GET(self):
        """This function returns a collection of file resources.

        This function accepts no input.

        This function outputs a JSON string representing a collection of file
        resources. The output should be produced in the following structure::

            [
                {
                    "id": <UUID>,
                    "path": "/relative/path/to/file",
                    "size": 0000
                }, ...
            ]
        """

        raise NotImplementedError()


class File(object):
    """This object manages instances of files.

    If a client sends a request to /Files/<UUID> then this object will manage
    that request.
    """

    def GET(self, id):
        """This function returns the requested portion of a binary file.

        Input
        =====

        This function requires the UUID of the target File resource. The UUID
        should be encoded in the URL in the pattern /File/<UUID>.

        This function also requires that standard HTTP Range headers be
        provided with the request. Ranges should be provided in terms of the
        starting and ending byte offsets to be delivered. For example, to
        retrieve the first 500 bytes of a file the following Range option
        should be provided::

            Range: bytes=0-499

        Output
        ======

        This function should output the raw, binary content of the requested
        file chunk.

        The HTTP response should also include a custom response header named
        Application-Validation-Hash that contains a SHA256 hash that can be
        used by the client to validate the chunk.
        """

        raise NotImplementedError()

if __name__ == "__main__":
    app.run()
