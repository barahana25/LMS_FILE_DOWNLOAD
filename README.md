# LMS_FILE_DOWNLOAD

## Description
수강 중인 모든 강의자료실에서 파일을 다운로드한 뒤,  
확장자가 `pdf`, `ppt`, `doc`, `hwp`인 파일은 `과목명/강의자료` 폴더에 저장하고,  
그 외 확장자의 파일은 `과목명/기타파일` 폴더에 저장합니다.  
다운로드할 파일이 없는 경우에는 해당 폴더를 생성하지 않습니다.

## How to Use

### 1. LMS API 키 발급 및 환경변수 등록
- LMS 사이트에서 **계정 → 설정**으로 이동합니다.
- API 키(토큰)를 발급받습니다.
- 발급받은 API 키를 환경변수 `LMS_API_KEY`로 등록합니다.

```bash
# 예시 (Linux/Mac)
export LMS_API_KEY=발급받은_API_키

# 예시 (Windows CMD)
set LMS_API_KEY=발급받은_API_키
```

> 참고: 발급 화면 예시  
> ![API 발급 화면](https://github.com/user-attachments/assets/8007c84a-fd9a-42c0-baac-dde5fbda18db)

### 2. 필요한 라이브러리 설치
필요한 Python 라이브러리를 설치합니다.

```bash
pip install canvasapi requests
```

### 3. 스크립트 실행
`lms_file_download.py` 파일을 원하는 폴더(예: `Desktop/Univ`)에 저장한 후, 다음 명령어로 실행합니다.

```bash
python lms_file_download.py
```

### 4. (선택) 주기적인 자동 실행 설정
- **Windows**: 작업 스케줄러(Task Scheduler)를 사용하여 하루에 한 번 자동 실행 설정
- **Mac/Linux**: `crontab`을 사용하여 자동 실행 설정

**crontab 예시:**

```bash
# 매일 오전 3시에 스크립트 실행
0 3 * * * /usr/bin/python3 /path/to/lms_file_download.py
```

## 주의사항
- `LMS_API_KEY` 환경변수가 설정되지 않으면 스크립트가 정상 실행되지 않습니다.
- API 서버 통신 실패 시 자동 재시도 기능은 포함되어 있지 않습니다.
- 지정된 확장자 외의 파일은 `기타파일` 폴더에 저장됩니다.
- 다운로드할 파일이 없는 경우 해당 과목명 폴더 및 하위 폴더는 생성되지 않습니다.
