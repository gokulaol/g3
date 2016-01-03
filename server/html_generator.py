#!/usr/bin/python


# Class that generates HTML for twitter bootstrap GUI
class TwitterBootstrap_HTMLGenerator():

    depth_counter = {}
    
    def __init__(self):
        # color translators
        self.color_to_panel_type = {}
        self.color_to_panel_type['blue'] = 'panel-primary'
        self.color_to_panel_type['light-green'] = 'panel-success'
        self.color_to_panel_type['light-blue'] = 'panel-info'
        self.color_to_panel_type['yellow'] = 'panel-warning'
        self.color_to_panel_type['pink'] = 'panel-danger'

        # depth_counters are more for verification:
        #   for example no. of <div> and </div> must match.
        self.depth_counter['div'] = 0
        return

    # if the given color does not exist in our color_to_panel,
    # then return the value for the BLUE color.
    def color_to_panel_type(self, color):

        if color in self.color_to_panel_type:
            return self.color_to_panel_type[color]
        else:
            return self.color_to_panel_type['blue']

    def _parse_paragraph(self, paragraph):
        return paragraph.replace('\n','<br>\n')
        
    # outputs "<div class=\"xyz\">"  where xyz is the parameter 'classes'
    # sdiv stands for start_div
    def sdiv(self, classes):
        self.depth_counter['div'] += 1
        return "<div class=\"" + classes + "\">" + "\n"

    # ediv starts for end_div (</div>)
    def ediv(self):
        self.depth_counter['div'] -= 1
        return "</div>" + "\n"
    
    # generate HTML for a panel, given no. of columns (of the 12)
    # that we want to span and panel body, footer, etc.
    # we translate the COLOR parameter to twitter panel "type" (above)
    def generate_panel(self, n_columns, panel_color, panel_body,
                       panel_title=None, panel_footer=None):

        panel_type = self.color_to_panel_type[panel_color]

        html = ''

        # start a row
        html += self.sdiv('row')

        # how many cols are we spanning?
        html += self.sdiv('col-xs-' + str(n_columns)) #  "<div class=\"col-xs-" + str(n_columns) + "\">"
        html += self.sdiv('panel ' + panel_type)      #  "<div class=\"panel panel-primary\">"

        if panel_title != None:
            html += self.sdiv('panel-heading')            #  "<div class=\"panel-heading\">"
	    html += "<h3 class=\"panel-title\">" + panel_title + "</h3>"
            html += self.ediv()                           #  "</div>"

        html += self.sdiv('panel-body')               #  "<div class=\"panel-body\">"
	html += self._parse_paragraph(panel_body) + '\n'
        html += self.ediv()
        
        if panel_footer != None:
            html += self.sdiv('panel-footer')             #  "<div class=\"panel-footer\">"
	    html += panel_footer + '\n'
            html += self.ediv()
        
        html += self.ediv()
        html += self.ediv()

        print self.depth_counter['div']
        
        return html



# uncomment this and run for testing
'''
def main():
    
    twg = TwitterBootstrap_HTMLGenerator()

    html = twg.generate_panel(9, 'blue', "PTITLE", "PBODY", "PFOOTER")
    print html


# main
if __name__ == '__main__':
    main()
'''
