#!/usr/bin/python

import os

from bottle import route, run, template
from bottle import get, post, request
from bottle import static_file

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

# later, pass base_dir as an argument to the program
base_dir='/Users/gokul/git_reposotories/g3/server/'

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root=base_dir)

@route('/images/<filename>')
def server_static(filename):
    return static_file(filename, root=base_dir + 'images')

@route('/bootstrap-3.3.4/<filename:path>')
def server_static_bootstrap(filename):
    # All these files fall in the bootstrap DIR.
    found = False
    
    # 1) get the name of the actual file and
    serve_filename = os.path.basename(filename)

    # 2) use os.walk to identify the directory associated with the
    #    file and then set that as the root dir
    #    NOTE that the loop quits on first match.
    for root, dirs, files in os.walk(base_dir + 'bootstrap-3.3.4'):
        if serve_filename in files:
            root_dir = root
            found = True
            break
        
    if found == False:
        print "Cound not find the file ", serve_filename
        return None
    else:
        return static_file(serve_filename, root=root_dir)

@post('/save')
def handles_save():
    title = request.forms.get('d_title')
    print title
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


run(host='localhost', port=8080, debug=True)




