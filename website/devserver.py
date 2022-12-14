#!/usr/bin/env python
try:
    from http import server
except ImportError:
    import SimpleHTTPServer as server

class MyHTTPRequestHandler(server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        server.SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    server.test(HandlerClass=MyHTTPRequestHandler)