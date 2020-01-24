import http.server
import ptvsd
import socketserver
from http import HTTPStatus

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world!')


if __name__ == '__main__':
  ptvsd.enable_attach()
  print("Starting hello-world server...")
  server = socketserver.TCPServer(('0.0.0.0', 8080), Handler)
  server.serve_forever()
