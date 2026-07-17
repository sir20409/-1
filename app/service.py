import os
from app.data_loader import load_data

# 분석 결과를 저장할 전역 변수
analysis_result = {}


def analyze_data(df):
    """
    여기에 준혁의 회귀분석 코드가 들어갑니다.
    지금은 예시 데이터만 반환합니다.
    """

    return {
        "Y1": {
            "R_squared": 0.82,
            "p_value": 0.003
        },
        "Y2": {
            "R_squared": 0.76,
            "p_value": 0.012
        },
        "images": {
            "residual_plot": "images/residual.png",
            "prediction_plot": "images/prediction.png"
        }
    }


def initialize_analysis():
    """
    서버 시작 시 자동 실행
    """

    global analysis_result

    df = load_data()

    analysis_result = analyze_data(df)


def get_analysis_result():
    """
    API가 호출할 분석 결과 반환
    """

    return analysis_result
