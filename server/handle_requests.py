#!/usr/bin/python

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
    
    # returns the data to be sent back to the browser
    def handle_post(self):

        if self.req_params['type'] == 'KNOWLEDGE_INPUT_SAVE':
            debug_print(5, "", self.req_params)
            debug_print(5, "", "POST")
            return "<p> HEE HEE: Your login information was correct.</p>"
        elif self.req_params['type'] == 'KNOWLEDGE_SEARCH':
            debug_print(5, "", self.req_params)
            debug_print(5, "", "POST")
            return self.handle_knowledge_search()
        else:
            return None
        
        
