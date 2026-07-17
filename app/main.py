from fastapi import FastAPI
from app.router import router
from app.service import initialize_analysis

app = FastAPI(
    title="Phishing Analysis API",
    description="보이스피싱 및 인터넷 사기 회귀분석 API",
    version="1.0.0"
)

# 서버 시작 시 자동 분석
@app.on_event("startup")
def startup_event():
    initialize_analysis()

# API 등록
app.include_router(router)

