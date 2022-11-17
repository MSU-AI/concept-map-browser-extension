# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import spacy
# json and spacy modules need to be in codebase
## en_core_web_sm model needs to be in codebase as well, and it may have to be downloaded seperately

def get_entities(text, model):
    '''
    function that takes text and returns a json for now;
    it can be reformatted in whatever way later
    # entities will be a list with start and end char and text of the entity
    '''
    entity_dict = {
        'text': text,
        'entities': []
    } 
    if (type(text) != str):
        return entity_dict
    
    processed_text = model(text)
    for idx, entity in enumerate(processed_text.ents):
        entity_dict['entities'].append(
            {
                'ent_id': idx,
                'entity_text': entity.text,
                'entity_start_char': entity.start_char,
                'entity_end_char': entity.end_char,
                'entity_label': entity.label_
            }
        )
    return entity_dict 


if __name__ == "__main__":
    model = spacy.load("en_core_web_sm") 
    long_text = "Paris is the capital and most populous city of France, with an estimated population of 2,175,601 residents as of 2018, in an area of more than 105 square kilometres (41 square miles). The City of Paris is the centre and seat of government of the region and province of Île-de-France, or Paris Region, which has an estimated population of 12,174,880, or about 18 percent of the population of France as of 2017."
    entities = get_entities(long_text, model)
    print(entities)