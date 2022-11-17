from doctest import OutputChecker
import json
from flask import Flask, request, jsonify, render_template
from backend import ml_pipeline


app = Flask(__name__)


# global variable to load models just once
MODEL_DICT = ml_pipeline.get_loaded_model_dict()

@app.route('/')
def home_page():
    example_embed='This string is from python'
    return render_template('index.html', embed=example_embed)

@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Python'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

@app.route('/conceptmap', methods=['POST'])
def get_triples_from_ml_backend():
    input_text_dict = request.get_json(force=True)
    triples = ml_pipeline.get_triples(input_text_dict['text'], MODEL_DICT)
    print('\n\n\n')
    print('##########################################################')
    print(len(triples))
    print('##########################################################')
    print('\n\n\n')
    return jsonify(triples)

#Run the app:
if __name__ == "__main__":
     app.debug = True
     app.run()