from prediction import Prediction
import numpy as np


## PROCESS 1
input_symptoms = np.zeros((132, 1))
input_symptoms[0] = 1.
input_symptoms[1] = 0.6
input_symptoms[2] = 1.
input_symptoms[5] = 1.

predicter = Prediction()
print(predicter.predict(input_symptoms))