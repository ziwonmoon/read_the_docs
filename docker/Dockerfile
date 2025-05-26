# 베이스 이미지 설정 (Python 3.10 + 최신 패키지)
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Playwright 추가 설치 (크롤링용)
RUN playwright install

# src 폴더 전체 복사
COPY src/ /app/src

# 문서 저장소 마운트 지점
VOLUME /app/documents

# 진입점: 온디맨드 명령 실행
ENTRYPOINT ["python", "src/main.py"]