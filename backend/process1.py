import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from joblib import dump, load

# symptoms_to_disease = np.genfromtxt('datasets/Disease Prediction ML/data_symptoms_to_disease.csv', delimiter=',')

data = pd.read_csv('datasets/Disease Prediction ML/training.csv')

# Load the dataset (already done in previous steps)

# Separate features and target variable
X = data.drop('prognosis', axis=1)
y = data['prognosis']

# Encode the target variable
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Initialize and train the Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
dump(clf, 'symptoms_to_disease.joblib') 

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

input_symptoms = np.zeros((132, 1))  # Ensure this array has the same number of elements as your features
input_symptoms[0] = 1.
input_symptoms[1] = 0.6
input_symptoms[2] = 1.
input_symptoms[5] = 1.

# Predict the probabilities for each class
probs = clf.predict_proba(input_symptoms.T)

# print(sorted(probs))


# print("\nSorted Diseases by Probability:")
# for disease, prob in zip(sorted_diseases, sorted_probs):
#     print(f"{disease}: {prob:.4f}")
# Get the disease names from the encoder
disease_names = encoder.inverse_transform(np.arange(len(encoder.classes_)))
print(disease_names)


sorted_indices = np.argsort(probs[0])[::-1]  # Sort probabilities in descending order
sorted_diseases = disease_names[sorted_indices]
sorted_probs = probs[0][sorted_indices]

# Display the probabilities along with disease names
# for disease, prob in zip(sorted_diseases, sorted_probs):
#     print(f"{disease}: {prob:.4f}")

