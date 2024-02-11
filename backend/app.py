from flask import Flask, jsonify, request
from mockdata import insurance_plans, diseases
from flask_cors import CORS
from utils import swap_disease_with_index, predict_diseases, predict_insurance_plans, normalize_insurance_predictions, top_insurance_matches
from mockdata import recieve_data
from explanation2 import Explanation

app = Flask(__name__)

CORS(app)

# Endpoint to get all tasks
@app.route('/insurance', methods=['GET'])
def get_insurance_plans():
    return jsonify({'insurance': insurance_plans})

# Endpoint to get a specific task by ID
@app.route('/diseases', methods=['GET'])
def get_diseases():
    return jsonify({'diseases': diseases})

# Endpoint to create a new task
@app.route('/predict', methods=['POST'])
def predict_diseases_and_insuraces():
    data = request.json

    user_info = {
        "name": data["name"],
        "age": data["age"],
        "location": data["currentLocation"],
        "gender": data["gender"],
        "history": data["familyHistory"],
        "symptoms": data["symptoms"],
        "intensity": data["symptomIntensity"]
    }
    recieve_data(user_info)
    
    # return jsonify({'message': 'Information recorded', 'user info': user_info}), 201

    symptom_intensity = swap_disease_with_index(data["symptoms"], data["symptomIntensity"])
    disease_weights = predict_diseases(symptom_intensity, data['familyHistory'])
    sorted_insurance_plans, sorted_probs, sorted_indices = predict_insurance_plans(disease_weights)
    # print("sorted insurance plans", sorted_insurance_plans)
    temp =list(sorted_insurance_plans[:5])
    print("temp", temp)
    tmp_dic = {}
    for i in range(5):
        tmp_dic[i] = temp[i], sorted_probs[sorted_indices[i]]
    # print("temp", temp)
    # unsorted_insurance_matches = normalize_insurance_predictions(sorted_insurance_plans, sorted_probs)
    # insurance_predictions = top_insurance_matches(unsorted_insurance_matches)
    # print(([(k, v) for k, v in insurance_predictions.items()])[:3])
    insurance_predictions = tmp_dic
    insurance_names = [insurance_predictions[i][0] for i in range(len(insurance_predictions))]
    # print(insurance_predictions)
    a= Explanation()
    see_why = a.get_explanations(disease_weights, insurance_names)
    # print("see why", see_why)
    return jsonify({'message': 'Diseases predicted', 'disease predictions': disease_weights, 'insurance predictions': insurance_predictions, 'see why': see_why}), 201



if __name__ == '__main__':
    app.run(debug=True)
