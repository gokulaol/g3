#!/usr/bin/python

# all mongo db related functions will be here.

import pymongo

from pymongo import MongoClient
from arguments import global_args, print_exception, debug_print, debug_pprint, print_table_from_dict
from arguments import color

# MongoDB related global constants
MONGO_DB_NAME='knowledge_text_db'
MONGO_COL_NAME='all_series'
# knowledge will be stored in this field of the JSON object, irrespective of series etc.
MONGO_KNOWLEDGE_FIELD='d_knowledge'
MONGO_TEXT_INDEX_NAME='knowledge_text_index'

# get the (db,col) related to knowledge
def _get_db_col():

    try:
        # get a client connection
        mongo_client = MongoClient(global_args.mongo_host,
                                   global_args.mongo_port)
        debug_print(5, "MongoClient:", mongo_client)

        # our knowledge_text database (has a fixed name)
        know_db_name = MONGO_DB_NAME
        know_db = mongo_client[know_db_name]

        # get the collection that has ALL the Series sheets
        know_col_name = MONGO_COL_NAME
        know_col = know_db[know_col_name]

        debug_print(5, "db,col: ", know_db, know_col)

        return know_db, know_col

    except:

        print_exception(True)
            
# this is invoked as the server starts up
# the main function here is to connect to
# mongo and also to create index. we maintain
# the main connection in a global variable
def mongo_init():

    try:
        # get the db and the collection
        know_db, know_col = _get_db_col()
        
        # make sure there is an index
        know_col.ensure_index([(MONGO_KNOWLEDGE_FIELD, 'text')], name=MONGO_TEXT_INDEX_NAME)

        print color.red("Ensured MongoDB Indices.")
        
    except:

        print_exception(True)
        

# search in the mongodb. right now, we are
# restricted to searching for one word
# we will return the # of results given
# by return_limit value.
#
# TODO: perhaps a better way is to use the
#       mongo cursor for this.
# 
def mongo_search(search_term, return_limit):
    result = []    
    try:
        # get the db and the collection
        know_db, know_col = _get_db_col()
 
        # make sure there is an index
        # know_col.ensure_index([('tdata' , 'text')], name='knowledge_text_index')

        s_term = { "$text" : { "$search" : search_term } }
        debug_print(5,"search_term:", s_term)

        x = know_col.find(s_term).limit(return_limit)
        y = know_col.find()
        for item in y:
            print item
        for item in x :
            debug_print(2, "Item: ", item)
            result.append(item)

        return result
    
    except:

        print_exception(True)
        
    
    
    
