#!/usr/bin/python

# test connection to mongodb, insert a few text documents,
# create a text index, do the search and print out the result.

import argparse
import pymongo

from pymongo import MongoClient
from arguments import print_exception, print_table_from_dict
import random

# core taken from  :  http://pythonfiddle.com/random-sentence-generator/
class RandomSentence():

    s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
    p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
    s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
    p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
    infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]

    def random_sentence(self):
        '''
        # Makes a random senctence from the different parts of speech. Uses a SINGULAR subject
        if input("Would you like to add a new word?").lower() == "yes":
            new_word = input("Please enter a singular noun.")
            s_nouns.append(new_word)
        else:
        '''
        sentence = ''
    	sentence += random.choice(self.s_nouns) + ' '
        sentence += random.choice(self.s_verbs) + ' '
        sentence += random.choice(self.s_nouns).lower() + ' ' or random.choice(self.p_nouns).lower() + ' '
        sentence += random.choice(self.infinitives) + ' '

        return sentence
    
def mongo_connect(host, port):
    client = MongoClient(host = host, port = port)
    print client
    return client

def mongo_input_data(client):
    # get a db
    db = client['test1']

    # get a collection
    col = db['col1']

    print col
    print db

    # item1
    str0 = 'this is the first item. the world is a wonderful place.'
    str0 += 'it is amazing to be in this knowledge.'
    item0 = { 'name'  : 'ITEM0',
              'tdata' : str0 }
    col.insert_one(item0)

    rs = RandomSentence()
    # insert 20 elements
    for i in range(1,20):
        sent = rs.random_sentence()
        item = { 'name' : 'ITEM' + str(i),
                 'tdata' : sent }
        col.insert_one(item)
        
    print db.collection_names(include_system_collections=False)

    i = 0
    p_dict = {}
    for item in col.find():        
        p_dict[i] = item
        i += 1

    print_table_from_dict(['Key','Value'],p_dict)

    # create a text index
    # col.create_index({"tdata" : "text"})
    col.ensure_index([('tdata' , 'text')], name='test_text_index')
        
    search_term = { "$text" : { "$search" : "Superman" } }
    x = col.find(search_term).limit(10)
    for item in x :
        print item
    
    #mongo.db.products.find(
    #   { '$text': { '$search': string } },
    #   fields=({ 'name': 1, 'foo': 1, 'bar': 1, 'score': { '$meta': 'textScore' } )
    

    
def mongo_text_search():
    return
    
def main():
    client = mongo_connect('localhost',27017)

    mongo_input_data(client)
    
# main
if __name__ == '__main__':
    main()

