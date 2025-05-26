# 베이스 이미지 설정 (Python 3.10 + 최신 패키지)
FROM python:3.11-slim

# 기본 패키지 설치 (node, curl 등)
RUN apt-get update && apt-get install -y \
    curl gnupg ca-certificates \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN npm install -g @modelcontextprotocol/inspector@0.13.0

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

# 진입점
#ENTRYPOINT ["python", "src/main.py"]

#배포시에는 mcp dev 사용
CMD ["mcp-inspector", "--", "python", "src/main.py"]