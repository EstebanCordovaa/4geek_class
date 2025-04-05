import logging
from flask import Flask, request, jsonify
from pickle import load as pickle_load

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

api = Flask(__name__)

with open('/workspaces/4geek_class/models/model_maternal_risk.pkl', 'rb') as file:
    model = pickle_load(file)

@api.route('/api', methods=['POST'])
def predict_maternal_risk():
    data = request.get_json()
    age = data.get('age')
    systolicbp = data.get('systolicbp')
    diastolicbp = data.get('diastolicbp')
    bs = data.get('bs')
    bodytemp = data.get('bodytemp')
    heartrate = data.get('heartrate')

    try:
        prediction = model['model'].predict([[age, systolicbp, diastolicbp, bs, bodytemp, heartrate]])
        logger.info('Prediction made successfully')
    except Exception as e:
        logger.error(f'Ocurrió un error: {e}')
        return jsonify({'error': 'No se pudo realizar la predicción'}), 400

    class_predict = model['target_classes'][int(prediction[0])]
    return jsonify({'prediction': class_predict})

if __name__ == '__main__':
    api.run(debug=True)