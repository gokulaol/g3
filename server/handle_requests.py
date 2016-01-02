#!/usr/bin/python

import uuid
import json

from arguments import global_args, print_exception, debug_print, debug_pprint, print_table_from_dict

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
        try:
            # create a UUID and store it into the dictionary
            uuid_seed_string = self.req_params['d_series'] + self.req_params['d_date'] + self.req_params['d_sheetno']
            cur_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, uuid_seed_string)
            debug_print(5, "cur_uuid: ", cur_uuid, uuid.NAMESPACE_DNS)
            self.req_params['d_uuid'] = str(cur_uuid)

            if global_args.debug_level >= 5:
                print_table_from_dict([ 'POST param', 'Value'], self.req_params)

            # make a file name
            # The filename is "SERIES_<series_string>_DATE_<date_string>_SEQ_<sheet_no>.json"
            file_name = ''
            file_name += 'SERIES_'
            file_name += self.req_params['d_series'].replace(' ','_')
            file_name += '_DATE_'
            file_name += self.req_params['d_date'].replace('/','_').replace('-','_')
            file_name += '_SEQ_'
            file_name += self.req_params['d_sheetno']
            file_name += ".json"

            debug_print(5, "JSON file_name: ", file_name)
        
            # now write to a file
            full_file_name = global_args.base_dir + 'data/files/' + file_name
            with open(full_file_name, 'w') as outfile:
                json.dump(self.req_params, outfile, sort_keys = True,
                          indent = 4, ensure_ascii=False)

            return "<p> HEE HEE: Your login information was correct.</p>"

        except:
            print_exception(True)
    
    # returns the data to be sent back to the browser
    def handle_post(self):

        if self.req_params['d_type'] == 'KNOWLEDGE_INPUT_SAVE':
            return self.handle_knowledge_save()
        elif self.req_params['d_type'] == 'KNOWLEDGE_SEARCH':
            debug_print(5, "POST", self.req_params)
            return self.handle_knowledge_search()
        else:
            return None
        
        
