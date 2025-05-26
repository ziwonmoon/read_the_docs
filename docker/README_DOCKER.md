# Docker 환경 문서 (Docker Setup Documentation)

## 1. 빌드 및 실행 방법

docker-compose down

docker-compose up --build

실행방법은 추가필요


---

## 2. 주요 파일 및 역할
- `Dockerfile`: Python 3.11 기반, Playwright/llama-index 등 의존성 설치, src 폴더 복사, 엔트리포인트 지정
- `docker-compose.yml`: 서비스 정의, 볼륨 마운트, 포트 매핑 등 설정
- `requirements.txt`: 파이썬 의존성 관리
- `src/`: 실제 서비스 코드(main.py 등)
- `/app/documents`: 문서 저장소(볼륨)

---

## 3. 환경 변수 및 볼륨
- 필요 시 docker-compose.yml에 환경변수 추가 가능
- 문서 저장소는 `/app/documents`에 마운트

---

## 4. Trouble Shooting
- 빌드 오류 발생 시 캐시 삭제 후 재빌드: `docker-compose build --no-cache`
- Playwright 관련 에러: `RUN playwright install`이 Dockerfile에 포함되어 있는지 확인
- llama-index 관련 에러: requirements.txt에 버전 명시 여부 확인

---

## 5. 커스텀 및 확장
- 추가 의존성은 requirements.txt에 명시 후 Dockerfile에 반영
- 서비스 코드(main.py 등)는 src/에 위치

---

## 6. 기타
- 모든 커맨드는 프로젝트 루트 또는 docker 폴더에서 실행 권장
- 추가 수정사항은 README_DOCKER.md에 기록
