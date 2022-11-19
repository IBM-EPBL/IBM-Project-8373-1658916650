# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 10:58:46 2022

"""
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "gh2T-jLLrC0Ers17AZJWqkLXBMrFurJExV5ix8D9hNd6"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
print("mltoken",mltoken)
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["GRE Score","TOEFL Score","University Rating","SOP","LOR","CGPA","Research"]], "values": [[298 , 98  ,   5  ,   1.5 ,   2.5 ,   7.5,   0]]}]}

response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/245540f8-1433-430d-872f-725beceb8377/predictions?version=2022-06-18', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
predictions=response_scoring.json()
print(predictions['predictions'][0]['values'][0][1])