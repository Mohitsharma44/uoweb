#
# Author: Mohit Sharma
# Aug 08 2016
# CUSP 2016
#

"""

Module to accept images using post method
and display the data using websocket.

The image is not be saved on the server!

"""
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
        self.write("""<body style="background-color: grey;">
        <p style="color:yellow; font-size:500%;" align="center">Warning!! </br> </p> 
        <p style="font-size: 150%" align="center">Incorrect Operation </br> </p>""")
        self.write("""<p style="font-size:150%" align="center">Contact: Mohit.Sharma@nyu.edu </p> </body>""")
        self.finish()
        
    def post(self, *args):
        self.file1 = self.request.files['file1'][0]
        self.orig_fname = self.file1['filename']
        for client in clients:
            client.write_message(self.file1['body'], binary=True)
        self.write("OK")
        

static_path = "./"

app = web.Application([
    (r'/upload', ApiHandler),
    (r'/ws', WSHandler),
    (r'/(.*)', web.StaticFileHandler, {'path': static_path})
])

if __name__ == "__main__":
    app.listen(8888)
    ioloop.IOLoop.instance().start()
