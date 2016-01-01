#!/usr/bin/python

import argparse
import json
import os
import sys
import inspect
import linecache

from pprint import pprint
from prettytable import PrettyTable

DEFAULT_BASE_DIR='/Users/gokul/git_repositories/g3/server/'
DEFAULT_LISTEN_HOST='localhost'
DEFAULT_LISTEN_PORT='8090'

# dummy class (argument holder)
class Arguments:
    debug_level = 0
    base_dir    = DEFAULT_BASE_DIR
    listen_host = DEFAULT_LISTEN_HOST
    listen_port = DEFAULT_LISTEN_PORT

    def __init__(self):
        return

    def _make_dict(self):
        print_dict = {}
        print_dict['debug_level'] = self.debug_level
        print_dict['base_dir']    = self.base_dir
        print_dict['listen_host'] = self.listen_host
        print_dict['listen_port'] = self.listen_port
        return print_dict
    
    def __repr__(self):
        print self._make_dict()
        ret_str = 'debug_level = ' + str(self.debug_level)
        ret_str += ', base_dir = ' + self.base_dir
        ret_str += ', listen_host = ' + self.listen_host
        ret_str += ', listen_port = ' + self.listen_port
        return ret_str

    def __str__(self):
        pd = self._make_dict()
        pprint(pd)
        return json.dumps(pd)


# this will be imported into other files
global_args = Arguments()


# right now, this function appears in the class above also.
# that needs to be removed.
def debug_print(*pargs):
    if len(pargs) <= 2 :
        print "#DEBUG: Too few arguments to d_print function. At least 3 are needed: d_print( DEBUG_LEVEL, CONTEXT_STRING, VAR # ARGUMENTS...)"
        return
        
    # check if this print leve is greater than debug level
    print_level = pargs[0]
    if print_level > global_args.debug_level:
        return

    # get the context
    frame = inspect.currentframe()
    caller_frame = frame.f_back
    info = inspect.getframeinfo(caller_frame)

    # finish parsing pargs and create strings
    context_str = pargs[1]
    pargs_str = " ".join((map(lambda x: str(x), pargs[2:])))

    # create the message that includes context
    mesg_to_write = '[' + str(info.filename) + '|'\
                    + 'lineno:' + str(info.lineno) + '|'   \
                    + 'function:' + str(info.function) \
                    + '] : ' + context_str + ' ' + pargs_str + '\n'
    

    # finally, print
    print "#DEBUG:", mesg_to_write

# pretty printing
def debug_pprint(print_level, context_str, json_data): 
    if print_level <= global_args.debug_level:
        print "#DEBUG: [", context_str, "]"
        pprint(json_data)


def print_exception(terminate):
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
    if terminate:
        sys.exit(0)


# print a prettytable from a dictionary
# (where each key has value of same # of columns)
def print_table_from_dict(first_row, p_dict):
    d_first_row = list(first_row)
    d_first_row.insert(0,'')

    d_table = PrettyTable(d_first_row)
    
    row_no = 1
    for key,val in p_dict.iteritems():    
        d_row = [ str(row_no), key, val ]
        d_table.add_row(d_row)
        row_no += 1

    print d_table
    
# print all arguments as table
def print_args_as_table():

    # args_table -> a_table
    a_first_row = ["Argument/Parameter", "Value"]
    a_first_row.insert(0,'')

    a_table = PrettyTable(a_first_row)

    a_dict = global_args._make_dict()

    port = a_dict.pop('listen_port')
    
    row_no = 1
    for key,val in a_dict.iteritems():
        if key == "listen_host":
            val = "\033[31m " + "https://" + val + ":" + str(port) + '/' + "\033[0m"
        a_row = [ str(row_no), key, val ]
        a_table.add_row(a_row)
        row_no += 1

    print a_table
    '''
    # Make 'Critical' RED.
    if vd_item['summary'].lower().startswith('critical'):
    txt = "\033[31;43m" + vd_item['summary'] + "\033[0m"
    txt = "\033[31;43m" + vd_item['summary'] + "\033[0m"
    '''
    
    return
    
# this is not a class method
def parse_arguments():

    parser = argparse.ArgumentParser()

    #parser.add_argument("-c", "--cloud", type=str, 
    #                    help="the cloud that is being used", 
    #                    choices=['openstack','softlayer','platform'])

    parser.add_argument("-d", "--debug",  type=int,
                        help="debug level ([0..9]: 0 = no debug) (9 = lots of output)")

    parser.add_argument("-b", "--base_dir", type=str,
                        help="base directory for files")

    parser.add_argument("-l", "--listen_host", type=str,
                        help="host (or ip) to listen on")

    parser.add_argument("-p", "--port", type=str,
                        help="port to listen on")
    
    
    args = parser.parse_args()

    # do any processing of input args here
    # and return the processed args
    if args.debug != None:
        global_args.debug_level = args.debug

    if args.base_dir != None:    
        global_args.base_dir = args.base_dir

    if args.listen_host != None:
        global_args.listen_host = args.listen_host

    if args.port != None:
        global_args.listen_port = args.port

    # print all given arguments as neat table
    print_args_as_table()
        
    debug_pprint(3, "Command Line Args:", global_args)

    return

'''
# uncomment this and run for testing
# main
if __name__ == '__main__':
    parse_arguments()
    print global_args
'''
