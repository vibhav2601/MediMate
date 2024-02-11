import pandas as pd
from joblib import dump, load
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.metrics import make_scorer, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from prediction import Prediction
from process3 import predict_insurance_plan, load_insurance_plans

from headers_symptoms import headers as symptoms
from headers_measures import headers as measures

measures = np.array(measures)

input_symptoms = np.zeros((132, 1))  # Ensure this array has the same number of elements as your features
input_symptoms[0] = 1.
input_symptoms[1] = 0.6
input_symptoms[2] = 1.
input_symptoms[5] = 1.

disease_names = ['(vertigo) Paroymsal  Positional Vertigo','AIDS','Acne', 'Alcoholic hepatitis','Allergy','Arthritis','Bronchial Asthma','Cervical spondylosis','Chicken pox','Chronic cholestasis','Common Cold','Dengue','Diabetes','Dimorphic hemmorhoids(piles)','Drug Reaction','Fungal infection','GERD','Gastroenteritis','Heart attack','Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Hypertension','Hyperthyroidism','Hypoglycemia','Hypothyroidism','Impetigo','Jaundice','Malaria','Migraine','Osteoarthritis','Paralysis (brain hemorrhage)','Peptic ulcer diseae','Pneumonia','Psoriasis','Tuberculosis','Typhoid','Urinary tract infection','Varicose veins','hepatitis A']
disease_names = np.array(disease_names)


# data = pd.read_csv('datasets/Disease Prediction ML/training.csv')

# # Separate features and target variable
# X = data.drop('prognosis', axis=1)
# y = data['prognosis']

# encoder = LabelEncoder()
# y_encoded = encoder.fit_transform(y)

# X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# symptoms_to_disease = load('symptoms_to_disease.joblib')

predicter = Prediction()
disease_weights  = predicter.predict(input_symptoms)
disease_weights = np.fromiter(disease_weights.values(), dtype=float).T
insurance_providers, insurance_plans = load_insurance_plans()
# print(len(measures), insurance_plans.shape)

symptomp_to_disease_weights = np.loadtxt('symptomp_to_disease_weights.csv')
disease_measure_weights = np.load('disease_measure_weights.npy')

assert (symptomp_to_disease_weights.shape == (len(disease_names), 132))

top_5_disease_idx = np.argsort(disease_weights)[::-1][:5]
top_5_disease_names = disease_names[top_5_disease_idx]

symptomps_to_plans = symptomp_to_disease_weights.T @ disease_measure_weights @ insurance_plans
# TODO: problem, len(symptoms) == 133 but we've been using 132 everywhere
assert(symptomps_to_plans.shape[0] == 132)
disease_to_plans = disease_measure_weights @ insurance_plans
assert(disease_to_plans.shape
       [0] == len(disease_names))
sorted_insurance_plans, sorted_probs, sorted_indices = predict_insurance_plan(input_symptoms)
# print(symptoms_to_disease.shape, len(disease_names))
for disease in top_5_disease_idx:
    top_3_symptoms = symptoms[np.argsort(symptomp_to_disease_weights[disease])[::-1][:3]]
    top_3_measures = measures[np.argsort(disease_measure_weights[disease])[::-1][:3]]
    # print(disease_names[disease], top_3_symptoms, top_3_measures)