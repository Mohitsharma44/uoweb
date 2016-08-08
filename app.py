from tornado import websocket, web, ioloop

clients = []

class WSHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in clients:
            clients.append(self)

    def on_close(self):
        if self in clients:
            clients.remove(self)

class ApiHandler(web.RequestHandler):
    @web.asynchronous
    def get(self, *args):
        self.render("index.html")

    def post(self, *args):
        self.file1 = self.request.files['file1'][0]
        self.orig_fname = self.file1['filename']
        print "Receiving file ... "
        for client in clients:
            client.write_message(self.file1['body'], binary=True)
        self.write("OK")
        

static_path = "./"

app = web.Application([
    (r'/', ApiHandler),
    (r'/ws', WSHandler),
    (r'/(.*)', web.StaticFileHandler, {'path': static_path})
])

if __name__ == "__main__":
    app.listen(8888)
    ioloop.IOLoop.instance().start()
