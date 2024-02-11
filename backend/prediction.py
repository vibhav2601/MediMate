from joblib import dump, load
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

class Prediction:
    # input_symptoms = np.zeros((132, 1))  # Ensure this array has the same number of elements as your features
    disease_names = ['(vertigo) Paroymsal  Positional Vertigo','AIDS','Acne', 'Alcoholic hepatitis','Allergy','Arthritis','Bronchial Asthma','Cervical spondylosis','Chicken pox','Chronic cholestasis','Common Cold','Dengue','Diabetes','Dimorphic hemmorhoids(piles)','Drug Reaction','Fungal infection','GERD','Gastroenteritis','Heart attack','Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Hypertension','Hyperthyroidism','Hypoglycemia','Hypothyroidism','Impetigo','Jaundice','Malaria','Migraine','Osteoarthritis','Paralysis (brain hemorrhage)','Peptic ulcer diseae','Pneumonia','Psoriasis','Tuberculosis','Typhoid','Urinary tract infection','Varicose veins','hepatitis A']
    predictor = load('symptoms_to_disease.joblib')
    disease_risk_weights = {
        'Hyperthyroidism': 0.3,
        'Arthritis': 0.25,
        'Osteoarthritis': 0.25,
        'Hypothyroidism': 0.3,
        'Cervical Spondylosis': 0.2,
        'Migraine': 0.4,
        'Hypertension': 0.35,
        'Bronchial Asthma': 0.4,
        'Diabetes': 0.3,  # This is a generalized weight; differentiate if necessary.
    }
    def predict(self, input, history):
        # encoder = LabelEncoder()
        
        # input_symptoms_df = pd.DataFrame(input, columns= disease_names)
        probs = self.predictor.predict_proba(input.T)[0]
        # disease_names = encoder.inverse_transform(np.arange(len(encoder.classes_)))
        # sorted_indices = np.argsort(probs[0])[::-1]
        # sorted_diseases = self.disease_names[sorted_indices]
        # sorted_probs = probs[sorted_indices]
        # print("history", history)
        ret = {}
        for disease, prob in zip(self.disease_names, probs):
            ret[disease] = prob
        # print("before bump", ret)
        for disease in history:
            if disease in self.disease_risk_weights.keys():
                ret[disease] = min(1.0, ret[disease] + self.disease_risk_weights[disease])
        # print("after bump", ret)
        return ret
    
    def get_feature_importance(self):
        return self.predictor.feature_importances_


# input_symptoms = np.zeros((132, 1))
# input_symptoms[0] = 1.
# input_symptoms[1] = 0.6
# input_symptoms[2] = 1.
# input_symptoms[5] = 1.

# predicter = Prediction()
# print(predicter.predict(input_symptoms))