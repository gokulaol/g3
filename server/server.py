#!/usr/bin/python

# +------------------------------------------------------------------------+
# | All the necessary methods to find and serve files and to handle        |
# | get/post requests etc. It is based on the BOTTLE python framework.     |
# | It is also secure (supports SSL, borrowed from a third party website)  |
# +------------------------------------------------------------------------+

import os

from bottle import route, run, template
from bottle import get, post, request
from bottle import static_file
from bottle import Bottle, ServerAdapter
from pprint import pprint

from arguments import global_args, parse_arguments
from arguments import print_exception, debug_print, debug_pprint

## simple testing

@route('/hello')
def hello():
    return "Hello World! from Bottle! - GBK."

@route('/greet/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you doing?', name=name)

## simple get and post - a form.

@get('/login') # or @route('/login')
def login():
    header = "<form action=\"/login\" method=\"post\">"
    username = "Username: <input name=\"username\" type=\"text\"/>"
    password = "Password: <input name=\"password\" type=\"password\"/>"
    login = "<input value=\"Login\" type=\"submit\" />"
    footer = "</form>"
    
    total_text = header + username + password + login + footer
    return total_text

    '''
    <form action="/login" method="post">
    Username: <input name="username" type="text" />
    Password: <input name="password" type="password" />
    <input value="Login" type="submit" />
    </form>
    '''


def find_containing_dir(file_name, top_level_dir):
    found = False

    try:
        
        debug_print(5, "top_level_dir : ", top_level_dir)
        #  use os.walk to identify the directory associated with the
        #  file and then return that as the root dir
        #    NOTE that the loop quits on first match.
        for root, dirs, files in os.walk(top_level_dir):
            if file_name in files:
                root_dir = root
                found = True
                break
        
        if found == False:
            print "Could not find the file <%s> in top level dir <%s>" %(file_name, top_level_dir)
            # we return global_args.base_dir here because the call will serve
            # using static_file, which takes care of return code.
            return global_args.base_dir
        else:
            return root_dir

    except:

        print_exception(True)

@route('/<n_file_name>')
def serve_normal_files(n_file_name):

    # get the name of the actual file 
    file_name = os.path.basename(n_file_name)
        
    debug_print(5, "normal files: file_name = ", file_name)

    # search in the path
    containing_dir = find_containing_dir(file_name, global_args.base_dir)
    
    # static_file takes care of returning correct STATUS code
    # even if the file is not found.
    return static_file(file_name, root=containing_dir)

@route('/images/<file_name>')
def serve_image_files(file_name):
    debug_print(5, "image files: file_name = ", file_name)
    return static_file(file_name, root=global_args.base_dir + 'images')

    
# serving bootstrap specific files
@route('/bootstrap-3.3.4/<b_file_name:path>')
def serve_bootstrap_files(b_file_name):

    # get the name of the actual file and
    file_name = os.path.basename(b_file_name)

    # find the containing dir
    containing_dir = find_containing_dir(file_name, global_args.base_dir + 'bootstrap-3.3.4')

    # static_file takes care of returning correct STATUS code
    # even if the file is not found.
    return static_file(file_name, root=containing_dir)


# Handle POST request for save
@post('/save')
def handles_save():

    input_data = {}
    
    input_data['title'] = request.forms.get('d_title')
    input_data['knowledge'] = request.forms.get('d_knowledge')
    input_data['place'] = request.forms.get('d_place')
    input_data['date'] = request.forms.get('d_date')
    
    debug_pprint(4, "save handler:", input_data)
    return "<p> HEE HEE: Your login information was correct.</p>"
    
    

#@route('/images/<filename:re:.*\.png>')
#def send_image(filename):
#    return static_file(filename, root='/path/to/image/files', mimetype='image/png')

    
def check_login(username, password):
    if username == 'gokul' :
	return True
    return False

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
        
# 
#  NOTE: the following code starts the bottle server with
#        SSL enabled.
#        Code to enable SSL taken from:
#        http://www.socouldanyone.com/2014/01/bottle-with-ssl.html
#
#
# copied from bottle. Only changes are to import ssl and wrap the socket
class SSLWSGIRefServer(ServerAdapter):
    def run(self, handler):
        
        try:
        
            from wsgiref.simple_server import make_server, WSGIRequestHandler
            import ssl
            if self.quiet:
                class QuietHandler(WSGIRequestHandler):
                    def log_request(*args, **kw): pass
                self.options['handler_class'] = QuietHandler
            srv = make_server(self.host, self.port, handler, **self.options)
            srv.socket = ssl.wrap_socket (
                srv.socket,
                certfile='server.pem',  # path to certificate
                server_side=True)
            srv.serve_forever()

        except:
            
            print_exception(True)

#            
# Running the server securely.        
#
# Normal RUN (no SSL, http://) :
#          run(host="0.0.0.0", port=8090)
# Secure RUN (SSL, https://)   : 
#          srv = SSLWSGIRefServer(host="localhost", port=8090)
#          run(server=srv)
#    
def main():

    parse_arguments()
    
    srv = SSLWSGIRefServer(host=global_args.listen_host,
                           port=global_args.listen_port)
    run(server=srv)    
    return

# main
if __name__ == '__main__':
    main()





