from fastapi import APIRouter
from app.service import get_analysis_result

router = APIRouter()

@router.get("/api/analysis")
def analysis():
    """
    분석 결과 반환
    """
    return get_analysis_result()
