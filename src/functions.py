import sys
import datetime
import json
import pprint

import requests
import pandas
import jsonschema
import streamlit.cli as cli

from src import params

def download_augmented_data_to_disk(n_rows:int=None):
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

def load_augmented_data_from_disk(n_rows:int=None):
    return pandas.read_csv(params.LOCAL_PATH_AUGMENTED, sep=";", index_col="id", encoding="utf8", header=0, nrows=n_rows, dtype=params.DATASET_TYPES)

def run_web_app():
    sys.argv = ['0','run','./src/webapp.py']
    cli.main()

def get_current_day():
    return datetime.datetime.now().day

def get_current_month():
    return datetime.datetime.now().month

def get_current_year():
    return datetime.datetime.now().year

def open_json(filename:str):
    with open(filename, 'rb') as file_reader:
        return json.loads(file_reader.read().decode('utf-8'))

def save_json(data:dict, filename:str):
    with open(filename, "w", encoding='utf8') as file_writer:
        json.dump(data, file_writer, ensure_ascii=False, indent=2)

def load_consolidated_data_from_disk():
    return open_json(params.LOCAL_PATH_CONSOLIDATED)

def load_consolidated_data_schema_from_disk():
    return open_json(params.LOCAL_PATH_CONSOLIDATED_SCHEMA)

def load_augmented_data_from_disk(n_rows:int=None):
    return pandas.read_csv(params.LOCAL_PATH_AUGMENTED, sep=";", index_col="id", encoding="utf8", header=0, nrows=n_rows, dtype=params.DATASET_TYPES)

def filter_augmented_data_by_type(augmented_data:dict, type_value:str):
    data = load_consolidated_data_from_disk()
    num_total = len(data["marches"])
    print(set([m.get("_type") for m in data["marches"]]))
    data['marches'] = [m for m in data["marches"] if m.get("_type").lower()==type_value.lower()]
    num_filtered = len(data["marches"])
    print(num_total, ">", num_filtered)
    print(set([m.get("nature") for m in data["marches"]]))
    return data

def save_audit_results_to_disk(results):
    save_json(results, params.LOCAL_PATH_AUDIT_RESULTS)

def load_audit_results_from_disk():
    open_json(params.LOCAL_PATH_AUDIT_RESULTS)

def audit_consolidated_data_quality(n_rows:int=None):
    data = load_consolidated_data_from_disk()
    data = filter_augmented_data_by_type(data, "marché")
    schema = load_consolidated_data_schema_from_disk()
    if n_rows is not None:
        data["marches"] = data["marches"][:n_rows]
    results = validate_consolidated_data_against_schema(data, schema)
    save_audit_results_to_disk(results)

def validate_consolidated_data_against_schema(consolidated_data:dict, consolidated_data_schema:dict, include_details:bool=False):
    """Validate the consolidated data against JSON schema.
    This function makes assumptions on both the data structure and the schema definition:
        - The file has a property 'marches' under which are listed the entries
        - Each entry has a property 'uid'
        - The schema definition includes an 'anyOf' rule where only the first one is of interest (filter_keep_any_of = 0)

    Args:
        consolidated_data (dict): Consolidated DECP data as a dict
        consolidated_data_schema (dict): Schema as a dict
        include_details (bool, optional): Wether to include all errors details in the results. Defaults to False.

    Returns:
        dict: A report with multiple fields
            "num_invalid_entries": Number of invalid entries
            "num_valid_entries": Number of valid entries
            "share_valid_entries": Share of valid entries
            "num_errors_per_validator": Dict of number of errors per type of validator
            ("error_details_per_uid" : Error details, if include_details=True)
    """
    num_uid = [m.get("uid") for m in consolidated_data.get("marches")]
    num_total = len(num_uid)
    num_unique = len(set(num_uid))
    if num_total != num_unique:
        print("Warning : duplicated uids")
    validator = jsonschema.Draft7Validator(consolidated_data_schema)
    filter_keep_any_of = 0
    errors_any_of = validator.iter_errors(consolidated_data)
    error_details_per_uid = {}
    num_errors_per_validator = {}
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
                    num_errors_per_validator[suberror.validator] = 1 + num_errors_per_validator.get(suberror.validator,0)
        error_details_per_uid[instance_uid] = instance_suberrors
    num_invalid_entries = len(error_details_per_uid)
    num_valid_entries = num_total - num_invalid_entries
    share_valid_entries = num_valid_entries / num_total
    share_valid_entries = round(share_valid_entries, 2)
    results = {
        "num_invalid_entries":num_invalid_entries,
        "num_valid_entries":num_valid_entries,
        "share_valid_entries":share_valid_entries,
        "num_errors_per_validator":num_errors_per_validator
    }
    if include_details:
        results["error_details_per_uid"] = error_details_per_uid
    return results
