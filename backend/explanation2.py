import pandas as pd
from joblib import dump, load
import numpy as np
from headers_measures import headers as measure_names
from headers_diseases import headers as disease_names

#  assume u get the diseases as an input
class Explanation:
    # takes top 5 diseases as input
    all_measures_needed = np.zeros((47,1))
    disease_measure_weights = np.load('disease_measure_weights.npy')
    def disease_to_checks(self, input):
        # input is the disease index
        # for i,j in enumerate(input):
            # i is the index of the ith disease
            # j is the wiehgt of the disease
        i, j = input
        row_of_measures = self.disease_measure_weights[i] * j
        row_of_measures = row_of_measures.reshape((47,1))
            # indices_of_largest = np.argsort(row_of_measures)[-3:]
            # ret = self.check_to_insurance(indices_of_largest)
        # ret = np.argsort(row_of_measures)[-3:]
            # print(i, self.disease_measure_weights[i], row_of_measures)
            # print(row_of_measures)
            # indices_of_max_measures = np.argsort(row_array)[-5:] 
            # self.all_measures_needed.append(row_of_measures)
        return row_of_measures
    def check_to_insurance(self, input, checks):
        # input is the insurance plan in question
        insurance_plans = pd.read_csv('datasets/US Healthcare Data/Star_rating_fall_master data.csv', encoding='cp1252', skiprows=1, header=0)
        insurance_providers = insurance_plans.iloc[:, :3]
        insurance_providers.columns = ['Contract Name', 'Organization', 'Parent Group']
        insurance_plans = insurance_plans.iloc[:, 3:]
        insurance_plans = insurance_plans.to_numpy()
        # insurance_plans[input] is the insurance plan in question
        checks_covered = insurance_plans[input]
        checks_covered = checks_covered.reshape((47,1))
        res = checks_covered * checks
        res = res.reshape((47))
        # print(res)
        sorted_indices = np.argsort(res)[-3:]
        # print(res.shape)
        # print(res)
        # print(checks_covered.shape)
        return sorted_indices, res[sorted_indices]
    def get_explanations(self, diseases_input, insurance_plans_list):
        temp = np.zeros((41))
        for x in diseases_input.keys():
            temp[disease_names.index(x)] = diseases_input[x]
        diseases_input = temp
        important_measures_all = {}
        top_5_diseases = np.argsort(diseases_input)[::-1][:5]
        # print(insurance_plans_list)
        for insurance_plan_name in insurance_plans_list:
            important_measures = {}
            # print(list(insurance_providers['Contract Name']))
            insurance_plan = list(insurance_providers['Contract Name']).index(insurance_plan_name)
            for i in top_5_diseases:
                # print("Disease index" ,i, "Disease weight", j)
                j = diseases_input[i]
                measures = self.disease_to_checks((i, j))
                # print(measures.shape)
                indices_of_top_checks, top_checks_covered = self.check_to_insurance(insurance_plan, measures)
                #disease prob * disease_to_measure * measure_to_insurance
                # print(top_checks_covered)
                coverage = np.array([insurance_plans[insurance_plan][i] for i in indices_of_top_checks])
                coverage = np.abs(coverage)
                for coverage_idx, index in enumerate(indices_of_top_checks):
                    key = measure_names[index][5:]
                    if key not in important_measures.keys():
                        important_measures[key] = (set(), coverage[coverage_idx])
                    important_measures[key][0].add(disease_names[i])
                # print('coverage', coverage)
            # print(insurance_providers['Contract Name'][insurance_plan])
            important_measures_all[insurance_providers['Contract Name'][insurance_plan]] = important_measures
            for k in important_measures_all.keys():
                for j in important_measures_all[k].keys():
                    # print("important_measures_all", important_measures_all)
                    important_measures_all[k][j] = (list(important_measures_all[k][j][0]), important_measures_all[k][j][1])
        return important_measures_all
a = Explanation()
diseases_input = np.zeros((41))
diseases_input[0] = 1
diseases_input[1] = 0.6
diseases_input[2] = 0.4
diseases_input[3] = 0.8
# top_5_diseases = np.argsort(diseases_input)[::-1][:5]
# print(top_5_diseases)

insurance_plans = pd.read_csv('datasets/US Healthcare Data/Star_rating_fall_master data.csv', encoding='cp1252', skiprows=1, header=0)
insurance_providers = insurance_plans.iloc[:, :3]
insurance_providers.columns = ['Contract Name', 'Organization', 'Parent Group']
insurance_plans = insurance_plans.iloc[:, 3:]
insurance_plans = insurance_plans.to_numpy()
# we know the insurance plan in question
insurance_plans_list = [1,2,9,3]


# print(a.get_explanations(diseases_input, insurance_plans_list))