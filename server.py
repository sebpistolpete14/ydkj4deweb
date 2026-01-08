import http.server
import socketserver

# This tells the server to correctly identify WASM files
MAP = http.server.SimpleHTTPRequestHandler.extensions_map
MAP['.wasm'] = 'application/wasm'

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    httpd.serve_forever()