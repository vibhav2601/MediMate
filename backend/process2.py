from headers_diseases import headers as headers1
from headers_measures import headers as headers2
import openai
import pandas as pd
import numpy as np
import os
import json


os.environ["OPENAI_API_KEY"] = "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"
# openai.api_key = os.environ["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"]

# write code to connect each header1 with header2

client = openai.OpenAI()
def get_relevance(disease, measure):
    
    response_text = client.chat.completions.create(
      model="gpt-4",
      messages=[
          {"role": "user", "content": f"Rate the importance of {measure} for managing or preventing {disease} on a scale from 0 to 1. Only give me the decimal value. For example, 0.5."}
          ],
      max_tokens=60,
      # temperature=0.0
    )
    response_text = str(response_text)


    return response_text

def parse(response_text):
   # Find the index of "content='"
    start_index = response_text.find("content='") + len("content='")

    # Find the index of the closing single quote after the content
    end_index = response_text.find("'", start_index)

    # Extract the numeric value as a substring
    content_numeric = response_text[start_index:end_index]

    return content_numeric
    
# client = openai.OpenAI()

# response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
#   ]
# )
# print(response)
# stream = client.chat.completions.create(
#     model="gpt-4",
#     messages=[{"role": "user", "content": "Say this is a test"}],
#     stream=True,
# )
    # try:
    #     # Extract the first line of the response and parse the relevance as a float
    #     relevance = float(response.choices[0].text.strip().split('\n')[0])
    # except ValueError:
    #     # If parsing fails, set relevance to a default value (e.g., 0.1)
    #     relevance = 0.1
    # return response
# data = np.zeros((len(headers1), len(headers2)))
# for indx1, i in enumerate(headers1):
#     for indx2, j in enumerate(headers2):
#         # use OPENAI to figure out a weight of importance between [0,1.0] for each pair of headers
#         print(i, j)
#         response = get_relevance(i, j)
#         parsed = parse(response)
#         try:
#           data[indx1, indx2] = parsed
#         except:
#           data[indx1, indx2] = -1
#           print(response, parsed)

# np.save('disease_measure_weights.npy', data)

data = np.load('disease_measure_weights.npy')
np.savetxt("disease_measure_weights.csv", data, delimiter=",")
