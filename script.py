# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import spacy
#json and spacy modules need to be in codebase
##en_core_web_sm model needs to be in codebase as well, and it may have to be downloaded seperately

def text_to_json(text): #I wrote this as a function that takes text and returns a json for now; it can be reformatted in whatever way later
    if (type(text) != str):
        return None 
    entity_dict = {} 
    model = spacy.load("en_core_web_sm") 
    processed_text = model(text)
    for count, entity in enumerate(processed_text.ents):
        if entity.text in entity_dict.keys():
            entity_dict[entity.text] += [count, entity.label_]
        else:
            entity_dict[entity.text] = [count, entity.label_]
    json_object = json.dumps(entity_dict)
    with open("out.json", "w") as outfile:
        outfile.write(json_object)
    return outfile #this outfile will be a json object formatted with entity names accessing entity info
    #right now the only info outputted is what entity it is in the string (ex: 1st) and its classification (name, organization, ect.)
    #we can change this later based on how we want this to integrate with the rest of our code