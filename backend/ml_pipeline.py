import spacy
import itertools
import opennre
from transformers import pipeline
from backend.text_summarization.text_summarizer import text_summarizer_inference
from backend.NER.extract_entities import get_entities
from backend.relationship_extraction.relation_ext_code import extract_relationship
from pprint import pprint


def get_loaded_model_dict():
    '''
    Loading all the models.
    This function should be called just once in the main script
    '''
    loaded_model_dict = {
        'sentence_model': None,
        'summarizer': None,
        'ner_model': None,
        'relation_model': None
    }
    # sentence splittin_model
    try:
        loaded_model_dict['sentence_model'] = spacy.load('en_core_web_sm')
        print('\n')
        print('Sentence model loaded ')
        print('\n')
    except Exception as e:
        print(e)
        print('Sentence model not loaded properly')
    
    # summarizer model
    try:
        loaded_model_dict['summarizer'] = pipeline("summarization")
        print('\n')
        print('Summarizer model loaded successfully')
        print('\n')
    except Exception as e:
        print(e)
        print('Summarizer model not loaded successfully')

    # ner model 
    try:
        loaded_model_dict['ner_model'] = spacy.load('en_core_web_sm')
        print('\n')
        print('NER model loaded successfully')
        print('\n')
    except Exception as e:
        print(e)
        print('NER model not loaded successfully')

    # relationship model
    try:
        loaded_model_dict['relation_model'] = opennre.get_model('wiki80_cnn_softmax') 
        print('\n')
        print('Relationship Model was loaded successfully')
        print('\n')
    except Exception as e:
        print(e)
        print('Relationship Model was not loaded successfully')

    return loaded_model_dict



def get_sentences(text, model):
    return [t.text for t in model(text).sents]


def prepare_data_for_relation(ner_output):
    relationship_data = []
    for sent_obj in ner_output:
        sentence_text = sent_obj['text']
        sentence_entities = sent_obj['entities']
        for i, j in itertools.combinations(range(len(sentence_entities)), 2):
            relationship_data.append(
                {
                    'text': sentence_text,
                    'h': {
                        'pos': (
                            sentence_entities[i]['entity_start_char'],
                            sentence_entities[i]['entity_end_char']
                        )
                    },
                    't': {
                        'pos': (
                            sentence_entities[j]['entity_start_char'],
                            sentence_entities[j]['entity_end_char']
                        )
                    },
                }
            )
    return relationship_data


def get_triples(text, model_dict):
    # summarize
    summarized_text = text_summarizer_inference(
        text, model_dict['summarizer']
    )
    # split sentences
    sentences  = get_sentences(
        text, model_dict['sentence_model']
    )
    print(len(sentences))
    pprint(sentences)
    # ner step
    # will run for every sentence and get the entities and text
    ner_step_output = []
    for sentence in sentences:
        sent_dict_obj = get_entities(sentence, model_dict['ner_model'])
        ner_step_output.append(sent_dict_obj)

    # relationships
    ## preparing relationship data
    relationship_input_data = prepare_data_for_relation(
        ner_step_output
    )
    for rel_dict in relationship_input_data:
        rel_model_output = extract_relationship(
            rel_dict, model_dict['relation_model']
        )
        rel_dict['relation'] = rel_model_output

    # generate triples
    triples = []
    for rel_dict in relationship_input_data:
        sent_text = rel_dict['text']
        head_ent = sent_text[rel_dict['h']['pos'][0]: rel_dict['h']['pos'][1]]
        child_ent = sent_text[rel_dict['t']['pos'][0]: rel_dict['t']['pos'][1]]
        relation = rel_dict['relation']
        triples.append(
            {
                'head_ent': head_ent,
                'child_ent': child_ent,
                'relationship': relation,
                'sentence': sent_text
            }
        )
    return triples


if __name__ == "__main__":
    text = "Paris is the capital and most populous city of France, with an estimated population of 2,175,601 residents as of 2018, in an area of more than 105 square kilometres (41 square miles). The City of Paris is the centre and seat of government of the region and province of Île-de-France, or Paris Region, which has an estimated population of 12,174,880, or about 18 percent of the population of France as of 2017."
    model_dict = get_loaded_model_dict()
    triples = get_triples(text, model_dict)
    pprint(triples)