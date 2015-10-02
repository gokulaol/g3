#!/usr/bin/python

from utils import print_exception

class GetHandler:

    def __init__(self):
        # nothing much to do here
        self.basic_content = ''
        return

    # create HTML content saying inaccessible
    # and that path does not exist
    def content_inaccessible(self, path):

        content = {}

        content['type'] = 'text/html'

        c_str  = "<html>"
        c_str += "<head><title>Guru. Grace. Gratitude</title></head>"
        c_str += "<body> "
        c_str += "<p> Guru. Grace. Gratitude </p> "
        c_str += "<p>  File [" + path[1:] + "] not FOUND!!" + "</p>" 
        c_str += "</body>"
        c_str += "</html>"

        content['data'] = c_str
        return content


    def get_content(self, path):
        content = {}
        print "---> IN get_content:"

        try:
            file_name = path[1:]

            if file_name.endswith(".css"):
                content_type = "text/css"
            elif file_name.endswith(".js"):
                content_type = "application/javascript"
            else:
                content_type = "text/html"

            content['type'] = content_type
            print "trying to open the file...", file_name
            f = open(file_name, 'r')
            x = f.read()
            content['data'] = x

        except:

            print_exception(False)
            # if anything goes wrong, we return "inaccessible content"
            content = self.content_inaccessible(path)

        finally:

            print "---> OUT get_content: "
            return content
