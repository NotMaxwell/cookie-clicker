#!/usr/bin/env python3
"""
Simple HTTP server to serve Cookie Clicker locally
Usage: python serve.py [port]
Default port: 8000
"""
import http.server
import socketserver
import sys
import os
import webbrowser

# Change to the directory containing this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow cross-origin requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print(f"Serving Cookie Clicker at http://localhost:{PORT}")
            print(f"Open your browser to: http://localhost:{PORT}")
            print("Press Ctrl+C to stop the server")
            
            # Automatically open the browser
            webbrowser.open(f"http://localhost:{PORT}")
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except OSError as e:
        if e.errno == 10048:  # Port already in use
            print(f"Port {PORT} is already in use. Try a different port:")
            print(f"python serve.py {PORT + 1}")
        else:
            print(f"Error starting server: {e}")
