# Import the Canvas class
from canvasapi import Canvas
import os

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

courses = canvas.get_courses()
for course in courses:
    course_name = course.name
    course_name = course_name[:course_name.find('-')]
    
    course_file_list = course.get_files()

    if list(course_file_list):
        make_dir(os.path.join(path, course_name))
    else:
        continue

    if any(
        any(ext in file.display_name.lower() for ext in ['pdf', 'ppt', 'doc', 'hwp'])
        for file in course_file_list
    ):
        make_dir(os.path.join(path, course_name, '강의자료'))
    if any(
        not any(ext in file.display_name.lower() for ext in ['pdf', 'ppt', 'doc', 'hwp'])
        for file in course_file_list
    ):
        make_dir(os.path.join(path, course_name, '기타파일'))

    for file in course_file_list:
        file_url = file.url
        filesize = file.size

        # 저장될 경로 설정
        if any(ext in file.display_name.lower() for ext in ['pdf', 'ppt', 'doc', 'hwp']):
            save_path = os.path.join(path, course_name, '강의자료', file.display_name)
        else:
            save_path = os.path.join(path, course_name, '기타파일', file.display_name)

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