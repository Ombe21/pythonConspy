from fastapi import FastAPI
import csv
from fastapi import UploadFile

app = FastAPI()

import requests
import json
import pandas as pd
import csv
import os

response_API = requests.get('https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv')


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


"""
def csv_to_json(csvFilePath):
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
    jsonString = json.dumps(jsonArray)
    return json.loads(jsonString)
"""

print(response_API.status_code)
data = response_API.text

f = open('temp.csv', 'a')

# f.write(data)  #this create the database
f.close()

data = csv_to_json('temp.csv', 'temp.json')

# print(data['wind_cons_change_pct'])

# print(data)

a = 1


@app.post("/add/csv")
async def addToDbCsv(toAddCsv: UploadFile):
    line = toAddCsv.file.readline()
    while (line != ''):
        f = open('temp.csv', 'a')
        f.write(line)
        line = toAddCsv.file.readline()


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
