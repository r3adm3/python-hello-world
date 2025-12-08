from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <p>This is a simple Python web server.</p>
        </body>
        </html>
        '''
        self.wfile.write(html.encode())

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), HelloHandler)
    print('Server running on http://localhost:8000')
    server.serve_forever()