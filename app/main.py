from fastapi import FastAPI

from app.router import router
from app.service import initialize_analysis


app = FastAPI(
    title="범죄 데이터 분석 시스템",
    description="보이스피싱 및 인터넷 사기 회귀분석 API",
    version="1.0.0"
)


# API 연결
app.include_router(router)


# 서버 시작 시 분석 실행
@app.on_event("startup")
def startup_event():
    initialize_analysis()


@app.get("/")
def root():
    return {
        "message": "Server Running",
        "docs": "/docs"
    }
