import numpy as np
from prediction import Prediction

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
# disease_weights  = predicter.predict(input_symptoms)
# disease_weights = np.fromiter(disease_weights.values(), dtype=float).T

symptomp_to_disease_weights = np.zeros((len(disease_names), 132))
for i in range(132):
    temp = np.zeros((132,1))
    # set ith symptom to 1
    temp[i] = 1.
    # isolate disease and symptom weights
    disease_weights = predicter.predict(temp)
    disease_weights = np.fromiter(disease_weights.values(), dtype=float).T
    symptomp_to_disease_weights[:, i] = disease_weights

np.savetxt('symptomp_to_disease_weights.csv', symptomp_to_disease_weights)