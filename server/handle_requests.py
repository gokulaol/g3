#!/usr/bin/python

from arguments import global_args, print_exception, debug_print, debug_pprint

class HandleRequest:
    
    def __init__(self, req_type, req_params):
        self.req_type = req_type
        self.req_params = req_params
        return

    # returns the data to be sent back to the browser
    def get_return_data(self):
        debug_print(5, "", self.req_params)
        return "<p> HEE HEE: Your login information was correct.</p>"
