from fastapi import FastAPI
from sqlalchemy.dialects.postgresql import psycopg2

app = FastAPI()

import requests
import json
import pandas as pd
import csv
import os
import pyodbc


server = 'conspy.cyqm4cgvogvg.eu-west-3.rds.amazonaws.com'
database = 'ConsPy'
username = 'ConsPy'
password = 'JWC616BuObW1boP0gmQL'
port = 5432

# aller sur https://docs.aws.amazon.com/fr_fr/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Connecting.Python.html


response_API = requests.get('https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv')


def csv_to_json(csvFilePath)->json:
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



print(response_API.status_code)
data = response_API.text

f = open('temp.csv','w')
f.write(data)
f.close()
data = csv_to_json('temp.csv')

print(data)
os.remove('temp.csv')



aaa=1


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}