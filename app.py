import glob
from flask import Flask
from flask_restful import Api, Resource, reqparse

from core.corpus import Corpus
from core.model import Model

app = Flask(__name__)
api = Api(app)


@app.before_first_request
def initialisation():
    global beta, GLOBAL_REF_MODEL
    dataset_path = '.\\dataset\\*.txt'
    models = []
    for file_name in glob.glob(dataset_path):
        models.append(Corpus(path_to_corpus=file_name).freq_result)
    m = Model(*models)
    beta = m.beta
    GLOBAL_REF_MODEL = m.global_ref_model


class Classification(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('speech',
                        type=str,
                        required=True,
                        help='This field cannot be left blank!'
                        )

    def post(self):
        data = Classification.parser.parse_args()
        speech = data['speech']
        with open(file='.\\text.txt', encoding="utf-8") as file:
            txt = file.read()

        txt = txt + ' ' + speech + ' '
        speaker = Model(Corpus(corpus=txt).freq_result, GLOBAL_REF_MODEL)
        phi = speaker.beta

        if phi >= beta:
            return {'classification': 'Pathological'}
        else:
            return {'classification': 'Healthy'}


api.add_resource(Classification, '/classification')

if __name__ == '__main__':
    app.run()
