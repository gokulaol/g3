#!/usr/bin/python

import uuid

from arguments import global_args, print_exception, debug_print, debug_pprint

class HandleRequest:
    
    def __init__(self, req_type, req_params):
        self.req_type = req_type
        self.req_params = req_params
        return

    def handle_knowledge_search(self):
        html_content = "<div class=\"row\">"
        html_content += "<div class=\"col-xs-9\">"
	html_content += "<div class=\"panel panel-primary\">"
	html_content += "<div class=\"panel-heading\">"
	html_content += "<h3 class=\"panel-title\">Panel title</h3>"
	html_content += "</div>"
	html_content += "<div class=\"panel-body\">"
	html_content += "Search Result 1"
	html_content += "</div>"
	html_content += "<div class=\"panel-footer\">Panel footer</div>"
	html_content += "</div>"
	html_content += "</div>"
	html_content += "</div>"	

        return html_content

    # save the given knowledge into an input file
    # we save every sheet in a unique file
    def handle_knowledge_save(self):
        # Make a UUID using the following INPUTs
        #
        # Make a uuid_seed_string = str(date) + str(series)
        # Use the uuid_seed_string with uuid.NAMESPACE_DNS + string (see uuid5())
        #
        uuid_seed_string = "Series"
        cur_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, uuid_seed_string)
        debug_print(5, "cur_uuid: ", cur_uuid, uuid.NAMESPACE_DNS)
        return "<p> HEE HEE: Your login information was correct.</p>"
        
        
    # returns the data to be sent back to the browser
    def handle_post(self):

        if self.req_params['type'] == 'KNOWLEDGE_INPUT_SAVE':
            debug_print(5, "POST", self.req_params)
            return self.handle_knowledge_save()
        elif self.req_params['type'] == 'KNOWLEDGE_SEARCH':
            debug_print(5, "POST", self.req_params)
            return self.handle_knowledge_search()
        else:
            return None
        
        
