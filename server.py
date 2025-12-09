from http.server import HTTPServer, BaseHTTPRequestHandler
import signal
import threading

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
    
    # Suppress log messages for cleaner output (optional)
    def log_message(self, format, *args):
        return  # Silent mode

def shutdown_handler(signum, frame):
    print('\nShutting down server gracefully...')
    sys.exit(0)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), HelloHandler)
    print('Server running on http://localhost:8000')
    print('Press Ctrl+C to stop the server')
    
    # Run server in a separate thread
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    def shutdown_server(signum, frame):
        print('\nShutting down server gracefully...')
        server.shutdown()
        server.server_close()
        print('Server stopped.')
        exit(0)
    
    signal.signal(signal.SIGINT, shutdown_server)
    
    # Keep main thread alive
    try:
        server_thread.join()
    except KeyboardInterrupt:
        shutdown_server(None, None)