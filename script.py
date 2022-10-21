# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import spacy

def text_to_json(text):
    if (type(text) != str):
        return None
    entity_dict = {}
    model = spacy.load("en_core_web_sm")
    processed_text = model(text)
    for count, entity in enumerate(processed_text.ents):
        if entity.name in entity_dict.keys():
            entity_dict[entity.name] += [count, entity.label_]
        else:
            entity_dict[entity.name] = [count, entity.label_]
    json_object = json.dumps(entity_dict)
    with open("out.json", "w") as outfile:
        outfile.write(json_object)
    return outfile