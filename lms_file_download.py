# Import the Canvas class
from canvasapi import Canvas
import os
from canvasapi.requester import Requester

# CanvasAPI에서 제공하는 Requester 클래스를 상속받아 파일 크기를 확인하는 메서드 추가
class CustomRequester(Requester):
    def _get_filesize(self, url, headers=None):
        headers = headers or {}
        response = self._session.head(url, headers=headers)
        if 'Content-Length' in response.headers:
            return int(response.headers['Content-Length'])
        return None
    
def make_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

path = os.path.dirname(os.path.abspath(__file__))

# Canvas API URL
API_URL = "https://canvas.kumoh.ac.kr"
# Canvas API key
API_KEY = os.environ.get('LMS_API_KEY')

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

# Custom requester to handle file size checking
canvas._Canvas__requester = CustomRequester(API_URL, API_KEY)

courses = canvas.get_courses()
for course in courses:
    course_name = course.name
    course_name = course_name[:course_name.find('-')]
    make_dir(os.path.join(path, course_name))
    make_dir(os.path.join(path, course_name, '강의자료'))
    make_dir(os.path.join(path, course_name, '과제'))

    for file in course.get_files():
        file_url = file.url
        filesize = canvas._Canvas__requester._get_filesize(file_url)
        # 저장될 경로 설정
        if any(ext in file.display_name.lower() for ext in ['pdf', 'ppt', 'hwp']):
            save_path = os.path.join(path, course_name, '강의자료', file.display_name)
        else:
            save_path = os.path.join(path, course_name, '과제', file.display_name)

         # 파일이 존재하면 크기 비교
        if os.path.exists(save_path):
            local_size = os.path.getsize(save_path)
            if filesize is not None and local_size == filesize:
                print(f"✅ 이미 존재하는 파일이며 크기 동일: {file.display_name}, 다운로드 생략")
                continue
            else:
                print(f"🔄 파일 크기 다름, 다시 다운로드: {file.display_name}")
        else:
            print(f"⬇️ 새 파일 다운로드: {file.display_name}")

        file.download(save_path)