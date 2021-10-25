import sys
import datetime

import requests
import pandas
import streamlit.cli as cli

from src import params

def download_data_to_disk(n_rows=None):
    if n_rows is not None:
        url_prefix = f"&rows={int(n_rows)}"
    else:
        url_prefix = ""
    url = params.BASE_URL_AUGMENTED + url_prefix
    r = requests.get(url, allow_redirects=True, verify=True)
    with open(params.LOCAL_PATH_AUGMENTED, 'wb') as file_writer:
        file_writer.write(r.content)

def download


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
