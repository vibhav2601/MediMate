from headers_diseases import headers as diseases
import numpy as np
import pandas as pd
from prediction import Prediction



# load disease_measure_weights from process2.py
disease_measure_weights = np.load('disease_measure_weights.npy')
assert(len(diseases) == disease_measure_weights.shape[0])

def load_insurance_plans():
    # load insuracnce plans
    insurance_plans = pd.read_csv('datasets/US Healthcare Data/Star_rating_fall_master data.csv', encoding='cp1252', skiprows=1, header=0)
    insurance_providers = insurance_plans.iloc[:, :3]
    insurance_providers.columns = ['Contract Name', 'Organization', 'Parent Group']
    insurance_plans = insurance_plans.iloc[:, 3:]
    insurance_plans = insurance_plans.to_numpy().T
    return insurance_providers, insurance_plans

insurance_providers, insurance_plans = load_insurance_plans()
assert(insurance_plans.shape[0] == disease_measure_weights.shape[1])


input = np.zeros((132, 1))
input[0] = 1.
input[1] = 0.6
input[2] = 1.
input[5] = 1.

def predict_insurance_plan(disease_weights, ifPrint = False):
    predicter = Prediction()
    # disease_weights = np.array(predicter.predict(input_symptoms).values())
    # disease_weights  = predicter.predict(input_symptoms)
    # disease_weights = np.fromiter(disease_weights.values(), dtype=float).T
    # print(disease_weights.shape, disease_measure_weights.shape)
    res = disease_weights @ disease_measure_weights @ insurance_plans
    # print(res)

    # figure out top 5 diseases, using those index into disease_measure_weights to get the relevant checks, then index into insurance plan coverage for those checks


    # diseases * disease_measure_weights * insruance_weights
    # disease_names = encoder.inverse_transform(np.arange(len(encoder.classes_)))
    # print(insurance_providers.head())
    # print('process3.py ', np.argsort(res)[-5:])
    sorted_indices = np.argsort(res)[::-1]
    sorted_insurance_plans = insurance_providers['Contract Name'][sorted_indices]
    sorted_probs = res[sorted_indices]
    # ret = {}
    for plan, prob in zip(sorted_insurance_plans, sorted_probs):
        # ret[disease] = prob
        if ifPrint:
            print(f"{plan} has {prob}")
    return sorted_insurance_plans, sorted_probs, sorted_indices
# print(ret)

# predict_insurance_plan(input)