from fastapi import FastAPI
import csv
from fastapi import UploadFile


import uvicorn
from fastapi import FastAPI

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

f = open('api/temp.csv', 'a')

# f.write(data)  #this create the database
f.close()

data = csv_to_json('api/temp.csv', 'api/temp.json')

# print(data['wind_cons_change_pct'])


a = 1


@app.post("/add/csv")
async def addToDbCsv(toAddCsv: UploadFile):
    line = toAddCsv.file.readline()
    f = open('api/temp.csv', 'a')
    while (line != ''):
        f.write(line)
        line = toAddCsv.file.readline()
    f.close()


@app.get("/")
async def getDataJson():
    csv_to_json('api/temp.csv', 'api/data.json')
    f = open('api/data.json')
    lines = f.readlines()
    f.close()
    return lines



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
