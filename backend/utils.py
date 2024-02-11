import pandas as pd
import numpy as np
import scipy.stats as stats
from prediction import Prediction
from process3 import predict_insurance_plan

def get_disease_indices(disease_list):
    disease_list = reformat_strings(disease_list)
    data = pd.read_csv('datasets/Disease Prediction ML/training.csv')
    data = data.drop('prognosis', axis=1)
    disease_data = data.columns.tolist()
    disease_to_index = {}
    
    for disease in disease_list:
        disease_to_index[disease] = disease_data.index(disease)

    return disease_to_index


def map_index_to_intensity(disease_to_intensity, disease_to_index):
    index_to_intensity = {}
    for disease in disease_to_intensity:
        formatted_disease = '_'.join(disease.split())
        formatted_disease
        index_to_intensity[disease_to_index[formatted_disease]] = disease_to_intensity[disease]
    
    return index_to_intensity

def reformat_strings(unformatted_list):
    formatted_list = []
    for item in unformatted_list:
        unformatted_item = item.split()
        formatted_item = '_'.join(unformatted_item)
        formatted_list.append(formatted_item)
    
    return formatted_list

def swap_disease_with_index(disease_list, disease_to_intensity):
    disease_to_index = get_disease_indices(disease_list)
    index_to_intensity = map_index_to_intensity(disease_to_intensity, disease_to_index)
    return index_to_intensity

def predict_diseases(symptom_intensity, history):
    input_symptoms = np.zeros((132, 1))
    for index, intensity in symptom_intensity.items():
        input_symptoms[index] = (intensity / 5)
    predicter = Prediction()
    prediction = predicter.predict(input_symptoms, history)
    return sort_prediction(prediction)

def sort_prediction(predictions):
    disease_prone_list = sorted(predictions.items(), key=lambda x: x[1], reverse=True)
    sorted_predictions = {}
    for disease, proneness in disease_prone_list:
        sorted_predictions[disease] = proneness
    return sorted_predictions

def predict_insurance_plans(disease_weights):
    disease_weights = np.fromiter(disease_weights.values(), dtype=float).T
    sorted_insurance_plans, sorted_probs, sorted_indices = predict_insurance_plan(disease_weights)
    return sorted_insurance_plans, sorted_probs, sorted_indices

def normalize_insurance_predictions(insurance_plans, probs, n=20):
    '''
    There is no normalization right now becuase for some reason the probs are coming out pretty nice.
    '''
    valid_indices = np.where(probs > 0)[0]
    # valid_indices = valid_indices[0:n]
    probs = probs[valid_indices]
    # print("valid indices", valid_indices)
    # print(probs)
    insurance_plans = insurance_plans[valid_indices]
    # print("insurance plans", np.argsort(insurance_plans))
    ###
    mean_score = np.mean(probs)
    std_dev = np.std(probs)
    normalized_scores = ((np.array(probs) - mean_score) / std_dev)
    normalized_scores = stats.norm.cdf(normalized_scores) * 100
    ###
    # normalized_scores = probs
    # print(normalized_scores)
    insurance_match = {}
    for i in range(len(insurance_plans)):
        insurance_match[normalized_scores[i]] = insurance_plans[i]
    # print("insurance match", insurance_match)
    return insurance_match

def top_insurance_matches(insurance_matches, n=5):
    top_matches = {}
    insurance_matches_list = sorted(insurance_matches.items(), reverse=True)
    # print(insurance_matches_list)
    for i in range(n):
        match_percent, insurance_name = insurance_matches_list[i]
        top_matches[i] = insurance_name, match_percent
    return top_matches

# def count_bad_data():
#     count = 0
#     data = pd.read_csv('datasets/Disease Prediction ML/training.csv')
#     data = data.drop('prognosis', axis=1)
#     disease_data = data.columns.tolist()
#     bad_data = []
#     for disease in disease_data:
#         if len(disease.split()) > 1:
#             count += 1
#             bad_data.append(disease)
#     return count, bad_data


# print(count_bad_data())