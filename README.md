# LMS_FILE_DOWNLOAD
lms api를 이용해 수강중인 모든 강의자료를 다운받음.

## Description
수강중인 모든 강의자료실에서 파일을 다운받은뒤, 확장자가 "pdf", "ppt", "doc", "hwp"인 것은 과목명/강의자료 폴더에 저장되고, 그 이외의 확장자인 파일들은 모두 과목명/기타파일 폴더에 저장된다.

## How to Use
1. lms에서 계정-설정으로 들어가 토큰을 발급받고 생성된 API키를 환경변수 "LMS_API_KEY"에 등록해준다.
![image](https://github.com/user-attachments/assets/8007c84a-fd9a-42c0-baac-dde5fbda18db)
2. pip install canvasapi, requests 로 필요한 라이브러리를 설치해준다.
3. lms_file_download.py를 원하는 폴더(ex> Desktop/Univ)에 넣고, 파이썬으로 실행시켜준다.
4. (선택사항) 윈도우의 경우 윈도우 스케줄러, Mac이나 linux의 경우 crontab으로 하루에 한 번씩 실행시켜준다.
