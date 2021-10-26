import sys
import datetime
import json
import pprint

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

def save_json(data, filename):
    with open(filename, "w", encoding='utf8') as file_writer:
        json.dump(data, file_writer, ensure_ascii=False, indent=2)

def filter_consolidated_data():
    data = open_json(params.LOCAL_PATH_CONSOLIDATED)
    num_total = len(data["marches"])
    print(set([m.get("_type") for m in data["marches"]]))
    data['marches'] = [m for m in data["marches"] if m.get("_type").lower()=='marché']
    num_filtered = len(data["marches"])
    print(num_total, ">", num_filtered)
    print(set([m.get("nature") for m in data["marches"]]))
    save_json(data, params.LOCAL_PATH_CONSOLIDATED_FILTERED)

def validate_consolidated_data_against_schema():
    schema = open_json(params.LOCAL_PATH_CONSOLIDATED_SCHEMA)
    #data = open_json(params.LOCAL_PATH_CONSOLIDATED)
    data = open_json("./data/decp_short.json")
    jsonschema.validate(data, schema)

def full_validate_consolidated_data_against_schema():
    schema = open_json(params.LOCAL_PATH_CONSOLIDATED_SCHEMA)
    #data = open_json(params.LOCAL_PATH_CONSOLIDATED)
    data = open_json("./data/decp_short.json")
    columns= []
    for m in data.get("marches"):
        print(m.keys())
        columns += list(m.keys())
        if isinstance(m, dict):
            for k in m.keys():
                columns.append(f"{m}.{k}")
    columns = set(columns)
    #print(columns)
    num_uid = [m.get("uid") for m in data.get("marches")]
    num_total = len(num_uid)
    num_unique = len(set(num_uid))
    if num_total != num_unique:
        print("Warning : duplicated uids")
    validator = jsonschema.Draft7Validator(schema)
    filter_keep_any_of = 0
    errors_any_of = validator.iter_errors(data)
    errors = {}
    for counter, error in enumerate(errors_any_of):
        instance_uid = error.instance.get("uid")
        instance_suberrors = []
        if error.context is None or len(error.context)==0:
            print("Warning : hidden errors")
        else:
            for subcounter, suberror in enumerate(error.context):
                if suberror.schema_path[0] == filter_keep_any_of:
                    if len(suberror.context)>0:
                        print("Warning : hidden suberrors")
                    error_details = {
                        "message":suberror.message,
                        "validator":suberror.validator,
                    }
                    instance_suberrors.append(error_details)
        errors[instance_uid] = instance_suberrors
    num_invalid_entries = len(errors)
    num_valid_entries = num_total - num_invalid_entries
    share_valid_entries = num_valid_entries / num_total
    share_valid_entries = round(share_valid_entries, 2)
    results = {
        "num_invalid_entries":num_invalid_entries,
        "num_valid_entries":num_valid_entries,
        "share_valid_entries":share_valid_entries,
        "details_per_uid":errors
    }
    print(results)
