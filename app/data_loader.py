import pandas as pd
import os

BASE_PATH = "data"


def load_data(file_name):
    path = os.path.join(BASE_PATH, file_name)

    if not os.path.exists(path):
        raise FileNotFoundError(path)

    return pd.read_excel(path)
