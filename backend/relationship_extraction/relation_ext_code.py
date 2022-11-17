import opennre


def extract_relationship(text_json, model):
    '''
    Used OpenNRE model with 80 classes for relationship.
    '''
    model_output = model.infer(text_json)
    relation = model_output[0]
    return relation


if __name__ == "__main__":
    model = opennre.get_model('wiki80_cnn_softmax')
    input_data = {
        'text': 'He was the son of Máel Dúin mac Máele Fithrich, and grandson of the high king Áed Uaridnach (died 612).', 
        'h': {'pos': (18, 46)}, 
        't': {'pos': (78, 91)}
    }
    relation = extract_relationship(input_data, model)
    print(
        'Relationship between {} and {} is {}'.format(
            input_data['text'][input_data['h']['pos'][0]: input_data['h']['pos'][1]],
            input_data['text'][input_data['t']['pos'][0]: input_data['t']['pos'][1]],
            relation
        )
    )
