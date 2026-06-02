import http.server
import socketserver
import socket

PORT = 5000
HTML_FILE = "StudioDex___Roblox_API_Learning_Platform.html"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.path = "/" + HTML_FILE
        return super().do_GET()

    def log_message(self, format, *args):
        pass

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with ReusableTCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Serving StudioDex on port {PORT}", flush=True)
    httpd.serve_forever()
