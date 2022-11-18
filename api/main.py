from fastapi import FastAPI

app = FastAPI()


"""@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}"""

import requests
import json
import pandas as pd
import csv


response_API = requests.get('https://data.ademe.fr/data-fair/api/v1/datasets/elecdom-donnees-de-consommation-annuelle/lines?size=10000&page=1&q_mode=complete&finalizedAt=2022-03-04T08:11:52.428Z&format=csv')


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath) as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


print(response_API.status_code)
data = response_API.text

f = open('temp.csv','w')
f.write(data)
f.close()
f = csv_to_json('temp.csv','jsontest')
print(data)
json_data = json.dumps(data)
parse_json = json.loads(json_data)

a=1