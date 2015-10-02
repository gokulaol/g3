#!/usr/bin/python

import time
import BaseHTTPServer
import ssl

from get_handler import GetHandler

HOST_NAME='9.2.212.51'
PORT_NUMBER=7777

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        # Response to a GET request: Get the content and write it
        # content dict will have the keys 'type' and 'data'
        gh = GetHandler()
        content = gh.get_content(self.path)

        self.send_response(200)
        self.send_header("Content-type", content['type'])
        self.end_headers()
        
        self.wfile.write(content['data'])


    def do_POST(self):
        # Handle a post request
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        self.end_headers()

        c_str  = "<html>"
        c_str += "<head><title>Guru. Grace. Gratitude</title></head>"
        c_str += "<body> "
        c_str += "<p> Guru. Grace. Gratitude </p> "
        # c_str += "<p>  File [" + path[1:] + "] not FOUND!!" + "</p>" 
        c_str += "</body>"
        c_str += "</html>"

        self.wfile.write(c_str)


        
if __name__ == '__main__':

    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    
    # for SSL
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile="./server.pem", server_side=True)

    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
