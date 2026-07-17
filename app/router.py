from fastapi import APIRouter
from app.service import get_analysis_result

router = APIRouter(
    tags=["분석 결과"]
)

from fastapi import Query


@router.get(
    "/api/analysis",
    summary="범죄 데이터 회귀분석 결과 조회"
)
def analysis(
    dataset: str = Query("data.xlsx")
):
    return get_analysis_result(dataset)
