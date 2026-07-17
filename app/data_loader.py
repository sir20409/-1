import os
import pandas as pd

# 프로젝트 루트 경로
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# data 폴더의 엑셀 파일
DATA_PATH = os.path.join(BASE_DIR, "data", "data.xlsx")


def load_data():
    """
    엑셀 파일을 읽어서 DataFrame 반환
    """
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"파일을 찾을 수 없습니다.\n{DATA_PATH}")

    df = pd.read_excel(DATA_PATH)

    return df
