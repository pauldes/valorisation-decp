import sys

import requests
import pandas
import streamlit.cli as cli

from src import params

def download_data_to_disk(n_rows=None):
    if n_rows is not None:
        url_prefix = f"&rows={int(n_rows)}"
    else:
        url_prefix = ""
    url = params.BASE_URL + url_prefix
    r = requests.get(url, allow_redirects=True, verify=True)
    with open(params.LOCAL_DATASET_PATH, 'wb') as file_writer:
        file_writer.write(r.content)

def load_data_from_disk(n_rows=None):
    return pandas.read_csv(params.LOCAL_DATASET_PATH, sep=";", index_col="id", encoding="utf8", header=0, nrows=n_rows, dtype=params.DATASET_TYPES)

def print_data_shape_and_sample(n_rows=None):
    dataset = load_data_from_disk(n_rows)
    print(dataset.sample(5))
    print(dataset.shape)

def run_web_app():
    sys.argv = ['0','run','./src/webapp.py']
    cli.main()