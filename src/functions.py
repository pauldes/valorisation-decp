import sys
import datetime
import json

import requests
import pandas
import jsonschema
import streamlit.cli as cli

from src import params

def download_augmented_data_to_disk(n_rows=None):
    if n_rows is not None:
        url_prefix = f"&rows={int(n_rows)}"
    else:
        url_prefix = ""
    url = params.URL_AUGMENTED + url_prefix
    response = requests.get(url, allow_redirects=True, verify=True, stream=True)
    with open(params.LOCAL_PATH_AUGMENTED, 'wb') as file_writer:
        for counter, chunk in enumerate(response.iter_content(chunk_size=4096)):
            file_writer.write(chunk)
            print(".", end='', flush=True)
    response = requests.get(url, stream = True)

def download_consolidated_data_to_disk():
    url = params.URL_CONSOLIDATED
    response = requests.get(url, allow_redirects=True, verify=True, stream=True)
    with open(params.LOCAL_PATH_CONSOLIDATED, 'wb') as file_writer:
        for counter, chunk in enumerate(response.iter_content(chunk_size=4096)):
            file_writer.write(chunk)
            print(".", end='', flush=True)
    response = requests.get(url, stream = True)

def download_consolidated_data_schema_to_disk():
    url = params.URL_CONSOLIDATED_SCHEMA
    r = requests.get(url, allow_redirects=True, verify=True)
    with open(params.LOCAL_PATH_CONSOLIDATED_SCHEMA, 'wb') as file_writer:
        file_writer.write(r.content)

def load_data_from_disk(n_rows=None):
    return pandas.read_csv(params.LOCAL_PATH_AUGMENTED, sep=";", index_col="id", encoding="utf8", header=0, nrows=n_rows, dtype=params.DATASET_TYPES)

def print_data_shape_and_sample(n_rows=None):
    dataset = load_data_from_disk(n_rows)
    print(dataset.sample(5))
    print(dataset.shape)

def run_web_app():
    sys.argv = ['0','run','./src/webapp.py']
    cli.main()

def get_current_day():
    return datetime.datetime.now().day

def get_current_month():
    return datetime.datetime.now().month

def get_current_year():
    return datetime.datetime.now().year

def open_json(filename):
    return json.loads(open(filename, 'rb').read().decode('utf-8'))

def validate_consolidated_data_against_schema():
    schema = open_json(params.LOCAL_PATH_CONSOLIDATED_SCHEMA)
    #data = open_json(params.LOCAL_PATH_CONSOLIDATED)
    data = open_json("./data/decp_short.json")
    jsonschema.validate(data, schema)

def print_data():
    data = open_json(params.LOCAL_PATH_CONSOLIDATED)
    num_total = len(data["marches"])
    types = set([m.get("_type") for m in data["marches"]])
    natures = set([m.get("nature") for m in data["marches"]])
    print(types)
    print(natures)
    #num_marches = len([m for m in data["marches"] if ])
    print(num_total)

def full_validate_consolidated_data_against_schema():
    schema = open_json(params.LOCAL_PATH_CONSOLIDATED_SCHEMA)
    #data = open_json(params.LOCAL_PATH_CONSOLIDATED)
    data = open_json("./data/decp_short.json")
    validator = jsonschema.Draft7Validator(schema)
    errors = validator.iter_errors(data)
    print("\n\n")
    #print(schema)
    for counter, error in enumerate(errors):
        print(f"\n===== ERROR N°{counter} :\n")
        if error.context is None or len(error.context)==0:
            print("MESSAGE:\n", error.message)
            print("CONTEXT:\n", error.context)
            print("CAUSE:\n", error.cause)
            print("VALIDATOR:\n", error.validator)
            print("VALIDATOR_VALUE:\n", error.validator_value)
            print("SCHEMA_PATH:\n", error.schema_path)
            print("PARENT:\n", error.schema_path)
            print("INSTANCE:\n", error.instance)
            print(len(error.context))
        else:
            for subcounter, suberror in enumerate(error.context):
                print(f"\n===== SUB-ERROR N°{subcounter} :\n")
                print("MESSAGE:\n", suberror.message)
                print("CONTEXT:\n", suberror.context)
                print("CAUSE:\n", suberror.cause)
                print("VALIDATOR:\n", suberror.validator)
                print("VALIDATOR_VALUE:\n", suberror.validator_value)
                print("SCHEMA_PATH:\n", suberror.schema_path)
                print("ABSOLUTE SCHEMA PATH:\n", suberror.absolute_schema_path)
                print("PARENT:\n", suberror.schema_path)
                print("INSTANCE:\n", suberror.instance)
                print(len(suberror.context))
