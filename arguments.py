#!/usr/bin/python

import argparse
import json
import os
import sys
import inspect
import linecache

from pprint import pprint

# dummy class (argument holder)
class Arguments:
    debug_level = 0
    simulate = False
    params_file = None
    params_dict = None

    def __init__(self):
        return

    def __repr__(self):
        print 'debug_level = ', self.debug_level

    def __str__(self):
        print_dict = {}
        print_dict['debug_level'] = self.debug_level
        print_dict['simulate'] = self.simulate
        print_dict['params_file'] = self.params_file
        print_dict['params_dict'] = self.params_dict
        pprint(print_dict)
        return "\n"

    #    def d_print(self, print_level, context_str, **kwargs):
    #        if print_level <= self.debug_level:
    #            print "#DEBUG: [", context_str, "]", kwargs

    def d_print(self, *pargs):
        if len(pargs) <= 2 :
            print "#DEBUG: Too few arguments to d_print function. At least 3 are needed: d_print( DEBUG_LEVEL, CONTEXT_STRING, VAR # ARGUMENTS...)"
            return

        # check if this print leve is greater than debug level
        print_level = pargs[0]
        if print_level > self.debug_level:
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
                        + '] : ' + context_str + pargs_str + '\n'
        

        # finally, print
        print "#DEBUG:", mesg_to_write

    def d_pprint(self, print_level, context_str, json_data): 
        if print_level <= self.debug_level:
            print "#DEBUG: [", context_str, "]"
            pprint(json_data)

# this will be imported into other files
global_args = Arguments()


# right now, this function appears in the class above also.
# that needs to be removed.
def d_print(*pargs):
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
def d_pprint(print_level, context_str, json_data): 
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

# this is not a class method
def parse_arguments():

    parser = argparse.ArgumentParser()

    #parser.add_argument("-c", "--cloud", type=str, 
    #                    help="the cloud that is being used", 
    #                    choices=['openstack','softlayer','platform'])

    parser.add_argument("-d", "--debug",  type=int,
                        help="debug level ([0..9]: 0 = no debug) (9 = lots of output)")


    parser.add_argument("-s", "--simulate",
                        help="useful for debugging",
                        action="store_true")

    parser.add_argument("-p", "--params_file", type=str, 
                        help="your cloudbench related params")
    #                   choices=['gokul_cb_params.json','prabhakar_cb_params.json'])
    
    parser.add_argument("-mo", "--monitor_only",
                        help="activates only the Monitor part of the MAPE",
                        action="store_true")

    parser.add_argument("-ao", "--analyze_only",
                        help="activates only the Analyze part of the MAPE",
                        action="store_true")

    parser.add_argument("-po", "--plan_only",
                        help="activates only the Plan part of the MAPE",
                        action="store_true")

    parser.add_argument("-eo", "--execute_only",
                        help="activates only the Execute part of the MAPE",
                        action="store_true")
    
    args = parser.parse_args()

    # do any processing of input args here
    # and return the processed args
    global_args.debug_level = args.debug
    global_args.simulate = args.simulate
    
    if args.params_file == None:
        print "Pass in a params file with  --params_file  or  -p  option."
        sys.exit()

    global_args.params_file = args.params_file
    
    # open the params file and read the configuration parameters
    json_params_file = open(global_args.params_file)

    json_data = json.load(json_params_file)
        
    json_params_file.close()    

    # change any fields of json_data (such as simulate) to global settings
    if "MONITOR_PARAMS" in json_data:
        if "SIMULATE" in json_data["MONITOR_PARAMS"]:
            json_data["MONITOR_PARAMS"]["SIMULATE"] = global_args.simulate

    if args.monitor_only:
        json_data['EXP_LIST'] = ["MONITOR"]
    if args.analyze_only:
        json_data['EXP_LIST'] = ["ANALYZE"]
    if args.plan_only:
        json_data['EXP_LIST'] = ["PLAN"]
    if args.execute_only:
        json_data['EXP_LIST'] = ["EXECUTE"]    

    global_args.params_dict = json_data

    global_args.d_pprint(3, "Arguments (after command line overriding):", json_data)

    return
'''
# uncomment this and run for testing
# main
if __name__ == '__main__':
    parse_arguments()
    print global_args
'''
